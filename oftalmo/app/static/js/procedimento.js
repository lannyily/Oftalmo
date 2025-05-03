
document.addEventListener("DOMContentLoaded", () => {
    const botoesLeiaMais = document.querySelectorAll(".card a");
  
    botoesLeiaMais.forEach((botao, index) => {
      switch (index) {
        case 0:
          botao.setAttribute("href", "perfilProcedimento.html");
          break;
      }
    });
  });
  
  
  