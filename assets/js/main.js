// Outdoor Adventures BC — interactions (max polish)
(function () {
  const ready = (fn) => (document.readyState !== 'loading') ? fn() : document.addEventListener('DOMContentLoaded', fn);

  // Register service worker (PWA + offline)
  if ('serviceWorker' in navigator && location.protocol !== 'file:') {
    window.addEventListener('load', () => {
      navigator.serviceWorker.register('/sw.js').catch(() => {});
    });
  }
  const reducedMotion = window.matchMedia('(prefers-reduced-motion: reduce)').matches;

  ready(() => {
    /* ---------- Mobile nav ---------- */
    const btn = document.querySelector('.nav-toggle');
    const list = document.querySelector('.nav ul');
    if (btn && list) {
      btn.addEventListener('click', () => {
        const open = list.classList.toggle('open');
        btn.setAttribute('aria-expanded', open ? 'true' : 'false');
      });
      list.querySelectorAll('a').forEach(a => a.addEventListener('click', () => list.classList.remove('open')));
    }

    /* ---------- Year in footer ---------- */
    document.querySelectorAll('[data-year]').forEach(el => el.textContent = new Date().getFullYear());

    /* ---------- Scroll-driven effects ---------- */
    const nav = document.querySelector('.nav');
    const progress = document.querySelector('.scroll-progress');
    const stickyBar = document.querySelector('.sticky-book');
    const onScroll = () => {
      const y = window.scrollY;
      if (nav) nav.classList.toggle('scrolled', y > 8);
      if (progress) {
        const h = document.documentElement.scrollHeight - window.innerHeight;
        progress.style.width = (h > 0 ? (y / h) * 100 : 0) + '%';
      }
      if (stickyBar) stickyBar.classList.toggle('visible', y > 600);
    };
    document.addEventListener('scroll', onScroll, { passive: true });
    onScroll();

    /* ---------- Reveal on scroll ---------- */
    const revealEls = document.querySelectorAll('.reveal, .reveal-left, .reveal-right, .reveal-scale');
    if ('IntersectionObserver' in window && !reducedMotion) {
      const io = new IntersectionObserver((entries) => {
        for (const e of entries) {
          if (e.isIntersecting) { e.target.classList.add('in'); io.unobserve(e.target); }
        }
      }, { threshold: 0.12, rootMargin: '0px 0px -40px 0px' });
      revealEls.forEach(el => io.observe(el));
    } else {
      revealEls.forEach(el => el.classList.add('in'));
    }

    /* ---------- Button ripple ---------- */
    document.querySelectorAll('.btn').forEach(b => {
      b.addEventListener('pointermove', (e) => {
        const r = b.getBoundingClientRect();
        b.style.setProperty('--mx', ((e.clientX - r.left) / r.width * 100) + '%');
        b.style.setProperty('--my', ((e.clientY - r.top) / r.height * 100) + '%');
      });
    });

    /* ---------- Counters ---------- */
    const counters = document.querySelectorAll('.stat strong[data-count]');
    if (counters.length && 'IntersectionObserver' in window && !reducedMotion) {
      const cio = new IntersectionObserver((entries) => {
        entries.forEach(e => {
          if (!e.isIntersecting) return;
          const el = e.target;
          const target = parseFloat(el.dataset.count);
          const suffix = el.dataset.suffix || '';
          const dur = 1400, start = performance.now();
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

    /* ---------- Smooth anchor scroll ---------- */
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

    /* ---------- Custom cursor (desktop only, hover-capable) ---------- */
    if (window.matchMedia('(hover: hover) and (pointer: fine)').matches && !reducedMotion && window.innerWidth > 900) {
      const dot = document.createElement('div'); dot.className = 'cursor-dot';
      const ring = document.createElement('div'); ring.className = 'cursor-ring';
      document.body.append(dot, ring);
      document.body.classList.add('has-custom-cursor');
      let rx = window.innerWidth/2, ry = window.innerHeight/2;
      let tx = rx, ty = ry;
      document.addEventListener('pointermove', (e) => {
        tx = e.clientX; ty = e.clientY;
        dot.style.transform = `translate(${tx - 4}px, ${ty - 4}px)`;
      });
      const loop = () => {
        rx += (tx - rx) * 0.18; ry += (ty - ry) * 0.18;
        ring.style.transform = `translate(${rx - 20}px, ${ry - 20}px)`;
        requestAnimationFrame(loop);
      };
      requestAnimationFrame(loop);
      document.querySelectorAll('a, button, .btn, .card, .ig-tile').forEach(el => {
        el.addEventListener('pointerenter', () => document.body.classList.add('cursor-hover'));
        el.addEventListener('pointerleave', () => document.body.classList.remove('cursor-hover'));
      });
    }

    /* ---------- Map skeleton ---------- */
    document.querySelectorAll('.map-frame iframe').forEach(ifr => {
      ifr.addEventListener('load', () => ifr.parentElement.classList.add('loaded'));
    });

    /* ---------- Weather widget ---------- */
    const wx = document.querySelector('[data-weather]');
    if (wx) {
      fetch('https://api.open-meteo.com/v1/forecast?latitude=49.888&longitude=-119.496&current=temperature_2m,wind_speed_10m,weather_code&timezone=America%2FVancouver')
        .then(r => r.json())
        .then(d => {
          const t = Math.round(d.current.temperature_2m);
          const w = Math.round(d.current.wind_speed_10m);
          const codeMap = {0:'☀️',1:'🌤️',2:'⛅',3:'☁️',45:'🌫️',48:'🌫️',51:'🌦️',53:'🌦️',55:'🌧️',61:'🌧️',63:'🌧️',65:'🌧️',71:'🌨️',73:'🌨️',75:'❄️',80:'🌦️',81:'🌧️',82:'⛈️',95:'⛈️'};
          const icon = codeMap[d.current.weather_code] || '🌤️';
          wx.innerHTML = `<span class="wx-icon">${icon}</span><span>Kelowna now <strong>${t}°C</strong> · wind ${w} km/h</span>`;
        })
        .catch(() => wx.innerHTML = '<span class="wx-icon">🌊</span><span>Kelowna, BC · on the water 7 days a week</span>');
    }

    /* ---------- Exit-intent modal (desktop) ---------- */
    const modalKey = 'oabc-exit-shown';
    const backdrop = document.querySelector('#exit-modal');
    if (backdrop && !sessionStorage.getItem(modalKey) && window.innerWidth > 820) {
      let shown = false;
      const show = () => {
        if (shown) return;
        shown = true;
        backdrop.classList.add('open');
        sessionStorage.setItem(modalKey, '1');
      };
      document.addEventListener('mouseout', (e) => {
        if (!e.relatedTarget && e.clientY < 30) show();
      });
      // Also show after 45s if they haven't left yet
      setTimeout(show, 45000);
      backdrop.addEventListener('click', (e) => { if (e.target === backdrop) backdrop.classList.remove('open'); });
      backdrop.querySelectorAll('[data-close]').forEach(b => b.addEventListener('click', () => backdrop.classList.remove('open')));
    }

    /* ---------- Hero video: pause off-screen, respect data-saver ---------- */
    const hv = document.querySelector('.hero-video');
    if (hv) {
      const conn = navigator.connection;
      if (conn && (conn.saveData || /2g/.test(conn.effectiveType))) {
        hv.pause(); hv.removeAttribute('autoplay'); hv.removeAttribute('src');
        // poster remains
      } else {
        hv.play().catch(() => {});
        if ('IntersectionObserver' in window) {
          const hvio = new IntersectionObserver(([e]) => { e.isIntersecting ? hv.play().catch(()=>{}) : hv.pause(); }, { threshold: 0.1 });
          hvio.observe(hv);
        }
      }
    }

    /* ---------- Active nav highlight ---------- */
    const path = location.pathname.replace(/\/$/,'') || '/';
    document.querySelectorAll('.nav a.navlink').forEach(a => {
      const href = a.getAttribute('href').replace(/\/$/,'') || '/';
      if (href === path || (href !== '/' && path.startsWith(href))) a.classList.add('active');
    });
  });
})();
