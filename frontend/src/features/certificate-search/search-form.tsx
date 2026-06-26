import {
  Button,
  Field,
  HStack,
  Input,
  Stack,
} from "@chakra-ui/react"

type SearchFormProps = {
  email: string
  error?: string
  isLoading: boolean
  onEmailChange: (value: string) => void
  onSubmit: () => void
}

export function SearchForm({
  email,
  error,
  isLoading,
  onEmailChange,
  onSubmit,
}: SearchFormProps) {
  return (
    <Stack gap={4}>
      <Field.Root invalid={Boolean(error)} required>
        <Field.Label>Buscar certificados por email</Field.Label>
        <Input
          type="email"
          value={email}
          placeholder="voce@empresa.com"
          onChange={(event) => onEmailChange(event.target.value)}
          disabled={isLoading}
          bg="white"
          borderColor="rgba(148, 163, 184, 0.35)"
          size="lg"
        />
        <Field.ErrorText>{error}</Field.ErrorText>
      </Field.Root>
      <HStack justify="space-between" align="center">
        <Button
          colorPalette="teal"
          size="lg"
          disabled={isLoading}
          onClick={onSubmit}
        >
          {isLoading ? "Consultando..." : "Buscar certificados"}
        </Button>
      </HStack>
    </Stack>
  )
}
