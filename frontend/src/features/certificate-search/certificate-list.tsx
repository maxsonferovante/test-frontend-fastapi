import { SimpleGrid } from "@chakra-ui/react"

import { CertificateCard } from "@/features/certificate-search/certificate-card"
import { Certificate } from "@/lib/api"

type CertificateListProps = {
  certificates: Certificate[]
}

export function CertificateList({ certificates }: CertificateListProps) {
  return (
    <SimpleGrid columns={{ base: 1, xl: 2 }} gap={5}>
      {certificates.map((certificate) => (
        <CertificateCard key={certificate.id} certificate={certificate} />
      ))}
    </SimpleGrid>
  )
}
