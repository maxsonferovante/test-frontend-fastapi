import { Stack } from "@chakra-ui/react"

import { CertificateList } from "@/features/certificate-search/certificate-list"
import { EmptyState } from "@/features/certificate-search/empty-state"
import { ErrorState } from "@/features/certificate-search/error-state"
import { FilterTabs } from "@/features/certificate-search/filter-tabs"
import { LoadingState } from "@/features/certificate-search/loading-state"
import { ResultsSummary } from "@/features/certificate-search/results-summary"
import { CertificateFilter, CertificateSearchResponse } from "@/lib/api"

type SearchResultsPanelProps = {
  isLoading: boolean
  requestError?: string
  selectedFilter: CertificateFilter
  result: CertificateSearchResponse | null
  onRetry: () => void
  onFilterChange: (filter: CertificateFilter) => void
}

export function SearchResultsPanel({
  isLoading,
  requestError,
  selectedFilter,
  result,
  onRetry,
  onFilterChange,
}: SearchResultsPanelProps) {
  if (isLoading) {
    return <LoadingState />
  }

  if (requestError) {
    return <ErrorState message={requestError} onRetry={onRetry} />
  }

  if (!result) {
    return (
      <EmptyState
        title="Faça sua primeira consulta"
        description="Informe um email acima para localizar certificados e analisar os resultados."
      />
    )
  }

  if (result.total_count === 0) {
    return (
      <EmptyState
        title="Nenhum certificado encontrado"
        description="O email informado nao possui certificados associados neste momento."
      />
    )
  }

  if (result.filtered_count === 0) {
    return (
      <Stack gap={5}>
        <FilterTabs activeFilter={selectedFilter} onFilterChange={onFilterChange} />
        <ResultsSummary
          totalCount={result.total_count}
          filteredCount={result.filtered_count}
          hasSuccess={result.has_success}
          hasFailed={result.has_failed}
        />
        <EmptyState
          title="Nenhum certificado neste filtro"
          description="Altere o filtro para ver outros resultados da busca atual."
        />
      </Stack>
    )
  }

  return (
    <Stack gap={5}>
      <FilterTabs activeFilter={selectedFilter} onFilterChange={onFilterChange} />
      <ResultsSummary
        totalCount={result.total_count}
        filteredCount={result.filtered_count}
        hasSuccess={result.has_success}
        hasFailed={result.has_failed}
      />
      <CertificateList certificates={result.certificates} />
    </Stack>
  )
}
