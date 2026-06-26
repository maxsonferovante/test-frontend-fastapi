import { appConfig } from "@/lib/config"
import { HttpError } from "@/lib/http-errors"

export type Certificate = {
  id: string
  order_id: number
  product_id: number
  participant_name: string
  participant_email: string
  participant_document: string
  certificate_url: string | null
  created_at: string | null
  updated_at: string | null
  success: boolean
}

export type CertificateFilter = "all" | "success" | "failed"

export type CertificateSearchResponse = {
  email: string
  applied_filter: CertificateFilter
  total_count: number
  filtered_count: number
  has_success: boolean
  has_failed: boolean
  certificates: Certificate[]
}

export async function fetchCertificates(
  email: string,
  status: CertificateFilter,
): Promise<CertificateSearchResponse> {
  const url = new URL("/api/v1/certificates", appConfig.apiBaseUrl || window.location.origin)
  url.searchParams.set("email", email)
  url.searchParams.set("status", status)
  const response = await fetch(url)
  const payload = await response.json()
  if (!response.ok) {
    throw new HttpError(payload.message ?? "Unable to fetch certificates.", response.status, payload.code)
  }
  return payload as CertificateSearchResponse
}
