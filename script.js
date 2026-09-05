document.addEventListener("DOMContentLoaded", () => {
  const card = document.querySelector(".card");
  if (card) {
    card.style.opacity = "0";
    card.style.transform = "translateY(18px)";

    requestAnimationFrame(() => {
      card.style.transition = "all 1s ease";
      card.style.opacity = "1";
      card.style.transform = "translateY(0)";
    });
  }
});
