/* ============================================================
   Copy button — shared component.
   Auto-initialises. Uses document-level click delegation, so it
   handles both static buttons and buttons inserted into the DOM
   later (e.g. the gallery detail overlay's templated content,
   which is cloned on open).

   Markup contract:
     <div class="copy-block">
       … <button class="gallery-copy" type="button">Copy</button> …
       <el class="js-copy-text"> … text to be copied … </el>
     </div>
   On click, the button copies the .js-copy-text element's text
   (its rendered text — newlines preserved for <pre>, paragraph
   breaks preserved for stacked <p>). Falls back to execCommand
   when the async Clipboard API is unavailable or rejects.
   ============================================================ */

(function () {
  function flashCopied(btn) {
    btn.classList.add('is-copied');
    btn.textContent = 'Copied';
    setTimeout(function () {
      btn.classList.remove('is-copied');
      btn.textContent = 'Copy';
    }, 2000);
  }

  function copyFallback(text) {
    var ta = document.createElement('textarea');
    ta.value = text;
    ta.setAttribute('readonly', '');
    ta.style.position = 'fixed';
    ta.style.top = '0';
    ta.style.opacity = '0';
    document.body.appendChild(ta);
    ta.select();
    try { document.execCommand('copy'); } catch (err) { /* no-op */ }
    document.body.removeChild(ta);
  }

  document.addEventListener('click', function (e) {
    var btn = e.target.closest('.gallery-copy');
    if (!btn) return;
    var block = btn.closest('.copy-block');
    var src = block && block.querySelector('.js-copy-text');
    if (!src) return;
    var text = src.innerText;
    if (navigator.clipboard && navigator.clipboard.writeText) {
      navigator.clipboard.writeText(text).then(
        function () { flashCopied(btn); },
        function () { copyFallback(text); flashCopied(btn); }
      );
    } else {
      copyFallback(text);
      flashCopied(btn);
    }
  });
})();
