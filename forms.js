/* Sends the contact and report forms to Formspree. A confirmation screen shows only after Formspree accepts the message. */
(function(){
  var EMAIL='preferredwebsolutions@gmail.com';
  document.querySelectorAll('form[data-formspree]').forEach(function(form){
    var status=form.querySelector('.status'),btn=form.querySelector('button[type=submit]');
    var done=document.getElementById(form.getAttribute('data-done'));
    form.addEventListener('submit',function(e){
      e.preventDefault();
      if(!form.checkValidity()){form.reportValidity();return}
      var label=btn.textContent;btn.disabled=true;btn.textContent='Sending…';
      status.className='status';status.textContent='';
      var data={};new FormData(form).forEach(function(v,k){data[k]=v});
      fetch(form.getAttribute('data-formspree'),{method:'POST',headers:{'Content-Type':'application/json','Accept':'application/json'},body:JSON.stringify(data)})
        .then(function(r){
          if(!r.ok)throw new Error('bad');
          form.hidden=true;
          if(done){done.hidden=false;var h=done.querySelector('h3');if(h){h.setAttribute('tabindex','-1');h.focus()}}
        })
        .catch(function(){
          btn.disabled=false;btn.textContent=label;
          status.className='status err';
          status.textContent='That did not send. Please email '+EMAIL+' and we will get back to you.';
        });
    });
  });
  document.querySelectorAll('[data-copy]').forEach(function(b){
    b.addEventListener('click',function(){
      var t=b.getAttribute('data-copy'),old=b.textContent;
      function ok(){b.textContent='Copied';setTimeout(function(){b.textContent=old},1800)}
      try{navigator.clipboard.writeText(t).then(ok,function(){b.textContent='Select the address to copy'})}catch(e){b.textContent='Select the address to copy'}
    });
  });
  var sw=document.querySelectorAll('.switch [role=tab]');
  sw.forEach(function(tab){
    tab.addEventListener('click',function(){select(tab)});
    tab.addEventListener('keydown',function(e){
      var i=Array.prototype.indexOf.call(sw,tab),n=null;
      if(e.key==='ArrowRight')n=sw[(i+1)%sw.length];
      if(e.key==='ArrowLeft')n=sw[(i-1+sw.length)%sw.length];
      if(n){e.preventDefault();select(n);n.focus()}
    });
  });
  function select(tab){
    sw.forEach(function(t){
      var on=t===tab;t.setAttribute('aria-selected',on);t.tabIndex=on?0:-1;
      var p=document.getElementById(t.getAttribute('aria-controls'));if(p)p.hidden=!on;
    });
  }
})();
