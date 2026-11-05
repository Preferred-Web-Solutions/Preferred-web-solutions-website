/* PWS site script: mobile menu and top-of-page scroll. No cookies, no storage, no third-party requests. */
(function(){
  var btn=document.querySelector('.menu-btn'),nav=document.getElementById('site-nav'),hdr=document.querySelector('.site-header');
  function setOpen(o,refocus){
    if(!nav||!btn)return;
    nav.classList.toggle('open',o);
    btn.setAttribute('aria-expanded',o?'true':'false');
    if(!o&&refocus){btn.focus()}
  }
  if(btn&&nav){
    btn.addEventListener('click',function(){setOpen(!nav.classList.contains('open'),false)});
    document.addEventListener('keydown',function(e){
      if(e.key==='Escape'&&nav.classList.contains('open'))setOpen(false,true);
    });
    document.addEventListener('click',function(e){
      if(nav.classList.contains('open')&&!hdr.contains(e.target))setOpen(false,false);
    });
    /* close when keyboard focus leaves the header; ignore a null relatedTarget (Safari does not focus tapped links) */
    hdr.addEventListener('focusout',function(e){
      var t=e.relatedTarget;
      if(t&&!hdr.contains(t))setOpen(false,false);
    });
    window.addEventListener('resize',function(){if(window.innerWidth>900)setOpen(false,false)});
  }
  /* a new page opens at the top, except Back/Forward or a #hash link */
  try{
    var nt=performance.getEntriesByType&&performance.getEntriesByType('navigation')[0];
    if(!location.hash&&!(nt&&nt.type==='back_forward')){document.documentElement.scrollIntoView()}
  }catch(e){}
})();
