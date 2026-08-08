from bs4 import BeautifulSoup
from pathlib import Path
R=Path(__file__).resolve().parents[1]

def dl(): return '<svg viewBox="0 0 24 24" aria-hidden="true"><path d="M12 3v11m0 0 4-4m-4 4-4-4M5 17v3h14v-3"/></svg>'

# HOME
p=R/'index.html'; s=BeautifulSoup(p.read_text(encoding='utf-8'),'html.parser')
if not s.find(id='scroll-progress'):
    x=s.new_tag('div',id='scroll-progress'); x['aria-hidden']='true'; s.body.insert(0,x)
for nav in s.select('nav.nav'):
    if not any(a.get_text(strip=True)=='Documentos' for a in nav.find_all('a',recursive=False)):
        a=s.new_tag('a',href='index.html#documentos'); a.string='Documentos'; nav.append(a)
for panel in s.select('.mobile-panel'):
    if not any(a.get_text(strip=True)=='Documentos' for a in panel.find_all('a',recursive=False)):
        a=s.new_tag('a',href='index.html#documentos'); a.string='Documentos'; panel.append(a)
media=s.select_one('.hero-media')
if media and not media.find('video'):
    v=s.new_tag('video',id='hero-loop'); v['muted']='';v['loop']='';v['playsinline']='';v['preload']='none';v['poster']='assets/hero-real.jpg';v['data-src']='assets/hero-loop.mp4';v['aria-hidden']='true';media.append(v)
ha=s.select_one('.hero-actions')
if ha:
    ha.clear(); ha.append(BeautifulSoup('<a class="link-primary" href="#modulos">Explorar os módulos →</a>','html.parser').a);ha.append(BeautifulSoup('<a class="link-secondary" href="URBAN-BRAIN-Apresentacao-Executiva.pdf" download>'+dl()+'<span>Apresentação Executiva</span></a>','html.parser').a)
hp=s.select_one('.hero-pills')
if hp and not s.select_one('.video-control'):
    b=s.new_tag('button',attrs={'class':'video-control','type':'button','aria-controls':'hero-loop'});b.string='Pausar vídeo';hp.insert_after(b)
for el,(v,l) in zip(s.select('.hero-board .metric'),[('+40 mil','capacidade de câmeras'),('>99,5%','referência antifraude'),('5','verticais integradas'),('Offline-first','continuidade em campo')]):
    el.clear();a=s.new_tag('strong');a.string=v;b=s.new_tag('span');b.string=l;el.extend([a,b])
if not s.find(id='arquitetura'):
    eco=s.find('section',id='ecossistema')
    h='''<section class="section architecture-section" id="arquitetura"><div class="container"><div class="section-head"><span class="eyebrow">Arquitetura operacional</span><h2>Do evento ao indicador, sem trocar de contexto.</h2><p>Uma jornada operacional clara, com integração aberta, visão geográfica e rastreabilidade ponta a ponta.</p></div><div class="command-flow"><article><span>01</span><strong>Detecta</strong><p>IA, vídeo, LPR e sensores.</p></article><article><span>02</span><strong>Contextualiza</strong><p>GIS, histórico e criticidade.</p></article><article><span>03</span><strong>Coordena</strong><p>CAD, protocolos e recursos.</p></article><article><span>04</span><strong>Executa</strong><p>Equipes, mobile e evidências.</p></article><article><span>05</span><strong>Audita</strong><p>BI, KPIs e rastreabilidade.</p></article></div><div class="architecture-stack"><div><strong>Operação</strong><span>CAD · VMS · Muralha · GIS</span></div><div><strong>Integração</strong><span>APIs · OAuth2 · SDKs</span></div><div><strong>IoT & Campo</strong><span>MQTT · Telemetria · Mobile</span></div><div><strong>Governança</strong><span>RBAC · Multi-tenant · Auditoria</span></div></div></div></section>'''
    eco.insert_after(BeautifulSoup(h,'html.parser').section)
for i,c in enumerate(s.select('#modulos .card')):
    m=c.select_one('.media'); img=m.find('img') if m else None
    if m and not m.select_one('.media-badge'):
        z=s.new_tag('span',attrs={'class':'media-badge'});z.string=['Monitoramento + IA','Presença facial','Mobilidade conectada','Telemedicina + IoT','IoT + prevenção'][i];m.append(z)
    if i==2 and img: img['src']='assets/transporte-v2.jpg';img['alt']='Passageiros em ônibus urbano representando mobilidade conectada.'
