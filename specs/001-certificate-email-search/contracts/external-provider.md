# External Provider Contract

## Endpoint

- Method: `GET`
- URL pattern: `https://SUA_URL_AQUI/dev/api/v1/users/{email}/certificates`
- Required header: `x-api-key: <secret>`

## Expected Response Shape

```json
{
  "email": "teste@gmail.com",
  "certificates": [
    {
      "id": "060d543f-7c44-4370-97c6-ca54cae0bfc2",
      "order_id": 3340,
      "product_id": 3336,
      "participant_name": "Maxson Almeida",
      "participant_email": "teste@gmail.com",
      "participant_document": "",
      "certificate_url": "https://SUA_URL_AQUI/dev/api/v1/certificate/download?id=060d543f-7c44-4370-97c6-ca54cae0bfc2",
      "created_at": "2025-12-06T17:57:07.693972",
      "updated_at": "2025-12-06T17:57:07.693972",
      "success": true
    },
    {
      "id": "b21c7fc8-ed52-4ee8-8267-3b01fdbc7c59",
      "order_id": 3272,
      "product_id": 316,
      "participant_name": "Maxson Almeida Ferovante",
      "participant_email": "teste@gmail.com",
      "participant_document": "",
      "certificate_url": null,
      "created_at": null,
      "updated_at": null,
      "success": false
    }
  ]
}
```

## Mapping Rules

- `email` da resposta externa alimenta `email` da resposta interna.
- `certificates` e filtrado internamente conforme `status`.
- `success=true` mapeia para filtro `success`.
- `success=false` mapeia para filtro `failed`.
- `certificate_url`, `created_at` e `updated_at` aceitam `null`.

## Failure Handling

- Timeout, indisponibilidade de rede ou resposta invalida do provedor devem ser traduzidos pelo backend para erro interno sem vazar a chave da API.
- O backend deve registrar contexto suficiente para diagnostico, sem logar o valor bruto de `x-api-key`.
