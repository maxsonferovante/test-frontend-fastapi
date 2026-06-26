import { Box, Button, Stack, Text } from "@chakra-ui/react"

type ErrorStateProps = {
  message: string
  onRetry: () => void
}

export function ErrorState({ message, onRetry }: ErrorStateProps) {
  return (
    <Box bg="red.50" border="1px solid" borderColor="red.200" borderRadius="2xl" p={8}>
      <Stack gap={4}>
        <Text fontWeight="semibold" color="red.700">
          Nao foi possivel concluir a consulta.
        </Text>
        <Text color="red.600">{message}</Text>
        <Button colorPalette="red" variant="outline" onClick={onRetry} width="fit-content">
          Tentar novamente
        </Button>
      </Stack>
    </Box>
  )
}
