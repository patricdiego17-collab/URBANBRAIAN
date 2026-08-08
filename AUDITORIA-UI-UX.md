# Auditoria Corporativa de UI/UX e Front-end - URBAN BRAIN

## Resumo executivo

A auditoria identificou fragilidades de consistencia, dependencia externa de midia/fontes, renderizacao de imagens por CSS/JavaScript e falta de uma camada clara de conversao tecnica. A versao revisada padroniza a jornada, elimina dependencias automaticas de rede e introduz datasheets por modulo.

## Problemas encontrados e correcoes aplicadas

- **Midia instavel:** imagens eram definidas em HTML, sobrescritas por CSS e novamente alteradas por JavaScript. Isso gerava corrida de carregamento, cache inconsistente e cards vazios. **Correcao:** cada imagem agora existe localmente e e renderizada por `<img>` ou caminho local estavel, sem troca em runtime.
- **Dependencias externas automaticas:** paginas internas carregavam Google Fonts e URLs Pexels. **Correcao:** removidas chamadas externas automaticas; o site usa stack tipografica local e assets versionados.
- **Dependencias automaticas no navegador:** parte da midia era solicitada fora do site e podia gerar bloqueios/permissoes. **Correcao:** a experiencia publicada usa caminhos locais; downloads de acervo remanescente acontecem apenas na etapa de build, nunca no navegador do visitante.
- **Navegacao inconsistente entre modulos:** headers e menus variavam por pagina. **Correcao:** padrao unico de cabecalho, mega menu, menu mobile e rodape.
- **Arquitetura de informacao pouco tecnica nas paginas de modulo:** faltava navegacao interna. **Correcao:** barra sticky com Visao geral, Capacidades, Integracoes, Fluxo e Datasheet.
- **Conversao tecnica ausente:** nao havia material para decisores e equipes de compras/engenharia levarem da pagina. **Correcao:** CTA `Baixar Datasheet (PDF)` em todos os cards e paginas, com cinco PDFs reais.
- **Acessibilidade e performance:** backgrounds sem texto alternativo e carregamento indiscriminado. **Correcao:** imagens semanticas com `alt`, `loading="lazy"` nos cards, foco visivel, `aria-expanded`, `prefers-reduced-motion` e menos requisicoes.

## Curadoria visual por modulo

### CCO e Segurança

Central de monitoramento real, em tons escuros, com parede de telas exibindo câmeras urbanas ao vivo e operadores uniformizados observando os monitores. Evitar estética de ficção científica.

### Educação e Escolas

Entrada de escola ou sala de aula clara e realista, com uma câmera/terminal enquadrando o rosto de uma criança e interface discreta mostrando “presença confirmada”, com professor ou agente escolar próximo.

### Transporte Público

Interior ou porta de embarque de ônibus urbano moderno, com passageiro diante de validador facial, câmera visível e confirmação discreta de acesso. Mostrar equipamento realista e ambiente de transporte público, sem parecer catraca de aeroporto.

### Saúde Digital

Sala de telemedicina/UBS real, com profissional de saúde usando notebook e biomonitores (ECG, estetoscópio digital ou oxímetro), tela com teleinterconsulta e aparência clínica limpa, humana e tecnológica.

### Telegestão e Defesa Civil

Cena real de defesa civil municipal: pluviômetro/sensor em área de risco, poste de sirene ou estação de alerta e equipe de campo uniformizada, preferencialmente sob tempo nublado/chuvoso. Combinar prevenção de risco com infraestrutura inteligente, sem cenas de desastre sensacionalistas.

## Melhorias adicionais implementadas

1. **Trust strip B2B na Home:** arquitetura modular, interoperabilidade, operacao em tempo real e rastreabilidade aparecem antes dos modulos para reduzir incerteza de gestores e equipes tecnicas.
2. **Navegacao tecnica sticky nas paginas internas:** acelera leitura em reunioes, editais e avaliacao tecnica sem obrigar scroll linear.
3. **Experiencia sem chamadas externas automaticas:** imagens, CSS e JavaScript consumidos pelo visitante sao servidos pelo proprio GitHub Pages; o WhatsApp so e aberto quando o usuario clica no CTA.
4. **Hierarquia de CTA em duas camadas:** `Conhecer o modulo` para exploracao e `Baixar Datasheet (PDF)` para conversao tecnica, mantendo `Solicitar Demonstracao` como contato fixo.

## Observacoes de curadoria futura

- Transporte: substituir a foto atual por cena de embarque com validador facial quando houver acervo institucional ou foto licenciada especifica.
- Defesa Civil: priorizar imagem que mostre sensor/pluviometro e sirene/equipe de campo no mesmo contexto; a foto atual comunica melhor telegestao de iluminacao do que prevencao de risco.
- Inteligencia Operacional: o maior salto de credibilidade futuro vira de screenshots reais do software, com dados anonimizados, em vez de mockups genericos.
