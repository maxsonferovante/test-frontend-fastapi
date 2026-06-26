import { Badge, HStack, Text } from "@chakra-ui/react"

type ResultsSummaryProps = {
  totalCount: number
  filteredCount: number
  hasSuccess: boolean
  hasFailed: boolean
}

export function ResultsSummary({
  totalCount,
  filteredCount,
  hasSuccess,
  hasFailed,
}: ResultsSummaryProps) {
  return (
    <HStack justify="space-between" wrap="wrap" gap={3}>
      <Text color="fg.muted">
        Exibindo {filteredCount} de {totalCount} certificados encontrados.
      </Text>
      <HStack gap={2}>
        {hasSuccess ? <Badge colorPalette="green">Com sucesso</Badge> : null}
        {hasFailed ? <Badge colorPalette="orange">Sem sucesso</Badge> : null}
      </HStack>
    </HStack>
  )
}
