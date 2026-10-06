(function(){
  document.querySelectorAll('[data-slide-viewer]').forEach(function(viewer){
    var images = Array.prototype.slice.call(viewer.querySelectorAll('[data-slide]'));
    var stage = viewer.querySelector('[data-slide-stage] img');
    var counter = viewer.querySelector('[data-slide-counter]');
    var thumbs = viewer.querySelectorAll('[data-slide-thumb]');
    var current = 0;
    function show(i){
      current=(i+images.length)%images.length;
      stage.src=images[current].getAttribute('src');
      stage.alt=images[current].getAttribute('alt') || ('Slide '+(current+1));
      counter.textContent='Slide '+(current+1)+' of '+images.length;
      thumbs.forEach(function(t,n){t.classList.toggle('active',n===current);});
      var active=thumbs[current]; if(active && active.scrollIntoView) active.scrollIntoView({behavior:'smooth',block:'nearest',inline:'center'});
    }
    viewer.querySelector('[data-prev]').addEventListener('click',function(){show(current-1)});
    viewer.querySelector('[data-next]').addEventListener('click',function(){show(current+1)});
    thumbs.forEach(function(t,n){t.addEventListener('click',function(){show(n)});});
    viewer.addEventListener('keydown',function(e){if(e.key==='ArrowLeft')show(current-1);if(e.key==='ArrowRight')show(current+1);});
    show(0);
  });
})();
