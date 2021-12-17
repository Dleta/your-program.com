const btnMobNav = document.querySelector(".mob-btn");
const headerEl = document.querySelector(".header");
const allLinks = document.querySelectorAll("a:link");

btnMobNav.addEventListener("click", function () {
  headerEl.classList.toggle("nav-open");
});

allLinks.forEach(function (link) {
  link.addEventListener("click", function (e) {
    const href = link.getAttribute("href");

    // Close mobile navigation
    if (link.classList.contains("main-nav-link"))
      headerEl.classList.remove("nav-open");
  });
});
