// Outdoor Adventures BC — service worker
const VERSION = 'v1-2026-04-22';
const CORE = [
  '/',
  '/offline.html',
  '/assets/css/styles.css',
  '/assets/js/main.js',
  '/assets/img/outdoor-adventures-bc-logo-coloured.png',
  '/assets/img/hero-poster.webp',
  '/assets/img/favicon-192.png',
  '/site.webmanifest'
];

self.addEventListener('install', (e) => {
  e.waitUntil(caches.open(VERSION).then(c => c.addAll(CORE)).then(() => self.skipWaiting()));
});

self.addEventListener('activate', (e) => {
  e.waitUntil(
    caches.keys().then(keys => Promise.all(keys.filter(k => k !== VERSION).map(k => caches.delete(k))))
      .then(() => self.clients.claim())
  );
});

self.addEventListener('fetch', (e) => {
  if (e.request.method !== 'GET') return;
  const url = new URL(e.request.url);
  if (url.origin !== location.origin) return; // ignore cross-origin
  // Network first for HTML; cache fallback + offline page
  if (e.request.mode === 'navigate' || (e.request.headers.get('accept') || '').includes('text/html')) {
    e.respondWith(
      fetch(e.request).then(res => {
        const copy = res.clone(); caches.open(VERSION).then(c => c.put(e.request, copy));
        return res;
      }).catch(() => caches.match(e.request).then(r => r || caches.match('/offline.html')))
    );
    return;
  }
  // Stale-while-revalidate for static assets
  e.respondWith(
    caches.match(e.request).then(cached => {
      const fetching = fetch(e.request).then(res => {
        const copy = res.clone(); caches.open(VERSION).then(c => c.put(e.request, copy)); return res;
      }).catch(() => cached);
      return cached || fetching;
    })
  );
});
