const menu=document.querySelector('.menu'),mobile=document.querySelector('.mobile'),mods=document.querySelector('.modules'),mbtn=document.querySelector('.modules-btn'),mtoggle=document.querySelector('.mobile-toggle');
menu?.addEventListener('click',()=>{mobile.classList.toggle('open');menu.setAttribute('aria-expanded',String(mobile.classList.contains('open')))});
mbtn?.addEventListener('click',e=>{e.preventDefault();mods.classList.toggle('open')});
document.addEventListener('click',e=>{if(mods&&!mods.contains(e.target))mods.classList.remove('open')});
mtoggle?.addEventListener('click',()=>mtoggle.parentElement.classList.toggle('open'));
const data={
cad:['Central de Despacho (CAD)','Mapa operacional, triagem, prioridades, despacho de equipes e rastreabilidade completa do atendimento.'],
muralha:['Muralha Inteligente','Passagens LPR/OCR, fatos, regras de alerta, pesquisas, correlações e apoio a abordagens.'],
video:['Vídeo / VMS','Playback, evidências, análise histórica e visão computacional aplicada à operação e investigação.'],
ged:['GED com IA','Acervo digital, documentos, contratos, busca estruturada e apoio analítico.'],
frotas:['Frotas e telemetria','Rastreamento, cercas eletrônicas, histórico, alertas e dados de operação em tempo real.'],
bi:['BI operacional','Dashboards, KPIs, mapas e leitura executiva consolidada da operação urbana.']
};
document.querySelectorAll('.feature').forEach(b=>b.addEventListener('click',()=>{document.querySelectorAll('.feature').forEach(x=>x.classList.remove('active'));b.classList.add('active');const d=data[b.dataset.feature];const t=document.querySelector('[data-ft]'),p=document.querySelector('[data-fp]');if(t&&p&&d){t.textContent=d[0];p.textContent=d[1]}}));

/* Fotos reais publicadas junto com o GitHub Pages; sem chamadas externas no navegador. */
const heroImg=document.querySelector('.hero-media img');
if(heroImg) heroImg.src='assets/hero-real.jpg';
const heroVideo=document.querySelector('.hero-media video');
if(heroVideo) heroVideo.remove();

/* CCO embutido como data URI para eliminar cache/arquivo truncado. */
const ccoPhoto="data:image/jpeg;base64,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...trimmed...";
const homeAssets=[
  ccoPhoto,
  'assets/educacao-real.jpg',
  'assets/transporte-real.jpg',
  'assets/saude-real.jpg',
  'assets/defesa-civil-real.jpg'
];
document.querySelectorAll('#modulos .modules-grid .card .media').forEach((el,i)=>{
  if(homeAssets[i]) el.style.setProperty('background-image',`url("${homeAssets[i]}")`,'important');
});

const pageAssets={
  'cco-seguranca.html':ccoPhoto,
  'educacao-escolas.html':'../assets/educacao-real.jpg',
  'transporte-publico.html':'../assets/transporte-real.jpg',
  'saude-digital.html':'../assets/saude-real.jpg',
  'telegestao-defesa-civil.html':'../assets/defesa-civil-real.jpg'
};
const pageName=location.pathname.split('/').pop();
const pagePhoto=document.querySelector('.page-photo');
if(pagePhoto&&pageAssets[pageName]){
  pagePhoto.style.setProperty('background-image',`url("${pageAssets[pageName]}")`,'important');
}
