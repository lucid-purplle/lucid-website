/* ============================================================
   Accordion — shared component.
   Auto-initialises. Document-level click delegation, so it works
   for items present at load and any added later.
   Multi-open: toggling one item never affects the others.

   Markup contract:
     <button class="accordion__header" type="button"
             aria-expanded="false" aria-controls="ID">
       … <span class="accordion__plus">+</span>
     </button>
     <div class="accordion__body is-collapsed" id="ID"> … </div>
   Clicking a header flips its aria-expanded and toggles the
   is-collapsed class on the body it controls.
   ============================================================ */

(function () {
  document.addEventListener('click', function (e) {
    var header = e.target.closest('.accordion__header');
    if (!header) return;
    var expanded = header.getAttribute('aria-expanded') === 'true';
    header.setAttribute('aria-expanded', String(!expanded));
    var body = document.getElementById(header.getAttribute('aria-controls'));
    if (body) body.classList.toggle('is-collapsed');
  });
})();
