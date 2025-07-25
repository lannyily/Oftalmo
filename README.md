# Clínica Oftalmo+ - Sistema de Agendamento

Este projeto foi desenvolvido com Django como **trabalho prático** de sistema web para uma **clínica oftalmológica**. Ele permite o cadastro de médicos, procedimentos e a solicitação de agendamento de consultas pelos pacientes por meio do site. O sistema envia confirmações automáticas e conta com um **painel administrativo completo**, projetado para facilitar o trabalho de secretários(as).

## Funcionalidades

* Cadastro de médicos
* Cadastro de procedimentos oftalmológicos
* Solicitação de agendamento de consultas online
* Confirmação automática por WhatsApp
* Área administrativa segura com:

  * Listagem de agendamentos com filtros por:

    * Procedimento
    * Médico
    * Data
    * Turno
  * Edição e remoção de registros
  * Painel organizado e customizado para facilitar o fluxo da secretaria
* Interface responsiva baseada em protótipo no Figma

## Estrutura de diretórios

```
app/
├── admin.py
├── apps.py
├── forms.py
├── mensagem.py
├── models.py
├── signals.py
├── urls.py
├── views/
├── templates/
├── static/
├── templatetags/
└── migrations/
project/
├── settings.py
├── urls.py
└── wsgi.py
manage.py
```

## Tecnologias utilizadas

* Python 3.10+
* Django 4.x
* PostgreSQL
* Bootstrap 5
* HTML/CSS
* JavaScript (para interações dinâmicas no formulário)
* Figma (protótipos da interface)

## Protótipo no Figma

> A interface foi planejada com foco em **usabilidade**, especialmente para facilitar o uso por secretários(as) da clínica.

Acesse o protótipo no Figma aqui:
**[Link para o Figma](https://www.figma.com/design/CzI43YxLK3zwwWlXMID4Ov/Oftalmo-?node-id=0-1&t=6pUiZSIk61YAkkCz-1)**

## Como executar o projeto localmente

1. Crie um ambiente virtual:

```bash
python -m venv venv
source venv/bin/activate  # ou venv\Scripts\activate no Windows
```

2. Aplique as migrações:

```bash
python manage.py migrate
```

3. Crie um superusuário:

```bash
python manage.py createsuperuser
```

4. Execute o servidor:

```bash
python manage.py runserver
```

5. Acesse o sistema:

* Página inicial: [http://localhost:8000](http://localhost:8000)
* Admin: [http://localhost:8000/admin](http://localhost:8000/admin)

## Personalizações no Admin

* Filtros por **turno, médico, procedimento e data**
* Campos organizados e renomeados para melhor legibilidade
* Tabelas de agendamentos com colunas destacadas
* Interface adaptada com ações administrativas rápidas

## Confirmações automáticas

Ao solicitar uma consulta, o paciente recebe:

* Mensagem via WhatsApp, com dados da consulta

## Desenvolvido por

> Erlanny Rodrigues
> Naiana Silva
> Andressa Caroline
> Sistemas de Informação - UFPI - CSHNB

