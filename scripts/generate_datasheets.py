#!/usr/bin/env python3
from pathlib import Path
import textwrap

ROOT = Path(__file__).resolve().parent.parent if Path(__file__).parent.name == 'scripts' else Path(__file__).resolve().parent
OUT = ROOT / 'datasheets'
OUT.mkdir(parents=True, exist_ok=True)

MODULES = [
    ('cco-seguranca','CCO e Seguranca','Videomonitoramento com IA, muralha inteligente, despacho e investigacao operacional.',
     ['Videomonitoramento com IA para deteccao e geracao de alertas.','Muralha Inteligente com leitura LPR/OCR, passagens, restricoes e correlacoes.','Central de Despacho (CAD) com triagem, prioridade, mapa operacional e envio de recursos.','Playback, evidencias, historico e integracao com GED, frotas, telemetria e BI.'],
     ['VMS / CFTV','CAD','GIS','GED + IA','Frotas','Telemetria','APIs'],
     ['Detectar: video, IA, LPR e sensores.','Contextualizar: mapa, historico e prioridade.','Despachar: equipe ou viatura adequada.','Auditar: evidencias, KPIs e historico.'],
     'Central de monitoramento real, em tons escuros, com parede de telas exibindo cameras urbanas ao vivo e operadores uniformizados. Evitar estetica de ficcao cientifica.'),
    ('educacao-escolas','Educacao e Escolas','Frequencia facial, comunicacao com familias, protecao escolar e prevencao a evasao.',
     ['Registro facial automatico de presenca.','Notificacoes de entrada, ausencia e eventos relevantes por canais digitais.','Indicadores para apoio a prevencao da evasao escolar.','Integracao com transporte escolar, saude, ocorrencias e dados georreferenciados.'],
     ['Biometria facial','Notificacoes','Transporte escolar','GIS','Ocorrencias','APIs'],
     ['Registrar: identificacao facial e frequencia.','Comunicar: alertas e notificacoes.','Monitorar: presenca, padroes e evasao.','Atuar: rede escolar integrada.'],
     'Entrada de escola ou sala de aula clara e realista, com camera/terminal enquadrando o rosto de uma crianca e interface discreta mostrando presenca confirmada, com professor ou agente escolar proximo.'),
    ('transporte-publico','Transporte Publico','Reconhecimento facial 1:N, embarque touchless e inteligencia antifraude.',
     ['Reconhecimento facial 1:N como credencial de mobilidade.','Embarque touchless com menor dependencia de midia fisica.','Inteligencia antifraude com acuracia superior a 99,5% conforme referencia do projeto.','Implantacao faseada com possibilidade de reaproveitamento da infraestrutura existente.'],
     ['Biometria 1:N','Validador','Aplicativo','Frotas','Telemetria','BI','APIs'],
     ['Identificar: reconhecimento facial.','Validar: credencial e regras.','Permitir: embarque e registro.','Analisar: uso, fraude e desempenho.'],
     'Interior ou porta de embarque de onibus urbano moderno, com passageiro diante de validador facial, camera visivel e confirmacao discreta de acesso.'),
    ('saude-digital','Saude Digital','UBS digital, e-SUS AB, teleinterconsulta, biomonitores IoT e inteligencia territorial.',
     ['UBS com fluxos assistenciais 100% digitais.','Integracao bidirecional nativa ao e-SUS AB.','Teleinterconsulta com biomonitores IoT, incluindo ECG e estetoscopio digital.','Mapeamento georreferenciado de endemias e visao territorial.'],
     ['e-SUS AB','Telemedicina','Biomonitores IoT','GIS','Prontuario','APIs'],
     ['Coletar: dados clinicos e operacionais.','Conectar: e-SUS AB e dispositivos.','Acompanhar: teleinterconsulta e monitoramento.','Prevenir: inteligencia territorial.'],
     'Sala de telemedicina/UBS real, com profissional de saude usando notebook e biomonitores, tela com teleinterconsulta e aparencia clinica limpa, humana e tecnologica.'),
    ('telegestao-defesa-civil','Telegestao e Defesa Civil','Iluminacao inteligente, pluviometria, sirenes, sensores e campo offline-first.',
     ['Telegestao de iluminacao publica com telemetria, consumo e manutencao preditiva.','Monitoramento pluviometrico preventivo e leitura de risco.','Sirenes com acionamento manual ou automatico.','Aplicativo de campo offline-first com sincronizacao posterior.'],
     ['IoT','Iluminacao','Pluviometria','Sirenes','GIS','Offline-first','APIs'],
     ['Monitorar: sensores, clima e infraestrutura.','Avaliar: risco e contexto territorial.','Acionar: alertas, sirenes e equipes.','Registrar: historico e KPIs.'],
     'Cena real de defesa civil municipal: pluviometro/sensor em area de risco, poste de sirene ou estacao de alerta e equipe de campo uniformizada, preferencialmente sob tempo nublado/chuvoso.'),
]

