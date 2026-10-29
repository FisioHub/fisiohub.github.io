/**
 * Fisio Hub Lugano — Main Frontend Script
 * Mobile menu toggle, keyboard navigation and header state on scroll.
 */
document.addEventListener("DOMContentLoaded", () => {
  const openBtn = document.getElementById("mobile-menu-open");
  const closeBtn = document.getElementById("mobile-menu-close");
  const overlay = document.getElementById("mobile-overlay");

  const setMenu = (open) => {
    if (!overlay) return;
    overlay.classList.toggle("is-open", open);
    overlay.setAttribute("aria-hidden", open ? "false" : "true");
    if (openBtn) openBtn.setAttribute("aria-expanded", open ? "true" : "false");
  };

  if (openBtn) openBtn.addEventListener("click", () => setMenu(true));
  if (closeBtn) closeBtn.addEventListener("click", () => setMenu(false));

  // Close the overlay when a link inside it is followed (e.g. same-page anchors)
  if (overlay) {
    overlay.querySelectorAll("a").forEach((a) =>
      a.addEventListener("click", () => setMenu(false))
    );
  }

  document.addEventListener("keydown", (e) => {
    if (e.key === "Escape") setMenu(false);
  });

  // Solid header once the page has scrolled
  const onScroll = () => {
    document.body.classList.toggle("is-scrolled", window.scrollY > 40);
  };
  onScroll();
  window.addEventListener("scroll", onScroll, { passive: true });
});
