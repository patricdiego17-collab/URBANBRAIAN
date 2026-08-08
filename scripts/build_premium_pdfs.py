from reportlab.pdfgen import canvas
from reportlab.lib.pagesizes import A4, landscape
from reportlab.lib.colors import HexColor, Color, white
from reportlab.pdfbase.ttfonts import TTFont
from reportlab.pdfbase import pdfmetrics
from reportlab.lib.utils import ImageReader
from PIL import Image
from pathlib import Path
R=Path(__file__).resolve().parents[1]; A=R/'assets'; O=A/'pdf-optimized'; D=R/'datasheets';D.mkdir(exist_ok=True);O.mkdir(exist_ok=True)
pdfmetrics.registerFont(TTFont('U','/usr/share/fonts/truetype/dejavu/DejaVuSans.ttf'));pdfmetrics.registerFont(TTFont('B','/usr/share/fonts/truetype/dejavu/DejaVuSans-Bold.ttf'))
N=HexColor('#06101C');N2=HexColor('#0A1A2B');BL=HexColor('#0A9DFF');CY=HexColor('#21C7E8');TX=HexColor('#12263A');MU=HexColor('#61788E');LI=HexColor('#D8E6F1');BG=HexColor('#F4F8FB')
mods=[
('cco-seguranca','01','CCO e Segurança','Videomonitoramento, visão computacional, muralha inteligente e despacho coordenado.','cco-final.jpg','+40 mil','capacidade de câmeras',['IA e alertas de vídeo','LPR/OCR e muralha inteligente','CAD, mapas e despacho','Playback, evidências e GED'],['VMS','LPR/OCR','CAD','GIS','GED','BI']),
('educacao-escolas','02','Educação e Escolas','Frequência facial, proteção escolar, comunicação com famílias e prevenção à evasão.','educacao-final-v3.jpg','Tempo real','registro e comunicação',['Presença facial automática','Notificações de entrada e ausência','Apoio ao combate à evasão','Segurança e visão territorial'],['Biometria','Escolas','Notificações','GIS','BI','APIs']),
('transporte-publico','03','Transporte Público','Reconhecimento facial 1:N, embarque touchless, recarga digital e inteligência antifraude.','transporte-v2.jpg','>99,5%','referência antifraude',['Biometria facial 1:N','Embarque touchless','Recarga digital pelo aplicativo','Implantação faseada'],['1:N','Validador','Aplicativo','Frotas','Telemetria','BI']),
('saude-digital','04','Saúde Digital','UBS digital, integração bidirecional ao e-SUS AB, teleinterconsulta e inteligência territorial.','saude-real.jpg','100%','jornada digital na UBS',['Fluxos assistenciais digitais','Integração bidirecional e-SUS AB','Teleinterconsulta e biomonitores IoT','Georreferenciamento de endemias'],['e-SUS AB','Telemedicina','IoT','GIS','BI','APIs']),
('telegestao-defesa-civil','05','Telegestão e Defesa Civil','Iluminação inteligente, pluviometria, sirenes, sensores e campo offline-first.','defesa-civil-real.jpg','Offline-first','continuidade em campo',['Dimerização e acionamento remoto','Consumo e manutenção preditiva','Pluviometria e leitura de risco','Alertas, sirenes e campo offline'],['IoT','MQTT','Iluminação','Pluviometria','Sirenes','GIS'])]

def prep(name,maxd=1500):
 s=A/name; d=O/name
 if s.exists():
  im=Image.open(s).convert('RGB');im.thumbnail((maxd,maxd),Image.LANCZOS);im.save(d,'JPEG',quality=84,optimize=True)
 return d
for n in ['hero-real.jpg','cco-final.jpg','educacao-final-v3.jpg','transporte-v2.jpg','saude-real.jpg','defesa-civil-real.jpg','urban-brain-wordmark.jpg']:prep(n,1800 if n=='hero-real.jpg' else 1400)

