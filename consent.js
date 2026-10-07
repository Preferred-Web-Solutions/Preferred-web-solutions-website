/* PWS consent banner. This site sets no cookies and loads no analytics or marketing scripts.
   The only thing stored is the visitor's own choice, in localStorage under "pws-consent". */
(function(){
  var KEY='pws-consent',VERSION='1.0';
  function read(){try{var v=JSON.parse(localStorage.getItem(KEY)||'null');return v&&v.v===VERSION?v:null}catch(e){return null}}
  function save(a,m){try{localStorage.setItem(KEY,JSON.stringify({v:VERSION,ts:new Date().toISOString(),analytics:!!a,marketing:!!m}))}catch(e){}}
  var root=document.createElement('div');
  root.className='consent';root.hidden=true;
  root.innerHTML=
    '<div class="consent-card" role="dialog" aria-labelledby="consent-title" aria-describedby="consent-text">'+
      '<h2 id="consent-title" tabindex="-1">Your privacy choices</h2>'+
      '<p id="consent-text">This site stores one small item on your device to remember this choice. It does not use analytics or marketing cookies today. If that changes, we will ask first. <a href="cookies.html">Cookie policy</a></p>'+
      '<div class="consent-prefs" id="consent-prefs" hidden>'+
        '<label class="pref"><input type="checkbox" checked disabled><span><b>Essential</b>Remembers your choice on this banner. Always on.</span></label>'+
        '<label class="pref"><input type="checkbox" id="c-an"><span><b>Analytics</b>Not used on this site right now.</span></label>'+
        '<label class="pref"><input type="checkbox" id="c-mk"><span><b>Marketing</b>Not used on this site right now.</span></label>'+
      '</div>'+
      '<div class="consent-btns">'+
        '<button type="button" class="btn primary small" id="c-all">Accept all</button>'+
        '<button type="button" class="btn small" id="c-rej">Reject non-essential</button>'+
        '<button type="button" class="btn small" id="c-man" aria-expanded="false" aria-controls="consent-prefs">Manage choices</button>'+
      '</div>'+
    '</div>';
  var opener=null;
  function show(focus){
    var s=read();
    root.querySelector('#c-an').checked=!!(s&&s.analytics);
    root.querySelector('#c-mk').checked=!!(s&&s.marketing);
    root.hidden=false;
    if(focus)root.querySelector('#consent-title').focus();
  }
  function hide(){root.hidden=true;if(opener){try{opener.focus()}catch(e){}opener=null}}
  function init(){
    document.body.appendChild(root);
    var all=root.querySelector('#c-all'),rej=root.querySelector('#c-rej'),man=root.querySelector('#c-man'),prefs=root.querySelector('#consent-prefs');
    all.addEventListener('click',function(){save(true,true);hide()});
    rej.addEventListener('click',function(){save(false,false);hide()});
    man.addEventListener('click',function(){
      if(prefs.hidden){prefs.hidden=false;man.setAttribute('aria-expanded','true');man.textContent='Save choices'}
      else{save(root.querySelector('#c-an').checked,root.querySelector('#c-mk').checked);hide();prefs.hidden=true;man.setAttribute('aria-expanded','false');man.textContent='Manage choices'}
    });
    root.addEventListener('keydown',function(e){if(e.key==='Escape'&&read())hide()});
    document.querySelectorAll('[data-cookie-settings]').forEach(function(b){
      b.addEventListener('click',function(){opener=b;show(true)});
    });
    if(!read())show(false);
  }
  if(document.readyState==='loading')document.addEventListener('DOMContentLoaded',init);else init();
})();