W,H=595.28,841.89
NAVY=(7/255,17/255,30/255); BLUE=(7/255,133/255,1); CYAN=(18/255,209/255,236/255); MUTED=(90/255,112/255,134/255); LIGHT=(244/255,247/255,251/255); WHITE=(1,1,1); LINE=(217/255,227/255,237/255)

def esc(s):
    # ASCII-only input by design, escape PDF delimiters
    return s.replace('\\','\\\\').replace('(','\\(').replace(')','\\)')

def rgb(c): return f'{c[0]:.3f} {c[1]:.3f} {c[2]:.3f}'

def text(x,y,s,size=10,bold=False,color=NAVY):
    font='F2' if bold else 'F1'
    return f'BT /{font} {size} Tf {rgb(color)} rg 1 0 0 1 {x:.1f} {y:.1f} Tm ({esc(s)}) Tj ET\n'

def rect(x,y,w,h,color,stroke=None,radius=0):
    # rounded corners omitted for portability; still clean corporate blocks
    out=f'{rgb(color)} rg {x:.1f} {y:.1f} {w:.1f} {h:.1f} re f\n'
    if stroke: out+=f'{rgb(stroke)} RG {x:.1f} {y:.1f} {w:.1f} {h:.1f} re S\n'
    return out

def line(x1,y1,x2,y2,color=LINE,width=1): return f'{rgb(color)} RG {width} w {x1:.1f} {y1:.1f} m {x2:.1f} {y2:.1f} l S\n'

def wrap(s,n): return textwrap.wrap(s,width=n,break_long_words=False,break_on_hyphens=False) or ['']

