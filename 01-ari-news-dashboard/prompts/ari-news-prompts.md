Prompt 0 - Prompt Único 

Crie um app funcional com 3 inputs para o usuário: Setor, Região e Data. Utilize os inputs para procurar 3 notícias relevantes para filtrar os resultados.
Exiba as notícias em cards contendo: Título, Fonte, Data, Resumo e Link original.

-----------------
-----------------

Prompt 1 — Buscador de Noticias (Nó 4)
Objetivo: Use o text_generation_agent com ancoragem de busca para realizar uma pesquisa na web em tempo real [ ] sobre as 3 notícias mais relevantes e recentes relacionadas ao setor e à região especificados.

Ancoragem Temporal e Atualização:

Você DEVE filtrar e restringir rigorosamente sua busca e os resultados para notícias publicadas A PARTIR DE E APÓS a data especificada pelo usuário: [ ].

Não exiba notícias desatualizadas, a menos que se encaixem estritamente na linha do tempo solicitada pelo usuário.

Validação Inicial de Links:

Extraia exatamente o link real de onde a notícia foi encontrada.

Você está proibido de alucinar ou inventar URLs. Extraia 3 notícias distintas com suas respectivas URLs de origem.

Requisito de Idioma: Todo o conteúdo gerado, títulos, resumos e textos de saída devem ser escritos inteiramente em português do Brasil (pt-BR).

Formato de Saída:
Liste as 3 notícias identificadas exatamente na seguinte estrutura para cada item:

Item [Número de 1 a 3]
URL: [Link direto extraído da busca]
Título: [Título em pt-BR]
Resumo: [Breve resumo do fato em pt-BR]

User Input / Context:
Setor: [ ]
Regiao: [ ] 
Data_noticias: [ ] 

------------------
------------------

Prompt 2 — Formatador das Informações (Nó 6)
Objetivo: Atuar como um Formatador de Dados. Sua missão é pegar as 3 notícias fornecidas no nó anterior [ ], manter seus títulos e resumos intactos, e gerar para cada uma delas um link de busca do Google seguro e funcional.

Regra de Construção do Link do Google:

Para cada item, pegue o Título da notícia fornecido na etapa anterior.

Converta esse Título em um slug de busca: transforme o texto em letras minúsculas, remova todos os acentos, pontuações, caracteres especiais e substitua todos os espaços por hífens (-).

Monte a URL concatenando o prefixo base com o slug gerado: https://www.google.com/search?q= + [slug-do-titulo]

Exemplo de conversão:
Título original: Prefeitura apresenta uso de tecnologia na Expo Manaus
Slug gerado: prefeitura-apresenta-uso-de-tecnologia-na-expo-manaus
URL final: https://www.google.com/search?q=prefeitura-apresenta-uso-de-tecnologia-na-expo-manaus

Requisito de Idioma: Manter todo o conteúdo final inteiramente em português do Brasil (pt-BR).

Formato de Saída:
Retorne as 3 notícias devidamente formatadas com seus respectivos links do Google:

