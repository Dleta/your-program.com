"use strict"

document.addEventListener("DOMContentLoaded", () => {
  const btnMobNav = document.querySelector(".mob-btn");
  const headerEl = document.querySelector(".header");
  const allLinks = document.querySelectorAll("a:link");
  const downloadMobNavBtn = document.querySelector(".download-nav-btn")
  const downloadNav = document.querySelector(".download-nav")

  try{
    btnMobNav.addEventListener("click", function () {
      headerEl.classList.toggle("nav-open");
    });
  }catch{}


  allLinks.forEach(function (link) {
    link.addEventListener("click", function (e) {
      const href = link.getAttribute("href");

      // Close mobile navigation                      might be posibel with a an eventlistener on class mian-nav-link
      if (link.classList.contains("main-nav-link"))
        headerEl.classList.remove("nav-open");
    });
  });

  downloadMobNavBtn.addEventListener("click", () => {
    downloadNav.classList.toggle("hide");
  })

})