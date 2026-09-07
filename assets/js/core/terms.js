// Keep glossary definitions available to keyboard users and dismissible with Escape.
document.addEventListener("DOMContentLoaded", () => {
  const terms = document.querySelectorAll(".dd-term");
  for (const term of terms) {
    const show = () => term.removeAttribute("data-dismissed");
    term.addEventListener("mouseenter", show);
    term.addEventListener("focusin", show);
    term.addEventListener("click", show);
  }
  document.addEventListener("keydown", (event) => {
    if (event.key === "Escape") {
      for (const term of terms) term.setAttribute("data-dismissed", "");
    }
  });
});
