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

/* Todas as mídias principais são locais para evitar dependência de rede no preview */
const homeAssets=[
  'assets/cco-monitoramento-urbano.jpg',
  'assets/educacao-presenca-facial.svg',
  'assets/transporte-publico.svg',
  'assets/saude-digital.svg',
  'assets/defesa-civil.svg'
];
document.querySelectorAll('#modulos .modules-grid .card .media').forEach((el,i)=>{
  if(homeAssets[i]) el.style.setProperty('background-image',`url('${homeAssets[i]}')`,'important');
});

const pageAssets={
  'cco-seguranca.html':'../assets/cco-monitoramento-urbano.jpg',
  'educacao-escolas.html':'../assets/educacao-presenca-facial.svg',
  'transporte-publico.html':'../assets/transporte-publico.svg',
  'saude-digital.html':'../assets/saude-digital.svg',
  'telegestao-defesa-civil.html':'../assets/defesa-civil.svg'
};
const pageName=location.pathname.split('/').pop();
const pagePhoto=document.querySelector('.page-photo');
if(pagePhoto&&pageAssets[pageName]){
  pagePhoto.style.setProperty('background-image',`url('${pageAssets[pageName]}')`,'important');
}
