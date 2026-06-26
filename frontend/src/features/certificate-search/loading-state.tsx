import { Box, Spinner, Stack, Text } from "@chakra-ui/react"

export function LoadingState() {
  return (
    <Box bg="whiteAlpha.900" borderRadius="2xl" p={10}>
      <Stack direction={{ base: "column", md: "row" }} gap={4} align="center">
        <Spinner color="teal.500" size="lg" />
        <Text color="gray.700">Consultando certificados...</Text>
      </Stack>
    </Box>
  )
}