if not s.find(id='cenarios'):
    it=s.find('section',id='inteligencia')
    h='''<section class="section scenarios-section" id="cenarios"><div class="container"><div class="section-head"><span class="eyebrow">Cenários integrados</span><h2>Mais valor quando os módulos trabalham juntos.</h2><p>A plataforma conecta eventos, contexto, decisão e resposta operacional.</p></div><div class="scenario-grid"><article><span>Segurança</span><h3>Alerta → contexto → despacho → evidência</h3><p>LPR e vídeo alimentam mapa, triagem, despacho e investigação.</p></article><article><span>Educação</span><h3>Presença → comunicação → permanência</h3><p>A entrada facial atualiza frequência, indicadores e comunicação.</p></article><article><span>Defesa Civil</span><h3>Sensor → risco → alerta → resposta</h3><p>Pluviometria e GIS apoiam alertas, sirenes e equipes de campo.</p></article></div></div></section>'''
    it.insert_after(BeautifulSoup(h,'html.parser').section)
if not s.find(id='documentos'):
    last=s.select('main > section.section')[-1]
    h='''<section class="section documents-section" id="documentos"><div class="container"><div class="section-head"><span class="eyebrow">Documentos técnicos</span><h2>Material executivo e datasheets prontos para reunião.</h2><p>Visão executiva para o gestor e profundidade técnica para avaliação do projeto.</p></div><div class="documents-layout"><article class="executive-document"><div><span class="doc-label">APRESENTAÇÃO EXECUTIVA</span><h3>URBAN BRAIN — O Cérebro Digital da Cidade</h3><p>Plataforma, módulos, arquitetura, cenários de uso e jornada de implantação.</p></div><a class="document-primary" href="URBAN-BRAIN-Apresentacao-Executiva.pdf" download>Baixar apresentação ↘</a></article><div class="datasheet-list"><a href="datasheets/cco-seguranca.pdf" download>CCO e Segurança <span>PDF ↘</span></a><a href="datasheets/educacao-escolas.pdf" download>Educação e Escolas <span>PDF ↘</span></a><a href="datasheets/transporte-publico.pdf" download>Transporte Público <span>PDF ↘</span></a><a href="datasheets/saude-digital.pdf" download>Saúde Digital <span>PDF ↘</span></a><a href="datasheets/telegestao-defesa-civil.pdf" download>Telegestão e Defesa Civil <span>PDF ↘</span></a></div></div></div></section>'''
    last.insert_before(BeautifulSoup(h,'html.parser').section)
p.write_text(str(s),encoding='utf-8')

# TRANSPORTE: imagem mais aderente + PDF executivo
p=R/'modulos/transporte-publico.html'; s=BeautifulSoup(p.read_text(encoding='utf-8'),'html.parser')
img=s.select_one('.page-photo img')
if img: img['src']='../assets/transporte-v2.jpg';img['alt']='Passageiros em ônibus urbano em São Paulo, representando mobilidade conectada.'
pa=s.select_one('.page-actions')
if pa and not pa.select_one('.page-executive-link'): pa.append(BeautifulSoup('<a class="page-executive-link" href="../URBAN-BRAIN-Apresentacao-Executiva.pdf" download>Apresentação Executiva ↘</a>','html.parser').a)
p.write_text(str(s),encoding='utf-8')

