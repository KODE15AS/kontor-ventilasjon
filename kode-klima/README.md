# kode-klima — overordnet web-UI

**KODE-klima** er brukernes inngang til hele anlegget: styring av de 10
undersystemene (regin/), smarthus-komponentene (smarthus/) og innsyn i
hovedanlegget (nilan/).

- Frontend: TypeScript + kompilert Svelte (norm «stack»), KODE15-profil
  (norm «web-profil», `raven-platform/webprofil-kode15/`)
- Backend: Rust; Python der det er hensiktsmessig
- Tilgang: 🔒 kun Tailscale / lokalt nett «Kode15»

Tegningsgrunnlag:

- `kontor-mal.svg` — ren geometri-mal, generert eksakt fra CAD-originalen
  `../dok/2026-09-30-kontor-layout.dxf` med `verktoy/dxf-til-svg.py` (kun
  lagene `0` og `1-YTTERGEOMETRI`; KODE15-farger, uten tekst). Dette er
  malen det bygges videre på med sonemerker og etiketter.
- `kontor-oversikt.svg` — tidligere utkast (rastersporing fra PDF),
  erstattes av mal + tekstlag.

Sonene får `id="gruppe-N"` for kobling mot status og styring i UI-et
(kryssreferanse i `../dok/omrader-og-grupper.md`).

Status: geometri-mal på plass; UI ellers ikke påbegynt — spesifiseres i
`handover/HANDOVER.md`.
