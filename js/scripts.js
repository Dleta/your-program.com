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

window.smartlook ||
  (function (d) {
    var o = (smartlook = function () {
        o.api.push(arguments);
      }),
      h = d.getElementsByTagName("head")[0];
    var c = d.createElement("script");
    o.api = new Array();
    c.async = true;
    c.type = "text/javascript";
    c.charset = "utf-8";
    c.src = "https://rec.smartlook.com/recorder.js";
    h.appendChild(c);
  })(document);
smartlook("init", "4f67633ae3794ffc3d3e3e00761e875332554c27");