def img(c,p,x,y,w,h):
 try:
  im=Image.open(p);iw,ih=im.size;s=max(w/iw,h/ih);nw,nh=iw*s,ih*s;c.drawImage(ImageReader(im),x-(nw-w)/2,y-(nh-h)/2,nw,nh)
 except:c.setFillColor(N2);c.rect(x,y,w,h,fill=1,stroke=0)
def box(c,x,y,w,h,fill=N2,stroke=None,r=9):
 c.setFillColor(fill);c.setStrokeColor(stroke or fill);c.roundRect(x,y,w,h,r,fill=1,stroke=1 if stroke else 0)
def txt(c,t,x,y,s=9,f='U',col=TX,w=None,l=None):
 c.setFillColor(col);c.setFont(f,s)
 if not w:c.drawString(x,y,t);return y
 l=l or s*1.35;line='';yy=y
 for q in t.split():
  z=(line+' '+q).strip()
  if c.stringWidth(z,f,s)<=w:line=z
  else:c.drawString(x,yy,line);yy-=l;line=q
 if line:c.drawString(x,yy,line);yy-=l
 return yy
def logo(c,x,y,w=100):
 try:
  im=Image.open(O/'urban-brain-wordmark.jpg');iw,ih=im.size;c.drawImage(ImageReader(im),x,y-w*ih/iw,w,w*ih/iw)
 except:pass
def foot(c,W,n,dark=False):
 c.setStrokeColor(HexColor('#28465F') if dark else LI);c.line(28,22,W-28,22);c.setFillColor(HexColor('#8AA4B9'));c.setFont('U',6);c.drawString(28,10,'URBAN BRAIN | Documento comercial técnico');c.drawRightString(W-28,10,str(n).zfill(2))
def pills(c,items,x,y,maxw):
 xx=x;yy=y
 for q in items:
  w=c.stringWidth(q,'B',7)+18
  if xx+w>x+maxw:xx=x;yy-=24
  box(c,xx,yy,w,18,HexColor('#EAF5FD'),None,5);c.setFillColor(HexColor('#0879C6'));c.setFont('B',7);c.drawCentredString(xx+w/2,yy+5,q);xx+=w+6

