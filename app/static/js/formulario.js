document.addEventListener("DOMContentLoaded", function () {
  const form = document.getElementById("formAgendamento");
  const mensagemDiv = document.getElementById("mensagem");

  if (!form) return;

  form.addEventListener("submit", function(event) {
    
    if (mensagemDiv) {
      mensagemDiv.textContent = "Enviando...";
      mensagemDiv.style.display = "block";
    }

    
  });
});
