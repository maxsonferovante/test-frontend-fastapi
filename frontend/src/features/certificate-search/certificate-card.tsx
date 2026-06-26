import { Badge, Box, Button, HStack, Stack, Text } from "@chakra-ui/react"

import { Certificate } from "@/lib/api"

type CertificateCardProps = {
  certificate: Certificate
}

export function CertificateCard({ certificate }: CertificateCardProps) {
  return (
    <Box
      bg="whiteAlpha.900"
      border="1px solid"
      borderColor="rgba(148, 163, 184, 0.25)"
      borderRadius="2xl"
      p={5}
      boxShadow="sm"
    >
      <Stack gap={4}>
        <HStack justify="space-between" align="start">
          <Stack gap={1}>
            <Text fontSize="lg" fontWeight="semibold" color="gray.800">
              {certificate.participant_name}
            </Text>
            <Text color="gray.600">{certificate.participant_email}</Text>
          </Stack>
          <Badge colorPalette={certificate.success ? "green" : "orange"}>
            {certificate.success ? "Sucesso" : "Sem sucesso"}
          </Badge>
        </HStack>
        <HStack wrap="wrap" gap={4} color="gray.600">
          <Text>Pedido #{certificate.order_id}</Text>
          <Text>Produto #{certificate.product_id}</Text>
        </HStack>
        <Text color="gray.500">
          Criado em: {certificate.created_at ?? "nao disponivel"}
        </Text>
        {certificate.certificate_url ? (
          <Button
            asChild
            colorPalette="teal"
            variant="subtle"
            width={{ base: "full", md: "fit-content" }}
          >
            <a href={certificate.certificate_url} target="_blank" rel="noreferrer">
              Abrir certificado
            </a>
          </Button>
        ) : (
          <Text color="orange.700">Certificado ainda nao disponivel para download.</Text>
        )}
      </Stack>
    </Box>
  )
}
