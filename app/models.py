from django.db import models
from django.db.utils import OperationalError, ProgrammingError
from django.db import connection
from django.core.management import call_command
import logging
from django.apps import apps
from django.core.signals import request_started
from django.dispatch import receiver

logger = logging.getLogger(__name__)




class ModelBase(models.Model):
    """Classe abstrata base com verificação de tabela"""
    class Meta:
        abstract = True

    @classmethod
    def _safe_table_check(cls):
        """Verificação segura sem causar erros de inicialização"""
        try:
            with connection.cursor() as cursor:
                if connection.vendor == 'sqlite':
                    cursor.execute(
                        "SELECT name FROM sqlite_master "
                        "WHERE type='table' AND name=%s",
                        [cls._meta.db_table]
                    )
                else:
                    cursor.execute(
                        "SELECT table_name FROM information_schema.tables "
                        "WHERE table_name = %s",
                        [cls._meta.db_table]
                    )
                return bool(cursor.fetchone())
        except Exception:
            return False

    @classmethod
    def ensure_table_exists(cls):
        """Versão segura para chamar durante o runtime"""
        if not cls._safe_table_check():
            logger.warning(f"Criando tabela {cls._meta.db_table}...")
            try:
                call_command('migrate', cls._meta.app_label, verbosity=0)
                return True
            except Exception as e:
                logger.error(f"Falha ao criar tabela: {str(e)}")
                return False
        return True

    def save(self, *args, **kwargs):
        if not self.ensure_table_exists():
            raise Exception(f"Falha na verificação da tabela {self.__class__.__name__}")
        super().save(*args, **kwargs)


class Medico(ModelBase):
    foto = models.ImageField(upload_to='medicos/')
    nome = models.CharField(max_length=100)
    numero_cmr = models.CharField(max_length=50)
    especialidades = models.CharField(max_length=200)
    atendimento = models.TextField(help_text="Ex: Segunda a Sexta, das 08h às 18h")
    diferenciais = models.TextField()
    formacao = models.TextField()
    procedimentos = models.ManyToManyField('Procedimento', related_name='medicos', blank=True)

    def __str__(self):
        return self.nome


class Procedimento(ModelBase):
    TIPO_CHOICES = [
        ('rotina', 'Exames de Rotina'),
        ('avancado', 'Exames Diagnósticos Avançados'),
        ('ambulatorial', 'Tratamentos e Procedimentos Ambulatoriais'),
        ('cirurgia', 'Cirurgias Oftalmológicas'),
    ]

    foto = models.ImageField(upload_to='procedimentos/')
    nome = models.CharField(max_length=100)
    descricao = models.TextField()
    tipo = models.CharField(max_length=20, choices=TIPO_CHOICES)
   
    tempo_procedimento = models.DurationField(help_text="Ex: 00:30:00 para 30 minutos")
    informacao_internacao = models.TextField()
    informacao_recuperacao = models.TextField()

    def __str__(self):
        return self.nome


class HorarioProcedimento(models.Model):
    DIA_CHOICES = [
        ('segunda', 'Segunda-feira'),
        ('terca', 'Terça-feira'),
        ('quarta', 'Quarta-feira'),
        ('quinta', 'Quinta-feira'),
        ('sexta', 'Sexta-feira'),
    ]

    TURNO_CHOICES = [
        ('manha', 'Manhã'),
        ('tarde', 'Tarde'),
    ]

    procedimento = models.ForeignKey(Procedimento, on_delete=models.CASCADE, related_name='horarios')
    dia = models.CharField(max_length=10, choices=DIA_CHOICES)
    turno = models.CharField(max_length=10, choices=TURNO_CHOICES)
    hora_inicio = models.TimeField()
    hora_fim = models.TimeField()

    class Meta:
        unique_together = ('procedimento', 'dia', 'turno', 'hora_inicio', 'hora_fim')
        ordering = ['procedimento', 'dia', 'turno', 'hora_inicio']

    def __str__(self):
        return f'{self.procedimento.nome} - {self.get_dia_display()} ({self.get_turno_display()}) {self.hora_inicio} às {self.hora_fim}'



class ProcedimentoDestaque(models.Model):
    procedimento = models.OneToOneField(
        Procedimento,
        on_delete=models.CASCADE,
        verbose_name="Procedimento em destaque"
    )
    ordem = models.PositiveIntegerField(default=0)
    data_criacao = models.DateTimeField(auto_now_add=True)
    
    class Meta:
        ordering = ['ordem']
        verbose_name = "Procedimento em Destaque"
        verbose_name_plural = "Procedimentos em Destaque"

    def __str__(self):
        return f"Destaque {self.ordem}: {self.procedimento.nome}"

class MedicoDestaque(models.Model):
    medico = models.OneToOneField(
        Medico,
        on_delete=models.CASCADE,
        verbose_name="Médico em destaque"
    )
    ordem = models.PositiveIntegerField(default=0)
    data_criacao = models.DateTimeField(auto_now_add=True)
    
    class Meta:
        ordering = ['ordem']
        verbose_name = "Médico em Destaque"
        verbose_name_plural = "Médicos em Destaque"

    def __str__(self):
        return f"Destaque {self.ordem}: {self.medico.nome}"
    
# Verificação inicial quando o modelo é carregado
try:
    Medico.ensure_table_exists()
    Procedimento.ensure_table_exists()
except Exception as e:
    logger.error(f"Erro na verificação inicial: {str(e)}")

DIAS_SEMANA = [
    ('segunda', 'Segunda'),
    ('terca', 'Terça'),
    ('quarta', 'Quarta'),
    ('quinta', 'Quinta'),
    ('sexta', 'Sexta'),
]

class Consulta(models.Model):
    nome = models.CharField(max_length=100)
    telefone = models.CharField(max_length=20)
    email = models.EmailField()
    cpf = models.CharField(max_length=14)
    dia = models.CharField(max_length=10, choices=DIAS_SEMANA)
    medico = models.ForeignKey(Medico, on_delete=models.CASCADE)
    mensagem = models.TextField(blank=True)
    data_atribuida = models.DateField(null=True, blank=True)
    confirmada = models.BooleanField(default=False)

    criado_em = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f'{self.nome} - {self.dia} - {self.medico.nome}'
    
class ConsultaConfirmadaManager(models.Manager):
    def get_queryset(self):
        return super().get_queryset().filter(confirmada=True)

class ConsultaConfirmada(Consulta):
    objects = ConsultaConfirmadaManager()

    class Meta:
        proxy = True
        verbose_name = "Consulta Confirmada"
        verbose_name_plural = "Calendário de Agendamento"
