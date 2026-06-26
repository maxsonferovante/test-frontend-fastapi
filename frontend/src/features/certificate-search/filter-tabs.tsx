import { Button, HStack } from "@chakra-ui/react"

import { CertificateFilter } from "@/lib/api"

const filters: Array<{ label: string; value: CertificateFilter }> = [
  { label: "Todos", value: "all" },
  { label: "Sucesso", value: "success" },
  { label: "Sem sucesso", value: "failed" },
]

type FilterTabsProps = {
  activeFilter: CertificateFilter
  onFilterChange: (value: CertificateFilter) => void
}

export function FilterTabs({ activeFilter, onFilterChange }: FilterTabsProps) {
  return (
    <HStack gap={3} wrap="wrap">
      {filters.map((filter) => (
        <Button
          key={filter.value}
          variant={activeFilter === filter.value ? "solid" : "outline"}
          colorPalette="teal"
          onClick={() => onFilterChange(filter.value)}
        >
          {filter.label}
        </Button>
      ))}
    </HStack>
  )
}