CSS=r'''
/* ===== Corporate evolution 2026.08 ===== */
#scroll-progress{position:fixed;left:0;top:0;width:0;height:2px;z-index:9999;background:linear-gradient(90deg,#0785ff,#12d1ec)}
.hero-media video{position:absolute;inset:0;z-index:1;width:100%;height:100%;object-fit:cover;opacity:0;transition:opacity .8s;filter:saturate(.86) contrast(1.08) brightness(.64)}.hero.video-on .hero-media video{opacity:1}.hero.video-on .hero-media img{opacity:.14}.hero-actions{display:flex;gap:10px;flex-wrap:wrap}.link-secondary,.page-executive-link{display:inline-flex;align-items:center;gap:8px;padding:13px 15px;border:1px solid #31526e;border-radius:6px;background:#071522b8;color:#d7e9f7;font-size:12px;font-weight:800}.link-secondary svg{width:17px;height:17px;fill:none;stroke:currentColor;stroke-width:1.8}.video-control{margin-top:14px;border:0;background:none;color:#86a2b8;font-size:10px;font-weight:900;text-transform:uppercase;cursor:pointer}.video-control:before{content:"●";margin-right:7px;color:#2ad59a}
#modulos .modules-grid{grid-template-columns:repeat(6,1fr)}#modulos .card{grid-column:span 2}#modulos .card:nth-child(4),#modulos .card:nth-child(5){grid-column:span 3}.media-badge{position:absolute;left:14px;top:14px;z-index:3;padding:7px 9px;border:1px solid #70d1ff77;border-radius:5px;background:#071522d9;color:#bdeaff;font-size:9px;font-weight:900;text-transform:uppercase;letter-spacing:.08em}
.architecture-section{background:#fff}.command-flow{display:grid;grid-template-columns:repeat(5,1fr);gap:10px}.command-flow article{padding:22px 18px;border:1px solid #d8e5ef;border-radius:10px;background:#fff;box-shadow:0 18px 42px #07223d12}.command-flow article>span{display:grid;place-items:center;width:38px;height:38px;margin-bottom:16px;border-radius:7px;background:#07111e;color:#65ccff;font-size:10px;font-weight:900}.command-flow strong{font-size:16px}.command-flow p{margin:7px 0 0;color:#64788f;font-size:11px}.architecture-stack{display:grid;grid-template-columns:repeat(4,1fr);gap:10px;margin-top:16px}.architecture-stack div{padding:17px;border-left:3px solid #0a9eff;background:#eef5fa}.architecture-stack strong,.architecture-stack span{display:block}.architecture-stack span{margin-top:4px;color:#64788f;font-size:10px}
.scenarios-section{background:#eef3f7}.scenario-grid{display:grid;grid-template-columns:repeat(3,1fr);gap:16px}.scenario-grid article{padding:25px;border:1px solid #d5e2ec;border-radius:11px;background:#fff;box-shadow:0 20px 50px #092a4612}.scenario-grid article>span{color:#0785dc;font-size:9px;font-weight:900;text-transform:uppercase;letter-spacing:.14em}.scenario-grid h3{margin:12px 0 8px;font-size:21px;line-height:1.08}.scenario-grid p{margin:0;color:#64788f;font-size:12px}
.documents-section{background:#07111e;color:#fff}.documents-section .section-head p{color:#91a8bd}.documents-section .eyebrow{color:#4fc5ff}.documents-layout{display:grid;grid-template-columns:1.2fr .8fr;gap:18px}.executive-document{display:grid;grid-template-columns:1fr auto;gap:24px;align-items:center;padding:32px;border:1px solid #1f435f;border-radius:13px;background:linear-gradient(135deg,#0a1a2b,#0c2740)}.doc-label{color:#55caff;font-size:9px;font-weight:900}.executive-document h3{margin:9px 0 7px;font-size:28px}.executive-document p{margin:0;color:#98aec0}.document-primary{padding:13px 15px;border-radius:7px;background:linear-gradient(135deg,#0785ff,#0ab6e9);font-size:11px;font-weight:900}.datasheet-list{display:grid;gap:7px}.datasheet-list a{display:flex;justify-content:space-between;padding:15px;border:1px solid #1d3b55;border-radius:7px;background:#091827;font-size:11px;font-weight:800}.datasheet-list span{color:#58bfff;font-size:9px}
@media(max-width:1080px){#modulos .modules-grid{grid-template-columns:1fr 1fr}#modulos .card,#modulos .card:nth-child(4),#modulos .card:nth-child(5){grid-column:auto}.command-flow{grid-template-columns:1fr 1fr}.architecture-stack{grid-template-columns:1fr 1fr}.documents-layout{grid-template-columns:1fr}}
@media(max-width:760px){.command-flow,.architecture-stack,.scenario-grid{grid-template-columns:1fr}.executive-document{grid-template-columns:1fr}.hero-actions{align-items:stretch}.link-primary,.link-secondary{justify-content:center}}
@media(prefers-reduced-motion:reduce){.hero-media video,.video-control{display:none!important}}
'''
JS=r'''
// Corporate experience enhancements
(()=>{const p=document.getElementById('scroll-progress');const up=()=>{if(p){const d=document.documentElement,m=Math.max(1,d.scrollHeight-d.clientHeight);p.style.width=Math.min(100,d.scrollTop/m*100)+'%'}};up();addEventListener('scroll',up,{passive:true});addEventListener('resize',up,{passive:true});const v=document.getElementById('hero-loop'),h=document.querySelector('.hero'),b=document.querySelector('.video-control'),reduce=matchMedia?.('(prefers-reduced-motion: reduce)').matches,save=navigator.connection?.saveData;if(v&&!reduce&&!save){v.src=v.dataset.src;v.addEventListener('canplay',()=>v.play().then(()=>h?.classList.add('video-on')).catch(()=>{}),{once:true});v.load();b?.addEventListener('click',()=>{if(v.paused){v.play();b.textContent='Pausar vídeo'}else{v.pause();b.textContent='Retomar vídeo'}})}else if(b)b.hidden=true})();
'''
sp=R/'assets/styles.css'; t=sp.read_text(encoding='utf-8');
if 'Corporate evolution 2026.08' not in t: sp.write_text(t+'\n'+CSS,encoding='utf-8')
jp=R/'assets/script.js'; t=jp.read_text(encoding='utf-8');
if 'Corporate experience enhancements' not in t: jp.write_text(t+'\n'+JS,encoding='utf-8')
print('site upgraded')