W,H=landscape(A4);out=R/'URBAN-BRAIN-Apresentacao-Executiva.pdf';c=canvas.Canvas(str(out),pagesize=(W,H))
img(c,O/'hero-real.jpg',0,0,W,H);c.setFillColor(Color(0.01,0.03,0.06,.84));c.rect(0,0,W,H,fill=1,stroke=0);logo(c,38,H-34,130);c.setFillColor(CY);c.setFont('B',8);c.drawString(40,H-102,'APRESENTAÇÃO EXECUTIVA | SMART CITIES & OPERAÇÃO URBANA');txt(c,'O Cérebro Digital da Cidade',40,H-150,35,'B',white,460,38);txt(c,'Segurança, educação, mobilidade, saúde, gestão urbana e defesa civil conectados em uma visão operacional única.',40,H-238,11,'U',HexColor('#D7E8F5'),460,16);x=40
for v,l in [('+40 mil','capacidade de câmeras'),('>99,5%','referência antifraude'),('5','verticais integradas'),('360º','visão operacional')]:box(c,x,56,120,48,Color(.03,.1,.18,.9),HexColor('#2C5677'));c.setFillColor(white);c.setFont('B',14);c.drawString(x+12,80,v);c.setFillColor(HexColor('#8FB1CB'));c.setFont('U',6);c.drawString(x+12,67,l);x+=128
c.showPage()
c.setFillColor(BG);c.rect(0,0,W,H,fill=1,stroke=0);logo(c,30,H-28);c.setFillColor(BL);c.setFont('B',8);c.drawString(30,H-84,'VISÃO DA PLATAFORMA');txt(c,'Uma operação urbana unificada, do sensor à decisão.',30,H-118,27,'B',TX,500,30);txt(c,'Detectar, contextualizar, coordenar, executar e auditar em uma mesma lógica operacional.',30,H-165,10,'U',MU,430,14);st=[('1','DETECTA','IA, vídeo, LPR e sensores'),('2','CONTEXTUALIZA','GIS, histórico e criticidade'),('3','COORDENA','CAD, protocolos e recursos'),('4','EXECUTA','equipes, mobile e evidências'),('5','AUDITA','BI, KPIs e rastreabilidade')];x=30;y=110;g=8;bw=(W-60-g*4)/5
for n,h,d in st:box(c,x,y,bw,102,white,LI);box(c,x+12,y+64,28,24,N2);c.setFillColor(CY);c.setFont('B',8);c.drawCentredString(x+26,y+72,n);c.setFillColor(TX);c.setFont('B',8);c.drawString(x+12,y+48,h);txt(c,d,x+12,y+31,7,'U',MU,bw-24,10);x+=bw+g
foot(c,W,2);c.showPage()
for pi,m in enumerate(mods,3):
 key,num,title,sub,ph,metric,ml,caps,ints=m;c.setFillColor(BG);c.rect(0,0,W,H,fill=1,stroke=0);img(c,O/ph,W*.52,0,W*.48,H);logo(c,30,H-28,92);c.setFillColor(BL);c.setFont('B',8);c.drawString(30,H-85,f'MÓDULO {num} | {title.upper()}');txt(c,title,30,H-118,27,'B',TX,W*.43,30);txt(c,sub,30,H-160,9,'U',MU,W*.43,13);box(c,30,H-252,150,60,N2);c.setFillColor(CY);c.setFont('B',17);c.drawString(44,H-220,metric);c.setFillColor(HexColor('#A8C1D4'));c.setFont('U',6.5);c.drawString(44,H-237,ml);c.setFillColor(TX);c.setFont('B',9);c.drawString(30,H-286,'CAPACIDADES-CHAVE');yy=H-310
 for q in caps:c.setFillColor(BL);c.circle(34,yy+2,2.2,fill=1,stroke=0);yy=txt(c,q,44,yy,7.4,'U',MU,W*.42,10)-5
 c.setFillColor(TX);c.setFont('B',9);c.drawString(30,86,'INTEGRAÇÕES E CAMADAS');pills(c,ints,30,56,W*.43);foot(c,W,pi);c.showPage()
