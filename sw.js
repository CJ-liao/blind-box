self.addEventListener('install', e => {
  e.waitUntil(caches.open('blindbox-v1').then(c =>
    c.addAll(['/Users/liqian/盲盒游戏/index.html'])
  ));
});
self.addEventListener('fetch', e => {
  e.respondWith(caches.match(e.request).then(r => r || fetch(e.request)));
});
