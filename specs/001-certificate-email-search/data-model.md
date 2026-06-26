# Data Model: Listagem de Certificados por Email

## Overview

O modelo de dados da feature e majoritariamente de leitura. O backend recebe uma resposta externa, normaliza os campos necessarios e devolve uma representacao estavel para o frontend.

## Entities

### CertificateSearchRequest

- Purpose: representar a solicitacao de busca iniciada pela usuaria.
- Fields:
  - `email`: email informado para consulta.
  - `status_filter`: `all`, `success` ou `failed`.
- Validation Rules:
  - `email` deve ter formato valido.
  - `status_filter` deve aceitar apenas valores previstos.

### CertificateRecord

- Purpose: representar um certificado retornado pela API externa e exposto pela API interna.
- Fields:
  - `id`: UUID do certificado.
  - `order_id`: identificador numerico do pedido.
  - `product_id`: identificador numerico do produto.
  - `participant_name`: nome exibivel do participante.
  - `participant_email`: email do participante.
  - `participant_document`: documento do participante, possivelmente vazio.
  - `certificate_url`: URL para download quando existir.
  - `created_at`: data/hora de criacao do certificado, podendo ser nula.
  - `updated_at`: data/hora de atualizacao do certificado, podendo ser nula.
  - `success`: indicador booleano de emissao bem-sucedida.
- Validation Rules:
  - `id` e obrigatorio.
  - `participant_email` deve corresponder ao email retornado pela consulta ou ser tratado como inconsistência de integracao.
  - `certificate_url` pode ser nulo apenas para certificados sem sucesso ou indisponiveis.
  - `created_at` e `updated_at` aceitam `null`.

### CertificateSearchResult

- Purpose: representar a resposta consolidada da busca para a UI.
- Fields:
  - `email`: email consultado.
  - `applied_filter`: filtro aplicado na resposta interna.
  - `total_count`: quantidade total de certificados retornados pelo provedor.
  - `filtered_count`: quantidade apos aplicacao do filtro.
  - `certificates`: lista de `CertificateRecord`.
  - `has_success`: indica se existe ao menos um certificado com sucesso.
  - `has_failed`: indica se existe ao menos um certificado sem sucesso.
- Validation Rules:
  - `filtered_count` deve refletir exatamente o tamanho de `certificates`.
  - `filtered_count` nunca pode ser maior que `total_count`.

### ApplicationDistributionPackage

- Purpose: representar a unidade operacional usada para distribuir a aplicacao completa.
- Fields:
  - `delivery_type`: identificador do formato de entrega adotado pela equipe.
  - `contains_backend`: indica que o servico HTTP interno faz parte do pacote.
  - `contains_frontend_assets`: indica que os assets compilados da interface fazem parte do pacote.
  - `startup_entrypoint`: comando principal de inicializacao do pacote.
  - `exposed_port`: porta HTTP disponibilizada para acesso da aplicacao.
- Validation Rules:
  - `delivery_type` deve identificar um unico artefato distribuivel.
  - `contains_backend` e `contains_frontend_assets` devem permanecer verdadeiros para cumprir o requisito de entrega completa.
  - `startup_entrypoint` deve iniciar a aplicacao sem dependencia de processo operacional separado para frontend.

### ExternalProviderResponse

- Purpose: espelhar a resposta recebida do provedor externo para fins de mapeamento de integracao.
- Fields:
  - `email`
  - `certificates[]`
- Validation Rules:
  - O backend deve tratar payload ausente, campos inesperados e tipos invalidos como falha de integracao.

## Relationships

- `CertificateSearchRequest` produz um `CertificateSearchResult`.
- `CertificateSearchResult` contem zero ou muitos `CertificateRecord`.
- `ExternalProviderResponse` e transformado em `CertificateSearchResult`.
- `ApplicationDistributionPackage` encapsula a entrega operacional do backend e dos assets do frontend para disponibilizar `CertificateSearchResult` pela interface web.

## State Transitions

### Search UI State

- `idle` -> estado inicial, sem busca executada.
- `loading` -> busca em andamento para um email valido.
- `success_with_results` -> busca concluida com um ou mais certificados.
- `success_empty` -> busca concluida sem certificados.
- `error` -> falha de validacao ou erro operacional.

### Certificate Outcome State

- `success=true` -> certificado emitido com URL de download potencialmente disponivel.
- `success=false` -> certificado nao emitido ou indisponivel; URL pode ser nula.

### Distribution Package State

- `build_pending` -> artefato unico ainda nao gerado.
- `built` -> pacote pronto para distribuicao com backend e frontend incorporados.
- `running` -> pacote iniciado e servindo a SPA e a API interna pelo mesmo fluxo de inicializacao.
