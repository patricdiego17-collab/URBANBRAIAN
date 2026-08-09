from pathlib import Path
from reportlab.lib.pagesizes import A4, landscape
from reportlab.lib import colors
from reportlab.lib.styles import getSampleStyleSheet, ParagraphStyle
from reportlab.lib.units import mm
from reportlab.platypus import SimpleDocTemplate, Paragraph, Spacer, Table, TableStyle, Image, PageBreak

ROOT=Path('.')
AS=ROOT/'assets'
OUT=ROOT/'URBAN-BRAIN-Apresentacao-Executiva.pdf'
NAVY=colors.HexColor('#071521'); BLUE=colors.HexColor('#087FF5'); CYAN=colors.HexColor('#14CDE7'); TEXT=colors.HexColor('#203747'); MUTED=colors.HexColor('#667B8E'); LINE=colors.HexColor('#D9E3EC'); PALE=colors.HexColor('#EEF7FC')
styles=getSampleStyleSheet()
styles.add(ParagraphStyle(name='K',fontName='Helvetica-Bold',fontSize=8.5,leading=10,textColor=BLUE,spaceAfter=5))
styles.add(ParagraphStyle(name='T',fontName='Helvetica-Bold',fontSize=27,leading=30,textColor=NAVY,spaceAfter=8))
styles.add(ParagraphStyle(name='H',fontName='Helvetica-Bold',fontSize=18,leading=21,textColor=NAVY,spaceAfter=6))
styles.add(ParagraphStyle(name='B',fontName='Helvetica',fontSize=9.4,leading=13,textColor=TEXT,spaceAfter=5))
styles.add(ParagraphStyle(name='S',fontName='Helvetica',fontSize=8,leading=10.5,textColor=MUTED,spaceAfter=3))
styles.add(ParagraphStyle(name='L',fontName='Helvetica',fontSize=8.8,leading=12,textColor=TEXT,leftIndent=9,bulletIndent=0,spaceAfter=2))
styles.add(ParagraphStyle(name='Cell',fontName='Helvetica',fontSize=8.1,leading=10.5,textColor=TEXT))
styles.add(ParagraphStyle(name='CellB',fontName='Helvetica-Bold',fontSize=8.1,leading=10.5,textColor=NAVY))

