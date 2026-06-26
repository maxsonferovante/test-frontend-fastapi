import { useDeferredValue, useState, useTransition } from "react"

import {
  CertificateFilter,
  CertificateSearchResponse,
  fetchCertificates,
} from "@/lib/api"
import { HttpError } from "@/lib/http-errors"

const EMAIL_PATTERN = /^[^\s@]+@[^\s@]+\.[^\s@]+$/

export function useCertificateSearch() {
  const [email, setEmail] = useState("")
  const [emailError, setEmailError] = useState<string | undefined>()
  const [selectedFilter, setSelectedFilter] = useState<CertificateFilter>("all")
  const [rawData, setRawData] = useState<CertificateSearchResponse | null>(null)
  const [serverData, setServerData] = useState<CertificateSearchResponse | null>(null)
  const [requestError, setRequestError] = useState<string | undefined>()
  const [isPending, startTransition] = useTransition()
  const deferredData = useDeferredValue(serverData)

  const validateEmail = (value: string) => {
    if (!value) {
      return "Informe um email para continuar."
    }
    if (!EMAIL_PATTERN.test(value)) {
      return "Informe um email valido."
    }
    return undefined
  }

  const applyFilterLocally = (
    data: CertificateSearchResponse,
    nextFilter: CertificateFilter,
  ): CertificateSearchResponse => {
    const certificates =
      nextFilter === "all"
        ? data.certificates
        : data.certificates.filter((certificate) =>
            nextFilter === "success" ? certificate.success : !certificate.success,
          )
    return {
      ...data,
      applied_filter: nextFilter,
      filtered_count: certificates.length,
      certificates,
    }
  }

  const submit = () => {
    const validationError = validateEmail(email)
    setEmailError(validationError)
    if (validationError) {
      return
    }
    startTransition(async () => {
      try {
        setRequestError(undefined)
        const payload = await fetchCertificates(email, "all")
        setSelectedFilter("all")
        setRawData(payload)
        setServerData(payload)
      } catch (error) {
        const message =
          error instanceof HttpError ? error.message : "Tente novamente em instantes."
        setRequestError(message)
      }
    })
  }

  const changeFilter = (nextFilter: CertificateFilter) => {
    setSelectedFilter(nextFilter)
    if (rawData) {
      const sourcePayload = { ...rawData, certificates: [...rawData.certificates] }
      setServerData(
        applyFilterLocally(
          {
            ...sourcePayload,
            applied_filter: "all",
            filtered_count: sourcePayload.certificates.length,
            certificates: sourcePayload.certificates,
          },
          nextFilter,
        ),
      )
    }
  }

  return {
    email,
    setEmail,
    emailError,
    isLoading: isPending,
    requestError,
    selectedFilter,
    searchResult: deferredData,
    submit,
    changeFilter,
  }
}