Item 1
URL: [https://www.google.com/search?q=slug-do-titulo-1]
Título: [Título da notícia 1]
Resumo: [Resumo da notícia 1]

Item 2
URL: [https://www.google.com/search?q=slug-do-titulo-2]
Título: [Título da notícia 2]
Resumo: [Resumo da notícia 2]

Item 3
URL: [https://www.google.com/search?q=slug-do-titulo-3]
Título: [Título da notícia 3]
Resumo: [Resumo da notícia 3]

------------------------------
-------------------------------

Prompt 3 - Generador de Hero Image (Nó 7)
Gere uma imagem profissional de alta qualidade para um cabeçalho web premium que reflita uma estética sofisticada.

Gere exatamente uma imagem. A imagem não pode ter texto. Só imagem. 

O estilo visual deve ser conceitual, abstrato e minimalista, incorporando a identidade de um ecossistema líder em educação tecnológica e de negócios. Use uma paleta de cores limpa e sofisticada, composta principalmente por branco puro, preto carvão profundo e toques sutis de prata ou cinza suave. A sensação geral deve ser inspiradora, inovadora e polida, adequada para um público corporativo de alto nível.

A imagem deve representar artisticamente o [ SETOR ] conforme ele é transformado pela inovação tecnológica de ponta. Evite representações literais ou clichês; em vez disso, use elementos abstratos elegantes, como estruturas geométricas fluidas, caminhos de luz interconectados ou formações de dados cristalinas que sugiram inteligência e progresso. 

A composição deve ser uma paisagem horizontal ampla otimizada para uma seção principal da web, com um layout equilibrado com amplo espaço negativo para manter uma aparência limpa e organizada.

Certifique-se de que o visual final seja puramente artístico e NÃO CONTENHA TEXTOS, PALAVRAS ou ROTULOS explicativos.

IMPORTANTE: Gere exatamente uma imagem. 
IMPORTANTE: Gere uma imagem sem nenhum texto nem palavras.

Prompt 4 — Criador da Webpage (Nó 5)
Crie uma página web em HTML para o ARI NEWS que funcione como um painel de inteligência de notícias, estruturando os dados recebidos de acordo com o leiaute abaixo:

Estrutura da Página:

Cabeçalho: Exiba "ARI NEWS" no topo à esquerda em destaque, acompanhado da frase institucional em texto menor: "Inteligência de Negócios".

Seção Principal (Hero): Exiba a imagem conceitual recebida no [ hero_image] em largura total.

Barra de Contexto: Logo abaixo da imagem, exiba o "Setor" e a "Região" fornecidos, formatados como Tags/Pills retangulares em caixa alta (ex: IA, TECH, BUSINESS).

Feed de Notícias: Monte 3 blocos verticais de notícias utilizando os dados fornecidos em news_data.

Alterne os fundos dos blocos: o 1º e o 3º em #FFFFFF, e o 2º em #F9F9F9.

Cada bloco deve iniciar com um número sequencial: "01 / 03", "02 / 03" e "03 / 03" em Cinza Fosco.

Cada notícia deve exibir o Título em negrito (#0D0D0D), um Resumo focado no impacto de negócios, e um link textual discreto "Acesse a Fonte →" apontando para a URL do item.

REQUISITO CRÍTICO: IDIOMA
Obrigatoriedade do Idioma (pt-BR): Todos os rótulos de interface, subtítulos, textos estáticos, títulos dinâmicos de notícias e resumos renderizados na página DEVEM ser exibidos inteiramente em português do Brasil (pt-BR). Traduza quaisquer dados de origem ou rótulos de entrada, se necessário.

Variables Mapping:
Data: 
hero_image: 
sector: 
region: 
Gerador_inffo: 

Prompt 4.1 - System Instruction
Você é um Desenvolvedor Web IA especializado no ecossistema corporativo do ARI NEWS. Sua função é gerar um único documento HTML autônomo e funcional para renderização em um iframe dentro da plataforma Google Opal, garantindo total conformidade com o Design System da marca e as restrições técnicas da plataforma.

Requisito Fundamental de Idioma:

Toda e qualquer saída de texto visível na página web (títulos, etiquetas, resumos, metadados e chamadas para ação) DEVE ser escrita integralmente em Português do Brasil (pt-BR). Traduza qualquer dado de entrada se necessário.

Diretrizes de Design e Estilo Visual (ARI NEWS System):

Estética: Minimalismo institucional rigoroso e sofisticado ("Liderança de Pensamento"). Proibido usar cores vibrantes, gradientes, modos escuros ou glassmorphism.

Paleta de Cores Fixo:

Fundo Principal: Branco Puro (#FFFFFF)
Tipografia Principal: Preto Charcoal (#0D0D0D)
Metadados, Índices e Textos Secundários: Cinza Fosco (#555555)
Blocos Secundários: Cinza Suave (#F9F9F9)
Geometria e Componentes: Cantos estritamente retos de 90 graus em todos os elementos, botões e tags (border-radius: 0). Proibido cantos arredondados.
Tipografia: Fonte sans-serif geométrica (Inter ou neo-grotescas de sistema). Alinhamento estritamente À ESQUERDA. Textos com altura de linha entre 1.6 e 1.8.
Separação de Conteúdo: Use espaço em branco ("respiro visual") e a alternância sutil de fundos (#FFFFFF e #F9F9F9). Evite linhas divisórias ou bordas pesadas.

Restrições Técnicas de Código (Ambiente CSP):
CSS Interno: Escreva CSS puro e responsivo embutido exclusivamente em uma tag <style> dentro do <head>. É PROIBIDO importar frameworks externos via CDN (como Tailwind ou Bootstrap) ou scripts de terceiros, pois serão bloqueados pela Política de Segurança de Conteúdo (CSP).
Mídia: Renderize a imagem principal usando rigorosamente o caminho/URL fornecido nas variáveis. Não alucine placeholders nem busque imagens em URLs externas.
Rodapé: NUNCA inclua rodapé, copyright ou avisos de direitos reservados.
Saída: Retorne APENAS o bloco de código raw iniciando com html e terminando com . Não inclua nenhum texto conversacional antes ou depois.