def stream_page(slug,title,subtitle,bullets,integrations,flow,visual):
    c=''
    c+=rect(0,H-205,W,205,NAVY); c+=rect(0,H-205,9,205,BLUE)
    c+=text(52,H-48,'URBAN BRAIN',10,True,WHITE); c+=text(52,H-72,'DATASHEET TECNICO',8,True,CYAN)
    c+=text(52,H-112,title,23,True,WHITE)
    yy=H-136
    for ln in wrap(subtitle,78): c+=text(52,yy,ln,9,False,(.72,.80,.87)); yy-=13
    yy=H-250; c+=text(52,yy,'CAPACIDADES PRINCIPAIS',12,True,NAVY); yy-=24
    for b in bullets:
        c+=rect(52,yy-2,6,6,BLUE)
        for ln in wrap(b,88): c+=text(66,yy,ln,9,False,MUTED); yy-=12
        yy-=8
    c+=text(52,yy,'INTEGRACOES E CAMADAS',12,True,NAVY); yy-=25
    xx=52
    for tag in integrations:
        tw=max(58, 7.2*len(tag)+18)
        if xx+tw>W-52: xx=52; yy-=30
        c+=rect(xx,yy-7,tw,22,(.91,.96,1)); c+=text(xx+8,yy,tag,7.5,True,(.04,.43,.69)); xx+=tw+8
    c+=line(52,42,W-52,42); c+=text(52,25,'URBAN BRAIN | Documento comercial tecnico',7,False,MUTED); c+=text(W-145,25,'Versao 2026.08',7,False,MUTED)
    p1=c
    c=''; c+=rect(0,0,W,H,LIGHT); c+=rect(0,H-95,W,95,NAVY); c+=text(52,H-58,title,17,True,WHITE); c+=text(W-170,H-58,'ARQUITETURA E OPERACAO',7.5,True,CYAN)
    yy=H-140; c+=text(52,yy,'FLUXO OPERACIONAL',12,True,NAVY); yy-=30
    boxw=(W-104-24)/4
    xx=52
    for i,item in enumerate(flow):
        c+=rect(xx,yy-76,boxw,76,WHITE,LINE); c+=rect(xx+9,yy-20,18,18,BLUE); c+=text(xx+15,yy-15,str(i+1),7.5,True,WHITE)
        parts=item.split(':',1); c+=text(xx+9,yy-38,parts[0],8.4,True,NAVY)
        body=parts[1].strip() if len(parts)>1 else ''
        ty=yy-52
        for ln in wrap(body,22): c+=text(xx+9,ty,ln,7.1,False,MUTED); ty-=9
        xx+=boxw+8
    yy-=116; c+=text(52,yy,'DIRETRIZ VISUAL RECOMENDADA',12,True,NAVY); yy-=20
    c+=rect(52,yy-112,W-104,112,WHITE,LINE); ty=yy-24
    for ln in wrap(visual,92): c+=text(65,ty,ln,8.2,False,MUTED); ty-=12
    c+=rect(52,65,W-104,62,NAVY); c+=text(68,102,'SOLICITE UMA DEMONSTRACAO TECNICA',10,True,WHITE); c+=text(68,84,'WhatsApp: +55 11 98666-2944',8,False,(.66,.77,.85))
    c+=text(52,34,'Recursos, integracoes e escopo final devem ser definidos conforme projeto e requisitos de contratacao.',6.5,False,MUTED)
    return [p1,c]

def build_pdf(path,pages):
    objs=[]
    # 1 catalog, 2 pages, 3 font normal, 4 font bold
    objs.append('<< /Type /Catalog /Pages 2 0 R >>')
    kids=' '.join(f'{5+i*2} 0 R' for i in range(len(pages)))
    objs.append(f'<< /Type /Pages /Kids [{kids}] /Count {len(pages)} >>')
    objs.append('<< /Type /Font /Subtype /Type1 /BaseFont /Helvetica >>')
    objs.append('<< /Type /Font /Subtype /Type1 /BaseFont /Helvetica-Bold >>')
    for i,content in enumerate(pages):
        page_obj=5+i*2; stream_obj=page_obj+1
        objs.append(f'<< /Type /Page /Parent 2 0 R /MediaBox [0 0 {W:.2f} {H:.2f}] /Resources << /Font << /F1 3 0 R /F2 4 0 R >> >> /Contents {stream_obj} 0 R >>')
        b=content.encode('latin-1')
        objs.append(f'<< /Length {len(b)} >>\nstream\n'+content+'endstream')
    out=bytearray(b'%PDF-1.4\n%\xe2\xe3\xcf\xd3\n')
    offsets=[0]
    for i,obj in enumerate(objs,1):
        offsets.append(len(out)); out+=f'{i} 0 obj\n'.encode(); out+=obj.encode('latin-1'); out+=b'\nendobj\n'
    xref=len(out); out+=f'xref\n0 {len(objs)+1}\n'.encode(); out+=b'0000000000 65535 f \n'
    for off in offsets[1:]: out+=f'{off:010d} 00000 n \n'.encode()
    out+=f'trailer\n<< /Size {len(objs)+1} /Root 1 0 R >>\nstartxref\n{xref}\n%%EOF\n'.encode()
    path.write_bytes(out)

for m in MODULES:
    slug,title,subtitle,bullets,integrations,flow,visual=m
    build_pdf(OUT/f'{slug}.pdf', stream_page(*m))
print('Generated',len(MODULES),'datasheets in',OUT)
