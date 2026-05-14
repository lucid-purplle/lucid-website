/* Lightbox — shared component.
   Auto-initialises on DOMContentLoaded. Discovers triggers by selector,
   no per-page configuration. No globals leaked.

   Markup contract:
     - Page contains a single <div class="lightbox">…</div> with
       descendants .lightbox__image and .lightbox__close.
     - Each trigger has class .howit-screenshot__trigger or .muse-thumb
       and contains an <img> child. The img's src/alt is mirrored into
       the lightbox. If the img has a data-full attribute, the lightbox
       initially shows the thumb (instant) and preloads the full image,
       swapping the src once it's ready (so a slow connection never
       leaves the lightbox blank).

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
    var triggers = document.querySelectorAll('.howit-screenshot__trigger, .muse-thumb');
    var lightbox = document.querySelector('.lightbox');
    if (!lightbox || triggers.length === 0) return;
    var lbImage = lightbox.querySelector('.lightbox__image');
    var lbClose = lightbox.querySelector('.lightbox__close');
    var previouslyFocused = null;

    function open(triggerEl) {
      var img = triggerEl.querySelector('img');
      if (!img) return;
      var thumbSrc = img.currentSrc || img.src;
      var fullSrc = img.getAttribute('data-full') || thumbSrc;
      // Show the thumb immediately (zero-latency display)
      lbImage.src = thumbSrc;
      lbImage.alt = img.alt || '';
      // If there's a separate full-size image, preload it and swap in
      // once it's ready. Guard against the user closing the lightbox
      // before the preload finishes.
      if (fullSrc !== thumbSrc) {
        var preloader = new Image();
        preloader.onload = function () {
          if (lightbox.classList.contains('lightbox--open')) {
            lbImage.src = fullSrc;
          }
        };
        preloader.src = fullSrc;
      }
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
