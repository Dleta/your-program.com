const btnX = document.querySelector(".mobile-nav-close-btn");
const btnM = document.querySelector(".mobile-nav-open-btn");
const headerEl = document.querySelector(".header");

btnM.addEventListener("click", function () {
  headerEl.classList.add("nav-open");
});

btnX.addEventListener("click", function () {
  headerEl.classList.remove("nav-open");
});