c.setFillColor(N);c.rect(0,0,W,H,fill=1,stroke=0);logo(c,30,H-28);c.setFillColor(CY);c.setFont('B',8);c.drawString(30,H-84,'ARQUITETURA E INTEROPERABILIDADE');txt(c,'Aberta para integrar. Estruturada para operar.',30,H-120,27,'B',white,520,30);txt(c,'Camadas de operação, dados, integração, IoT, mobilidade de campo e governança.',30,H-164,10,'U',HexColor('#9AB4C8'),470,14);cards=[('OPERAÇÃO','CAD · VMS · Muralha · GIS'),('DADOS','BI · GED · histórico · auditoria'),('INTEGRAÇÃO','APIs · OAuth2 · SDKs'),('CAMPO','Mobile · GPS · offline-first'),('IOT','MQTT · gateways · telemetria'),('CONTROLE','RBAC · multi-tenant · áreas')];x=30;y=70;bw=(W-76)/3
for i,(h,d) in enumerate(cards):cx=x+(i%3)*(bw+8);cy=y+(1-i//3)*98;box(c,cx,cy,bw,82,N2,HexColor('#24445E'));c.setFillColor(CY);c.setFont('B',7);c.drawString(cx+14,cy+56,h);txt(c,d,cx+14,cy+34,8,'U',HexColor('#D3E6F4'),bw-28,11)
foot(c,W,8,True);c.showPage()
img(c,O/'hero-real.jpg',0,0,W,H);c.setFillColor(Color(.01,.04,.08,.9));c.rect(0,0,W,H,fill=1,stroke=0);logo(c,38,H-34,115);c.setFillColor(CY);c.setFont('B',8);c.drawString(40,H-110,'PRÓXIMO PASSO');txt(c,'Leve a inteligência para a operação real.',40,H-150,32,'B',white,480,35);txt(c,'Solicite uma demonstração técnica e percorra os módulos, integrações e arquitetura em um cenário aderente à realidade do município.',40,H-230,11,'U',HexColor('#D3E6F4'),450,16);box(c,40,80,245,50,BL);c.setFillColor(white);c.setFont('B',11);c.drawString(58,100,'SOLICITAR DEMONSTRAÇÃO');c.setFillColor(HexColor('#A9C3D7'));c.setFont('U',8);c.drawString(40,55,'WhatsApp +55 11 98666-2944');c.save()
PW,PH=A4
for m in mods:
 key,num,title,sub,ph,metric,ml,caps,ints=m;p=D/(key+'.pdf');c=canvas.Canvas(str(p),pagesize=A4);c.setFillColor(N);c.rect(0,0,PW,PH,fill=1,stroke=0);img(c,O/ph,0,PH*.55,PW,PH*.45);c.setFillColor(Color(.01,.04,.08,.58));c.rect(0,PH*.55,PW,PH*.45,fill=1,stroke=0);logo(c,26,PH-24,96);c.setFillColor(CY);c.setFont('B',7);c.drawString(27,PH-88,f'DATASHEET TÉCNICO | MÓDULO {num}');txt(c,title,27,PH-116,24,'B',white,PW-54,27);txt(c,sub,27,PH-151,8.5,'U',HexColor('#D8EAF6'),PW-54,12);c.setFillColor(white);c.rect(0,0,PW,PH*.55,fill=1,stroke=0);box(c,27,PH*.55-72,150,54,N2);c.setFillColor(CY);c.setFont('B',16);c.drawString(41,PH*.55-43,metric);c.setFillColor(HexColor('#A7C1D5'));c.setFont('U',6);c.drawString(41,PH*.55-58,ml);c.setFillColor(TX);c.setFont('B',9);c.drawString(27,PH*.55-103,'CAPACIDADES PRINCIPAIS');yy=PH*.55-128
 for q in caps:c.setFillColor(BL);c.circle(31,yy+2,2.2,fill=1,stroke=0);yy=txt(c,q,40,yy,7.5,'U',MU,PW-72,10)-5
 c.setFillColor(TX);c.setFont('B',9);c.drawString(27,116,'INTEGRAÇÕES E CAMADAS');pills(c,ints,27,86,PW-54);foot(c,PW,1);c.showPage();c.setFillColor(BG);c.rect(0,0,PW,PH,fill=1,stroke=0);logo(c,27,PH-25,92);c.setFillColor(BL);c.setFont('B',7);c.drawString(27,PH-86,'ARQUITETURA OPERACIONAL');txt(c,'Do evento ao indicador.',27,PH-116,24,'B',TX,PW-54,27);txt(c,'Integração modular, rastreabilidade, segurança por perfis e expansão por etapas.',27,PH-150,8.5,'U',MU,PW-54,12);flows=['Detectar','Contextualizar','Executar','Auditar'];x=27;y=PH-285;bw=(PW-54-24)/4
 for i,q in enumerate(flows):box(c,x+i*(bw+8),y,bw,82,white,LI);box(c,x+i*(bw+8)+10,y+52,24,18,N2);c.setFillColor(CY);c.setFont('B',7);c.drawCentredString(x+i*(bw+8)+22,y+58,str(i+1));c.setFillColor(TX);c.setFont('B',7);c.drawString(x+i*(bw+8)+10,y+34,q)
 box(c,27,82,PW-54,108,N2);c.setFillColor(CY);c.setFont('B',7);c.drawString(42,160,'PRÓXIMO PASSO');c.setFillColor(white);c.setFont('B',15);c.drawString(42,135,'Solicite uma demonstração técnica.');txt(c,'Percorra fluxos, integrações e arquitetura em um cenário aderente ao município.',42,112,7.5,'U',HexColor('#B5CCDD'),PW-84,10);c.setFillColor(white);c.setFont('B',8);c.drawString(42,94,'WhatsApp +55 11 98666-2944');foot(c,PW,2);c.save()
print('premium PDFs generated')