scope='Recursos, quantidades, retenção, integrações, hardware, licenciamento, disponibilidade móvel e forma de implantação devem ser confirmados no projeto e na contratação.'
modules=[
('01','CCO e Segurança','Uma visão operacional comum para vídeo, mapas, ocorrências, alarmes, evidências e resposta.','cco-final.jpg',
 'Camada integradora para centros de comando e controle, reunindo VMS, visão computacional, LPR/OCR, CAD, GIS, GED, BI, alarmes, fluxos operacionais e mobilidade.',
 ['Integração de VMS, câmeras, analíticos, LPR/OCR, reconhecimento facial e eventos externos.','Mapa urbano com ocorrências, viaturas, câmeras, alertas e entidades georreferenciadas.','CAD para atendimento, prioridade, despacho e acompanhamento de recursos.','Gestão de alarmes e eventos com procedimentos operacionais configuráveis.','Playback, evidências, documentos e histórico associados ao contexto da ocorrência.','Dashboards, indicadores, relatórios, perfis e trilha de auditoria.'],
 [('Camadas','VMS, LPR/OCR, CAD, GIS, GED, BI e analíticos.'),('Operação','Web, desktop e mobilidade conforme o módulo implantado.'),('Segurança','Perfis, permissões granulares e trilha de auditoria.'),('Arquitetura','Modular, integrável e expansível por etapas.'),('Escala','Dimensionada conforme câmeras, retenção, analíticos, usuários e integrações.'),('Aplicações','COI/CCO municipal, segurança pública, infraestrutura crítica e operações multisite.')]),
('02','Educação e Escolas','Proteção escolar, frequência automatizada, conexão familiar e resposta integrada.','educacao-final-v3.jpg',
 'Ecossistema para controle de acesso, presença facial, alertas, comunicação com responsáveis, proteção perimetral e integração da escola com o centro de operações.',
 ['Controle de acesso com catracas ou fluxo aberto, conforme o desenho da unidade.','Identificação facial de alunos, responsáveis e pessoas previamente cadastradas.','Validação do vínculo entre aluno e responsável autorizado.','Registro de entrada, saída e presença com trilha temporal.','Alertas de ausência, evasão e tentativas não autorizadas.','Comunicação com responsáveis, proteção perimetral, GIS e relatórios por unidade.'],
 [('Acesso','Catracas, fluxo aberto e validações conforme a unidade.'),('Identificação','Reconhecimento facial e credenciais previstas no projeto.'),('Registros','Presença, entradas, saídas, alertas e histórico consultável.'),('Operação','Interface web e integração com central de operações.'),('Comunicação','Notificações e comunicação com responsáveis conforme configuração.'),('Aplicações','Escolas municipais, creches, campus e redes educacionais.')]),
('03','Mobilidade e Transporte','Alunos, motoristas, veículos, rotas e eventos monitorados do embarque ao desembarque.','transporte-v2.jpg',
 'Gestão de transporte escolar com câmeras, RFID de alunos, ADAS/DMS, GPS, telemetria, rotas, alertas e relatórios por veículo, aluno e período.',
 ['Câmeras internas, laterais e frontal conforme arquitetura embarcada.','RFID para registro de embarque e desembarque dos alunos.','GPS, rotas, cercas geográficas e histórico de trajetos.','Telemetria operacional e eventos de condução.','Recursos ADAS/DMS conforme equipamento integrado.','Alertas e relatórios por veículo, aluno, condutor, rota e período.'],
 [('Veículo','Câmeras, GPS e recursos integráveis de telemetria.'),('Aluno','Identificação RFID e correlação com veículo, rota e período.'),('Condução','ADAS/DMS conforme equipamento e escopo.'),('Mapa','Rotas, paradas, histórico, geofences e rastreamento.'),('Relatórios','Indicadores por veículo, aluno, condutor, rota e exceções.'),('Aplicações','Transporte escolar, transporte de pessoal e frotas monitoradas.')]),
('04','Saúde Digital','Telemedicina, prontuário, atenção primária, diagnóstico remoto e inteligência de dados.','saude-real.jpg',
 'Ecossistema com prontuário eletrônico, teleconsulta, teleinterconsulta, telediagnóstico, UBS digital, vigilância epidemiológica, biomonitores e gestão em tempo real.',
 ['Prontuário eletrônico integrado ao histórico do paciente.','Integração informada com e-SUS AB e RNDS, conforme escopo.','Agendamento online, vagas, encaixes, filas e painéis de chamada.','Teleconsulta, teleinterconsulta e telediagnóstico.','UBS digital, consultórios virtuais e biomonitores quando previstos.','Vigilância epidemiológica, mapas, painéis e relatórios gerenciais.'],
 [('Prontuário','Histórico clínico, registros assistenciais e agenda.'),('Integrações','e-SUS AB, RNDS e demais integrações conforme projeto.'),('Telemedicina','Teleconsulta, teleinterconsulta e telediagnóstico.'),('Monitoramento','Biomonitores e recursos IoT conforme implantação.'),('Gestão','Painéis, filas, vagas, relatórios e indicadores da rede.'),('Aplicações','APS, UBS, clínicas, redes municipais e redes privadas.')]),
('05','Telegestão e Defesa Civil','Iluminação, risco, sensores, sirenes, território e resposta coordenada em um mesmo mapa.','defesa-civil-real.jpg',
 'Iluminação pública conectada a sensores, áreas de risco, sirenes, estações meteorológicas, vistorias e resposta coordenada em mapa.',
 ['Cadastro de gateways, controladores, grupos e vínculos georreferenciados.','Comandos de ligar, desligar, dimerizar, consultar e reconectar.','Agendamentos com horários, vigência e aplicação individual ou por grupo.','Áreas de risco por polígonos, moradias e composição familiar.','Sensores, estações meteorológicas, sirenes e protocolos de acionamento.','Vistorias, ordens de serviço, despacho, histórico e relatórios operacionais.'],
 [('Iluminação','Gateways, controladores, grupos, telemetria e comandos remotos.'),('Território','Áreas de risco, moradias, sensores e estações em GIS.'),('Resposta','Ordens, vistorias, sirenes e integração com despacho.'),('Agendamentos','Programação por unidade ou grupo com vigência definida.'),('Relatórios','Histórico, exceções, inspeções e indicadores gerenciais.'),('Aplicações','Iluminação pública, defesa civil e prevenção climática.')])]

