const menu=document.querySelector('.menu'),mobile=document.querySelector('.mobile'),mods=document.querySelector('.modules'),mbtn=document.querySelector('.modules-btn'),mtoggle=document.querySelector('.mobile-toggle');
menu?.addEventListener('click',()=>{mobile.classList.toggle('open');menu.setAttribute('aria-expanded',String(mobile.classList.contains('open')))});
mbtn?.addEventListener('click',e=>{e.preventDefault();mods.classList.toggle('open')});
document.addEventListener('click',e=>{if(mods&&!mods.contains(e.target))mods.classList.remove('open')});
mtoggle?.addEventListener('click',()=>mtoggle.parentElement.classList.toggle('open'));
document.querySelector('.hero-note')?.remove();
const data={
cad:['Central de Despacho (CAD)','Mapa operacional, triagem, prioridades, despacho de equipes e rastreabilidade completa do atendimento.'],
muralha:['Muralha Inteligente','Passagens LPR/OCR, fatos, regras de alerta, pesquisas, correlações e apoio a abordagens.'],
video:['Vídeo / VMS','Playback, evidências, análise histórica e visão computacional aplicada à operação e investigação.'],
ged:['GED com IA','Acervo digital, documentos, contratos, busca estruturada e apoio analítico.'],
frotas:['Frotas e telemetria','Rastreamento, cercas eletrônicas, histórico, alertas e dados de operação em tempo real.'],
bi:['BI operacional','Dashboards, KPIs, mapas e leitura executiva consolidada da operação urbana.']
};
document.querySelectorAll('.feature').forEach(b=>b.addEventListener('click',()=>{document.querySelectorAll('.feature').forEach(x=>x.classList.remove('active'));b.classList.add('active');const d=data[b.dataset.feature];document.querySelector('[data-ft]').textContent=d[0];document.querySelector('[data-fp]').textContent=d[1]}));
const v=document.querySelector('.hero-media video');if(v){v.addEventListener('canplay',()=>document.body.classList.add('video-ready'));v.addEventListener('error',()=>v.remove())}