// Outdoor Adventures BC — interactions
(function () {
  const ready = (fn) => (document.readyState !== 'loading') ? fn() : document.addEventListener('DOMContentLoaded', fn);

  ready(() => {
    // Mobile nav toggle
    const btn = document.querySelector('.nav-toggle');
    const list = document.querySelector('.nav ul');
    if (btn && list) {
      btn.addEventListener('click', () => {
        const open = list.classList.toggle('open');
        btn.setAttribute('aria-expanded', open ? 'true' : 'false');
      });
      list.querySelectorAll('a').forEach(a => a.addEventListener('click', () => list.classList.remove('open')));
    }

    // Year in footer
    document.querySelectorAll('[data-year]').forEach(el => el.textContent = new Date().getFullYear());

    // Elevate nav on scroll
    const nav = document.querySelector('.nav');
    const onScroll = () => {
      if (!nav) return;
      if (window.scrollY > 8) nav.classList.add('scrolled');
      else nav.classList.remove('scrolled');
    };
    document.addEventListener('scroll', onScroll, { passive: true });
    onScroll();

    // Reveal on scroll
    const reducedMotion = window.matchMedia('(prefers-reduced-motion: reduce)').matches;
    const revealEls = document.querySelectorAll('.reveal, .reveal-left, .reveal-right, .reveal-scale');
    if ('IntersectionObserver' in window && !reducedMotion) {
      const io = new IntersectionObserver((entries) => {
        for (const e of entries) {
          if (e.isIntersecting) {
            e.target.classList.add('in');
            io.unobserve(e.target);
          }
        }
      }, { threshold: 0.12, rootMargin: '0px 0px -40px 0px' });
      revealEls.forEach(el => io.observe(el));
    } else {
      revealEls.forEach(el => el.classList.add('in'));
    }

    // Button pointer ripple
    document.querySelectorAll('.btn').forEach(b => {
      b.addEventListener('pointermove', (e) => {
        const r = b.getBoundingClientRect();
        b.style.setProperty('--mx', ((e.clientX - r.left) / r.width * 100) + '%');
        b.style.setProperty('--my', ((e.clientY - r.top) / r.height * 100) + '%');
      });
    });

    // Counter animation for stats
    const counters = document.querySelectorAll('.stat strong[data-count]');
    if (counters.length && 'IntersectionObserver' in window && !reducedMotion) {
      const cio = new IntersectionObserver((entries) => {
        entries.forEach(e => {
          if (!e.isIntersecting) return;
          const el = e.target;
          const target = parseFloat(el.dataset.count);
          const suffix = el.dataset.suffix || '';
          const dur = 1400;
          const start = performance.now();
          const step = (now) => {
            const t = Math.min(1, (now - start) / dur);
            const eased = 1 - Math.pow(1 - t, 3);
            const val = target % 1 ? (target * eased).toFixed(1) : Math.floor(target * eased);
            el.textContent = val + suffix;
            if (t < 1) requestAnimationFrame(step);
          };
          requestAnimationFrame(step);
          el.closest('.stat')?.classList.add('in-view');
          cio.unobserve(el);
        });
      }, { threshold: 0.5 });
      counters.forEach(c => cio.observe(c));
    }

    // Smooth scroll for internal hash links (adds easing beyond CSS smooth-scroll)
    document.querySelectorAll('a[href^="#"]').forEach(a => {
      a.addEventListener('click', (e) => {
        const id = a.getAttribute('href');
        if (id.length < 2) return;
        const t = document.querySelector(id);
        if (!t) return;
        e.preventDefault();
        t.scrollIntoView({ behavior: 'smooth', block: 'start' });
      });
    });
  });
})();
