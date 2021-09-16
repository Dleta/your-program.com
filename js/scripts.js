function betta_listen(element, e, f) {
  if (element) {
    if (NodeList.prototype.isPrototypeOf(element)) {
      betta_addListeners(element, e, f);
    } else {
      betta_addListener(element, e, f);
    }
  }
}

function betta_changeTheme() {
  try {
    if (document.body.classList.contains("light")) {
      document.body.classList.remove("light");

      localStorage.setItem("light", false);

      return true;
    } else {
      document.body.classList.add("light");

      localStorage.setItem("light", true);

      return true;
    }
  } catch (error) {
    // Could not change theme
  }
  // Could not change theme
  return null;
}

betta_listen(
  document.getElementById("betta_theme-button"),
  "click",
  betta_changeTheme
);

function betta_addListener(element, e, f) {
  element.addEventListener(e, (event) => {
    f(event);
  });
}
