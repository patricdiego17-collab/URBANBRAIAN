from pathlib import Path

index = Path('index.html')
s = index.read_text(encoding='utf-8')
s = s.replace('assets/ecossistema-urban-brain.jpg', 'assets/ecossistema-urban-brain.svg')
s = s.replace('assets/gis-operacional-urban-brain.jpg', 'assets/gis-operacional-urban-brain.svg')
s = s.replace('Apresentação Executiva <span>↘</span>', 'Catálogo Técnico <span>↘</span>')
s = s.replace('Material estruturado para reuniões, avaliação técnica, especificação e processos de contratação.', 'Catálogo ampliado com visão de ecossistema, módulos estratégicos, integrações, fluxos e parâmetros consolidados para avaliação técnica e comercial.')
s = s.replace('<span class="doc-label">APRESENTAÇÃO EXECUTIVA</span><h3>URBAN BRAIN — Plataforma de Inteligência Urbana</h3><p>Visão da plataforma, arquitetura, módulos estratégicos, portfólio consolidado e critérios de implantação.</p><a class="document-primary" href="URBAN-BRAIN-Apresentacao-Executiva.pdf" download>Baixar apresentação <span>↘</span></a>', '<span class="doc-label">CATÁLOGO TÉCNICO</span><h3>URBAN BRAIN — Catálogo técnico-comercial completo</h3><p>Documento ampliado com arquitetura do ecossistema, visão por módulo, integrações, fluxo operacional, aplicações e especificações consolidadas.</p><ul class="doc-bullets"><li>Visão do ecossistema e camadas transversais</li><li>Módulos estratégicos com detalhamento funcional</li><li>Integrações, governança e diretrizes de implantação</li></ul><a class="document-primary" href="URBAN-BRAIN-Apresentacao-Executiva.pdf" download>Baixar catálogo completo <span>↘</span></a>')
index.write_text(s, encoding='utf-8')

cssp = Path('assets/styles.css')
css = cssp.read_text(encoding='utf-8')
if '.doc-bullets{' not in css:
    css += '\n.doc-bullets{margin:14px 0 0;padding-left:18px;color:#d8e7f2;font-size:12px}.doc-bullets li+li{margin-top:5px}\n'
cssp.write_text(css, encoding='utf-8')

for p in Path('modulos').glob('*.html'):
    t = p.read_text(encoding='utf-8')
    t = t.replace('Baixar Datasheet (PDF)', 'Baixar Datasheet Técnico (PDF)')
    p.write_text(t, encoding='utf-8')

print('V4 patch applied')