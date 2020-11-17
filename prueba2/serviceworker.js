
var CACHE_NAME = 'my-site-cache-v1';

var urlsToCache = [
    '/web/Principal',
    '/web/Notebook',
    '/static/imagen/logo.png',
    '/static/css/materialize.css',
    '/static/css/materialize.min.css',
    '/static/js/materialize.js',
    '/static/js/materialize.min.js',
];



self.addEventListener('install', function(event) {
    // Perform install steps
    event.waitUntil(
      caches.open(CACHE_NAME)
        .then(function(cache) {
          console.log('Opened cache');
          return cache.addAll(urlsToCache);
        })
    );
  });
  ;

  self.addEventListener('fetch', function(event) {
    event.respondWith(

      fetch(event.request)
      .then((result)=>{
        return caches.open(CACHE_NAME)
        .then(function(c) {
          c.put(event.request.url, result.clone())
          return result;
        })
        
      })
      .catch(function(e){
          return caches.match(event.request)
      })
  

     
    );
});

 
