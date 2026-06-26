import { Box, Container, Heading, Stack, Text } from "@chakra-ui/react"

import { SearchForm } from "@/features/certificate-search/search-form"
import { SearchResultsPanel } from "@/features/certificate-search/search-results-panel"
import { useCertificateSearch } from "@/features/certificate-search/use-certificate-search"

export function HomeRoute() {
  const search = useCertificateSearch()

  return (
    <Box minH="100vh" bg="linear-gradient(135deg, #f8fafc 0%, #dff4ef 45%, #fef3c7 100%)">
      <Container maxW="container.xl" py={{ base: 10, md: 16 }}>
        <Stack gap={8}>
          <Stack gap={3} maxW="3xl">
            <Text
              width="fit-content"
              px={3}
              py={1}
              rounded="full"
              bg="whiteAlpha.700"
              color="teal.700"
              fontWeight="semibold"
            >
              Certificate Search Control Room
            </Text>
            <Heading fontSize={{ base: "4xl", md: "6xl" }} lineHeight="1">
              Consulte certificados por email e isole o que deu certo ou nao.
            </Heading>
            <Text color="gray.700" fontSize={{ base: "md", md: "lg" }}>
              Uma interface unica para localizar certificados, entender falhas e abrir os
              comprovantes disponiveis sem expor a integracao externa ao navegador.
            </Text>
          </Stack>

          <Box
            bg="rgba(255,255,255,0.78)"
            backdropFilter="blur(18px)"
            border="1px solid rgba(255,255,255,0.45)"
            borderRadius="3xl"
            p={{ base: 6, md: 8 }}
            boxShadow="0 30px 80px rgba(15, 23, 42, 0.12)"
          >
            <Stack gap={8}>
              <SearchForm
                email={search.email}
                error={search.emailError}
                isLoading={search.isLoading}
                onEmailChange={search.setEmail}
                onSubmit={search.submit}
              />
              <SearchResultsPanel
                isLoading={search.isLoading}
                requestError={search.requestError}
                selectedFilter={search.selectedFilter}
                result={search.searchResult}
                onRetry={search.submit}
                onFilterChange={search.changeFilter}
              />
            </Stack>
          </Box>
        </Stack>
      </Container>
    </Box>
  )
}
