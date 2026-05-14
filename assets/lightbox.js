/* Lightbox — shared component.
   Auto-initialises on DOMContentLoaded. Discovers triggers by selector,
   no per-page configuration. No globals leaked.

   Markup contract:
     - Page contains a single <div class="lightbox">…</div> with
       descendants .lightbox__image and .lightbox__close.
     - Each trigger has class .howit-screenshot__trigger and contains
       an <img> child whose src/alt are mirrored into the lightbox.

   Behaviour:
     - Click trigger → open. Focus moves to close button.
     - Click close button, click overlay (anywhere not the image), or
       press Escape → close. Focus returns to the previously focused el.
     - Body scroll is locked while open.

   Loaded with `defer` — runs after the document is parsed but before
   the DOMContentLoaded event, so the listener below is registered in
   time. */

(function () {
  document.addEventListener('DOMContentLoaded', function () {
    var triggers = document.querySelectorAll('.howit-screenshot__trigger');
    var lightbox = document.querySelector('.lightbox');
    if (!lightbox || triggers.length === 0) return;
    var lbImage = lightbox.querySelector('.lightbox__image');
    var lbClose = lightbox.querySelector('.lightbox__close');
    var previouslyFocused = null;

    function open(triggerEl) {
      var img = triggerEl.querySelector('img');
      if (!img) return;
      lbImage.src = img.currentSrc || img.src;
      lbImage.alt = img.alt || '';
      previouslyFocused = document.activeElement;
      lightbox.classList.add('lightbox--open');
      lightbox.setAttribute('aria-hidden', 'false');
      document.body.style.overflow = 'hidden';
      lbClose.focus();
    }

    function close() {
      if (!lightbox.classList.contains('lightbox--open')) return;
      lightbox.classList.remove('lightbox--open');
      lightbox.setAttribute('aria-hidden', 'true');
      document.body.style.overflow = '';
      // clear src after transition so the image doesn't flash on next open
      setTimeout(function () { lbImage.src = ''; }, 200);
      if (previouslyFocused && typeof previouslyFocused.focus === 'function') {
        previouslyFocused.focus();
      }
    }

    triggers.forEach(function (t) {
      t.addEventListener('click', function () { open(t); });
    });

    lightbox.addEventListener('click', function (e) {
      // Close when clicking the overlay (anywhere that isn't the image itself)
      if (e.target !== lbImage) close();
    });

    lbClose.addEventListener('click', function (e) {
      e.stopPropagation();
      close();
    });

    document.addEventListener('keydown', function (e) {
      if (e.key === 'Escape') close();
    });
  });
})();
