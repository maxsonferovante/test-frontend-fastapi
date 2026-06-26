import { Box, Stack, Text } from "@chakra-ui/react"

type EmptyStateProps = {
  title: string
  description: string
}

export function EmptyState({ title, description }: EmptyStateProps) {
  return (
    <Box
      bg="whiteAlpha.900"
      border="1px dashed"
      borderColor="rgba(148, 163, 184, 0.35)"
      borderRadius="2xl"
      p={10}
    >
      <Stack gap={3}>
        <Text fontSize="xl" fontWeight="semibold">
          {title}
        </Text>
        <Text color="gray.600">{description}</Text>
      </Stack>
    </Box>
  )
}
