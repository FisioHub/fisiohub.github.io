/**
 * Fisio Hub Lugano — Main Frontend Script
 * Handles mobile menu toggle and keyboard navigation.
 */
document.addEventListener("DOMContentLoaded", () => {
  const openBtn = document.getElementById("mobile-menu-open");
  const closeBtn = document.getElementById("mobile-menu-close");
  const overlay = document.getElementById("mobile-overlay");

  if (openBtn && overlay) {
    openBtn.addEventListener("click", () => {
      overlay.classList.add("is-open");
      overlay.setAttribute("aria-hidden", "false");
    });
  }

  if (closeBtn && overlay) {
    closeBtn.addEventListener("click", () => {
      overlay.classList.remove("is-open");
      overlay.setAttribute("aria-hidden", "true");
    });
  }

  document.addEventListener("keydown", (e) => {
    if (e.key === "Escape" && overlay && overlay.classList.contains("is-open")) {
      overlay.classList.remove("is-open");
      overlay.setAttribute("aria-hidden", "true");
    }
  });
});