portfolio=[
('Plataforma & Gestão Urbana','Gestão Urbana Inteligente; Operações e Serviços de Campo; BI e Assistente de IA; GED com IA; Telegestão de Iluminação; Defesa Civil e Inteligência Climática; Frotas e Telemetria'),
('Segurança & Centros de Operações','CCO e Interoperabilidade; Atendimento e Despacho; Canal Cidadão 153; VMS e Videomonitoramento; Inteligência Facial; Muralha LPR/OCR; Escolas Seguras; Guardas Municipais'),
('Mobilidade & Operações Especializadas','Gestão de Transporte Escolar; Gestão de Frotas de Concreteiras'),
('Saúde Digital','Saúde Digital Integrada'),
('Segurança Eletrônica & Infraestrutura','Controle de Acesso; Segurança Perimetral; BMS e Automação Predial; Cabeamento e Redes; Detecção e Combate a Incêndio; Manutenção Preventiva e Corretiva')]

def footer(c,doc):
 w,h=doc.pagesize;c.saveState();c.setStrokeColor(LINE);c.line(16*mm,12*mm,w-16*mm,12*mm);c.setFont('Helvetica',7.5);c.setFillColor(MUTED);c.drawString(16*mm,7*mm,'URBAN BRAIN | Catálogo técnico-comercial');c.drawRightString(w-16*mm,7*mm,f'{c.getPageNumber():02d}');c.restoreState()

def bullets(items): return [Paragraph(x,styles['L'],bulletText='•') for x in items]
def table(rows,a=46*mm,b=195*mm):
 data=[[Paragraph(f'<b>{x}</b>',styles['CellB']),Paragraph(y,styles['Cell'])] for x,y in rows];t=Table(data,colWidths=[a,b]);t.setStyle(TableStyle([('BOX',(0,0),(-1,-1),.5,LINE),('INNERGRID',(0,0),(-1,-1),.3,LINE),('BACKGROUND',(0,0),(0,-1),PALE),('VALIGN',(0,0),(-1,-1),'TOP'),('LEFTPADDING',(0,0),(-1,-1),7),('RIGHTPADDING',(0,0),(-1,-1),7),('TOPPADDING',(0,0),(-1,-1),6),('BOTTOMPADDING',(0,0),(-1,-1),6)]));return t

doc=SimpleDocTemplate(str(OUT),pagesize=landscape(A4),leftMargin=16*mm,rightMargin=16*mm,topMargin=14*mm,bottomMargin=18*mm)
st=[]
logo=Image(str(AS/'urban-brain-wordmark.jpg'),width=58*mm,height=25*mm)
st += [Spacer(1,5*mm),logo,Spacer(1,6*mm),Paragraph('CATÁLOGO TÉCNICO-COMERCIAL',styles['K']),Paragraph('URBAN BRAIN — Inteligência urbana integrada para operação, território e serviços públicos.',styles['T']),Paragraph('Visão executiva ampliada com arquitetura, módulos estratégicos, integrações, fluxos operacionais, aplicações e especificações consolidadas.',styles['B']),Spacer(1,5*mm),Image(str(AS/'cco-final.jpg'),width=145*mm,height=82*mm),Spacer(1,4*mm),Paragraph('Edição 2026.08 · Conteúdo estruturado a partir do material mestre do portfólio URBAN BRAIN.',styles['S']),PageBreak()]
st += [Paragraph('VISÃO DO ECOSSISTEMA',styles['K']),Paragraph('Diferentes áreas. Uma única inteligência operacional.',styles['T']),Paragraph('A plataforma conecta segurança, educação, mobilidade, saúde, gestão territorial, defesa civil, documentos, ativos e equipes em uma experiência operacional comum. O objetivo é transformar eventos dispersos em contexto, decisão, execução e auditoria.',styles['B']),Spacer(1,3*mm),table([('Plataforma','Ambiente modular, multiempresa e multiorganização, com painel web, APIs e mobilidade.'),('Operações de campo','Atendimentos, ordens, SLAs, equipes, formulários, fotos, materiais, aprovação e execução offline-first.'),('Inteligência','Dashboards, mapas, indicadores, relatórios e assistente de IA.'),('GED com IA','Documentos, contratos, pesquisa, exportação e análise assistida.'),('GIS + CAD','Mapa operacional, despacho, veículos, sensores, ativos e recursos.'),('Governança','Perfis, permissões granulares, isolamento organizacional e trilha de auditoria.')]),PageBreak()]
st += [Paragraph('ARQUITETURA OPERACIONAL',styles['K']),Paragraph('Do evento ao indicador, sem perder contexto.',styles['T']),Paragraph('Uma jornada comum sustenta as verticais e organiza a operação ponta a ponta.',styles['B']),Spacer(1,3*mm),table([('01 · Detectar','Vídeo, IA, LPR/OCR, sensores, aplicativos e integrações.'),('02 · Contextualizar','GIS, histórico, entidade, território, criticidade e documentos.'),('03 · Coordenar','CAD, procedimentos, equipes, prioridades e recursos.'),('04 · Executar','Web, mobile, campo, evidências e registros operacionais.'),('05 · Auditar','BI, relatórios, KPIs, histórico e trilhas de alteração.'),('Base técnica','API REST, autenticação, multi-tenant, perfis e conectores definidos por projeto.')]),PageBreak()]
for n,title,sub,img,desc,caps,specs in modules:
 st += [Paragraph(f'MÓDULO {n}',styles['K']),Paragraph(title,styles['T']),Paragraph(sub,styles['B'])]
 top=Table([[Image(str(AS/img),width=112*mm,height=63*mm),Paragraph('<b>Resumo executivo</b><br/>'+desc,styles['B'])]],colWidths=[116*mm,132*mm]);top.setStyle(TableStyle([('VALIGN',(0,0),(-1,-1),'TOP')]));st += [top,Spacer(1,3*mm)]
 left=[Paragraph('<b>Capacidades principais</b>',styles['H'])]+bullets(caps)
 right=[Paragraph('<b>Especificações consolidadas</b>',styles['H']),table(specs,42*mm,82*mm)]
 cols=Table([[left,right]],colWidths=[120*mm,128*mm]);cols.setStyle(TableStyle([('VALIGN',(0,0),(-1,-1),'TOP')]));st += [cols,PageBreak()]
