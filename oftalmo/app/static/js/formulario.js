document.addEventListener("DOMContentLoaded", function () {
  document.getElementById("formAgendamento").addEventListener("submit", function(event) {
    event.preventDefault();

    const nome = event.target.elements["nome"].value;
    const mensagemDiv = document.getElementById("mensagemSucesso");

    mensagemDiv.textContent = "Sua solicitação foi enviada com sucesso.";
    mensagemDiv.style.display = "block";

    this.reset(); 
  });
});

  