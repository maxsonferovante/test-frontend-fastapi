# Research: Listagem de Certificados por Email

## Decision 1: Fixar o backend na versao de FastAPI ja adotada pelo workspace

- Decision: usar FastAPI 0.138.1 no backend.
- Rationale: a versao ja esta fixada no `backend/pyproject.toml`, atende ao requisito funcional do projeto e suporta a abordagem oficial de servir frontend estatico via `app.frontend()`.
- Alternatives considered:
  - Retroceder para uma versao anterior do framework. Rejeitada porque perderia alinhamento com o estado atual do workspace sem beneficio claro.
  - Servir frontend com `StaticFiles`. Rejeitada porque o usuario explicitamente pediu a nova feature documentada em `tutorial/frontend/`.

## Decision 2: Manter React Router na linha v7 pedida pelo usuario

- Decision: usar React Router 7.18.0.
- Rationale: o workspace ja fixa `react-router` e `react-router-dom` em 7.18.0, preservando a major v7 solicitada pelo usuario e evitando migracao desnecessaria durante a entrega desta feature.
- Alternatives considered:
  - Migrar para uma major posterior. Rejeitada porque contraria a restricao explicita do pedido.
  - Evitar roteador e manter tela unica sem rotas. Rejeitada porque React Router continua util para organizar a SPA, estados de busca e futuras extensoes.

## Decision 3: Backend como facade da API externa de certificados

- Decision: o frontend conversa apenas com um endpoint interno do backend; o backend chama `GET /dev/api/v1/users/{email}/certificates` no provedor externo com `x-api-key`.
- Rationale: a chave da API nao pode ser exposta no navegador. O facade tambem permite normalizar mensagens de erro, mapear contratos e isolar eventual mudanca do provedor externo.
- Alternatives considered:
  - Chamar a API externa diretamente do frontend. Rejeitada por expor segredo e acoplar a UI a contrato externo.
  - Persistir os dados externamente em banco local. Rejeitada por adicionar complexidade sem requisito de historico ou cache persistente.

## Decision 4: Filtrar no frontend sem nova chamada externa para a mesma busca

- Decision: a busca por email retorna a colecao completa e o filtro `all|success|failed` e aplicado localmente sobre o resultado atual.
- Rationale: o contrato externo ja retorna certificados com o campo `success`; reaproveitar a resposta evita round-trip desnecessario e torna a alternancia instantanea.
- Alternatives considered:
  - Reconsultar o backend a cada troca de filtro. Rejeitada por custo desnecessario e UX pior.
  - Pedir ao provedor externo filtros por status. Rejeitada porque o contrato informado nao mostra esse recurso.

## Decision 5: Servir o build do frontend pelo FastAPI com `app.frontend()`

- Decision: o backend usara `app.frontend("/", directory="dist")` ou variante equivalente apontando para o build publicado do frontend.
- Rationale: a documentacao oficial do FastAPI para frontend descreve essa capacidade para servir arquivos gerados do frontend, com fallback automatico para `index.html` quando aplicavel em rotas client-side.
- Alternatives considered:
  - Nginx separado para assets. Rejeitada nesta fase por complexidade operacional desnecessaria.
  - Embutir assets manualmente via `StaticFiles`. Rejeitada porque a nova API do framework atende exatamente o caso descrito.

## Decision 6: UI baseada em Chakra UI com estilizacao e tokens alinhados a Tailwind v4

- Decision: usar Chakra UI como base de componentes e tema, com tokens e estilos compartilhando o fluxo moderno de Tailwind CSS v4 e padroes do shadcn/ui para composicao visual.
- Rationale: o usuario pediu os componentes do Chakra UI e a estilizacao do shadcn com Tailwind v4. A combinacao atende bem desde que Chakra seja a camada primaria de componentes e Tailwind/shadcn forneca tokens, utilitarios e eventuais blocos visuais reaproveitaveis.
- Alternatives considered:
  - Usar apenas Chakra UI. Rejeitada porque ignora o direcionamento de estilizacao com shadcn/Tailwind v4.
  - Usar apenas shadcn/ui. Rejeitada porque ignora o requisito explicito de componentes Chakra.

## Decision 7: Sem banco de dados na v1

- Decision: nao introduzir persistencia local neste ciclo.
- Rationale: a aplicacao apenas consulta e apresenta dados do provedor externo. Sem requisito de cache duravel, auditoria local ou historico, manter leitura direta reduz risco e complexidade.
- Alternatives considered:
  - Cache em memoria. Adiado; pode ser avaliado se a latencia real justificar.
  - Banco relacional/documental. Rejeitado por estar fora do escopo da feature.

## Decision 8: Distribuir backend e frontend em uma unica imagem Docker

- Decision: publicar a aplicacao em uma unica imagem Docker gerada por build multi-stage na raiz do repositorio.
- Rationale: o requisito de portabilidade pede um unico artefato de entrega. O backend ja serve o build do frontend pelo FastAPI, entao a imagem final pode conter apenas o runtime Python e os assets compilados, sem um segundo container para servidor web estatico.
- Alternatives considered:
  - Usar dois containers, um para backend e outro para frontend. Rejeitada porque aumenta a orquestracao e contraria o requisito de imagem unica.
  - Adicionar Nginx dentro da mesma imagem para servir assets. Rejeitada porque o FastAPI ja atende o caso com menor complexidade operacional.