st += [Paragraph('MAPA DO PORTFÓLIO',styles['K']),Paragraph('24 soluções sobre uma base operacional comum.',styles['T']),Paragraph('O portfólio consolidado permite ativar capacidades por necessidade, escopo e contratação, mantendo uma arquitetura integrada.',styles['B'])]
st += [table(portfolio,58*mm,183*mm),PageBreak()]
st += [Paragraph('INTEGRAÇÃO, GOVERNANÇA E IMPLANTAÇÃO',styles['K']),Paragraph('Critérios técnicos para expansão sustentável.',styles['T']),table([('Modelo de implantação','Modular e faseável, preservando integrações existentes e ampliando capacidade por etapas.'),('Canais de acesso','Web, APIs e mobilidade conforme módulo, equipamento e escopo.'),('Integrações','Conectores e APIs definidos de acordo com infraestrutura, fontes de dados e sistemas legados.'),('Segurança','Perfis, permissões, isolamento entre organizações e trilha de auditoria.'),('Dados e evidências','Imagens, vídeos, documentos, localização e anexos podem ser relacionados ao contexto operacional.'),('Dimensionamento','Capacidade definida por usuários, ativos, câmeras, retenção, telemetria, analíticos, integrações e disponibilidade requerida.'),('Continuidade','Recursos offline-first e sincronização aplicáveis aos módulos de campo previstos no projeto.'),('Operação','Procedimentos, níveis de prioridade, SLAs, fluxos e responsabilidades configurados conforme o desenho operacional.')]),Spacer(1,4*mm),Paragraph('<b>Nota de escopo.</b> '+scope,styles['S']),PageBreak()]
st += [Paragraph('PRÓXIMO PASSO',styles['K']),Paragraph('Aprofunde o escopo com uma demonstração orientada ao cenário da cidade.',styles['T']),Paragraph('O catálogo apresenta o portfólio consolidado. A composição final deve considerar infraestrutura existente, integrações necessárias, prioridades de implantação, quantidade de ativos, retenção, conectividade e critérios de contratação.',styles['B']),Spacer(1,6*mm),table([('Demonstração','Solicitação pelo WhatsApp +55 11 98666-2944.'),('Objetivo','Apresentar fluxos, módulos e arquitetura aplicáveis ao cenário do município.'),('Preparação recomendada','Mapa de sistemas existentes, quantidade aproximada de ativos, principais dores operacionais e prioridades de implantação.')]),Spacer(1,7*mm),Paragraph('URBAN BRAIN · Inteligência que conecta cidades. Gestão que transforma.',styles['H'])]
doc.build(st,onFirstPage=footer,onLaterPages=footer)
print(f'V4 catalog generated: {OUT}')