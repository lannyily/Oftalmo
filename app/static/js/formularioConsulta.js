/*document.addEventListener("DOMContentLoaded", function () {
  const form = document.getElementById("formAgendamento");
  if (!form) return;

  form.addEventListener("submit", function(event) {
    event.preventDefault(); // Evita envio normal para poder mostrar o alerta

    // Envia os dados do formulário com fetch (AJAX)
    const formData = new FormData(form);

    fetch(form.action, {
      method: "POST",
      body: formData,
      headers: {
        'X-CSRFToken': form.querySelector('[name=csrfmiddlewaretoken]').value
      }
    })
    .then(response => {
      if (response.ok) {
        alert("Sua solicitação foi enviada com sucesso!");
        window.location.href = "/"; // Redireciona para a home
      } else {
        alert("Houve um erro ao enviar. Tente novamente.");
      }
    })
    .catch(error => {
      console.error("Erro:", error);
      alert("Erro de rede. Verifique sua conexão.");
    });
  });
});*/

document.addEventListener("DOMContentLoaded", function () {
  const form = document.getElementById("formAgendamento");
  if (!form) return;

  form.addEventListener("submit", function(event) {
    // Verifica se o formulário é válido
    if (!form.checkValidity()) {
      // Se não for válido, deixa o navegador mostrar os balões
      return;
    }

    // Se for válido, impede o envio padrão e continua com o AJAX
    event.preventDefault();

    const formData = new FormData(form);

    fetch(form.action, {
      method: "POST",
      body: formData,
      headers: {
        'X-CSRFToken': form.querySelector('[name=csrfmiddlewaretoken]').value
      }
    })
    .then(response => {
      if (response.ok) {
        alert("Sua solicitação foi enviada com sucesso!");
        window.location.href = "/"; // Redireciona para a home
      } else {
        alert("Houve um erro ao enviar. Tente novamente.");
      }
    })
    .catch(error => {
      console.error("Erro:", error);
      alert("Erro de rede. Verifique sua conexão.");
    });
  });
});

