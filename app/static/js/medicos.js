document.addEventListener("DOMContentLoaded", () => {
  const cards = document.querySelectorAll(".card");

  cards.forEach(card => {
    card.addEventListener("click", () => {
      const medicoId = card.getAttribute("data-id");

      switch (medicoId) {
        case "joao-pedro-alves":
          window.location.href = "perfilMedico.html";
          break;
      }
    });
  });

  //Ação do botão solicitação de agendamento
  const agendarButton = document.querySelector(".btn-agendar");
  
  if (agendarButton) {
    agendarButton.addEventListener("click", () => {
      window.location.href = "formulario.html"; // 
    });
  }
});


