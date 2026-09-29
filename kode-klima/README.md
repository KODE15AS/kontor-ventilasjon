# kode-klima — overordnet web-UI

**KODE-klima** er brukernes inngang til hele anlegget: styring av de 10
undersystemene (regin/), smarthus-komponentene (smarthus/) og innsyn i
hovedanlegget (nilan/).

- Frontend: TypeScript + kompilert Svelte (norm «stack»), KODE15-profil
  (norm «web-profil», `raven-platform/webprofil-kode15/`)
- Backend: Rust; Python der det er hensiktsmessig
- Tilgang: 🔒 kun Tailscale / lokalt nett «Kode15»

Sonekartet `kontor-oversikt.svg` er mastertegningen for oversikten: SVG i
KODE15-profil der hver sone har `id="gruppe-N"` for kobling mot status og
styring i UI-et.

Status: sonekart-utkast på plass; UI ellers ikke påbegynt — spesifiseres i
`handover/HANDOVER.md`.
