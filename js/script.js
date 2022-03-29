const btnMobNav = document.querySelector(".mob-btn");
const headerEl = document.querySelector(".header");
const allLinks = document.querySelectorAll("a:link");
try{
  btnMobNav.addEventListener("click", function () {
    headerEl.classList.toggle("nav-open");
  });
}catch{}


allLinks.forEach(function (link) {
  link.addEventListener("click", function (e) {
    const href = link.getAttribute("href");

    // Close mobile navigation
    if (link.classList.contains("main-nav-link"))
      headerEl.classList.remove("nav-open");
  });
});

