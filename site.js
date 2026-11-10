/* PWS site script: mobile menu, fade-in on scroll and top-of-page scroll. No cookies, no storage, no third-party requests. */
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
    window.addEventListener('resize',function(){if(window.innerWidth>1060)setOpen(false,false)});
  }
  /* fade sections in as they scroll into view; skipped when the device asks for reduced motion */
  try{
    var reduce=window.matchMedia&&window.matchMedia('(prefers-reduced-motion: reduce)').matches;
    if(!reduce&&'IntersectionObserver' in window){
      var sel='main .sec-head, main .steps > li, main .plan, main .shot, main .shots-note, main .panel, main .compare, main .why-grid > div:first-child, main .entry, main .coming, main .faq, main .principles > li, main .owner, main .prose, main .refer, main .place-list, main .where > div:first-child, main .band .wrap > *, main .disclaimer';
      var els=[].slice.call(document.querySelectorAll(sel)).filter(function(el){return !el.closest('.hero')});
      els.forEach(function(el){
        var sibs=[].filter.call(el.parentNode.children,function(c){return els.indexOf(c)>-1});
        el.style.setProperty('--rv-d',Math.min(sibs.indexOf(el)*80,320)+'ms');
        el.classList.add('rv');
      });
      var io=new IntersectionObserver(function(ents){
        ents.forEach(function(en){if(en.isIntersecting){en.target.classList.add('in');io.unobserve(en.target)}});
      },{rootMargin:'0px 0px -8% 0px',threshold:0});
      document.documentElement.classList.add('rv-on');
      els.forEach(function(el){io.observe(el)});
    }
  }catch(e){}
  /* a new page opens at the top, except Back/Forward or a #hash link */
  function top(){window.scrollTo(0,0);document.documentElement.scrollTop=0;if(document.body)document.body.scrollTop=0}
  try{
    var nt=performance.getEntriesByType&&performance.getEntriesByType('navigation')[0];
    var back=nt&&nt.type==='back_forward';
    if(!location.hash&&!back){
      if('scrollRestoration' in history)history.scrollRestoration='manual';
      top();
      document.addEventListener('DOMContentLoaded',top);
      window.addEventListener('load',function(){top();setTimeout(top,60)});
    }
    window.addEventListener('pageshow',function(e){if(!e.persisted&&!location.hash&&!back)top()});
  }catch(e){}
})();
