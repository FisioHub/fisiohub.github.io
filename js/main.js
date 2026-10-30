/**
 * Fisio Hub Lugano — Main Frontend Script
 * Mobile menu toggle, keyboard navigation, language switch and header state on scroll.
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

  // Language switch: stay on the same section (#anchor) when changing language
  document.querySelectorAll(".lang-switch a").forEach((a) =>
    a.addEventListener("click", () => {
      if (window.location.hash) a.hash = window.location.hash;
    })
  );

  // Hero video: make sure it is muted and try to start it. Some phones block
  // autoplay (e.g. iPhone Low Power Mode); then the poster image stays visible
  // and we retry on the first touch / scroll, which counts as a user gesture.
  document.querySelectorAll(".hero-video").forEach((video) => {
    video.muted = true;
    video.defaultMuted = true;
    video.setAttribute("muted", "");
    const tryPlay = () => {
      const p = video.play();
      if (p && typeof p.catch === "function") p.catch(() => {});
    };
    tryPlay();
    const onGesture = () => {
      if (video.paused) tryPlay();
      ["touchstart", "click", "scroll"].forEach((ev) =>
        window.removeEventListener(ev, onGesture)
      );
    };
    ["touchstart", "click", "scroll"].forEach((ev) =>
      window.addEventListener(ev, onGesture, { passive: true })
    );
    document.addEventListener("visibilitychange", () => {
      if (!document.hidden && video.paused) tryPlay();
    });
  });

  // Solid header once the page has scrolled
  const onScroll = () => {
    document.body.classList.toggle("is-scrolled", window.scrollY > 40);
  };
  onScroll();
  window.addEventListener("scroll", onScroll, { passive: true });
});
