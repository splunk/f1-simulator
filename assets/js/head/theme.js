// Data Drivers uses a fixed dark documentation theme, including without JS.
// Do not inherit another Hextra site's localStorage preference on github.io.
function setTheme() {
  document.documentElement.classList.remove("light");
  document.documentElement.classList.add("dark");
  document.documentElement.style.colorScheme = "dark";
}
setTheme();
