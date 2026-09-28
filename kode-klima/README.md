# kode-klima — overordnet web-UI

**KODE-klima** er brukernes inngang til hele anlegget: styring av de 10
undersystemene (regin/), smarthus-komponentene (smarthus/) og innsyn i
hovedanlegget (nilan/).

- Frontend: TypeScript + kompilert Svelte (norm «stack»), KODE15-profil
  (norm «web-profil», `raven-platform/webprofil-kode15/`)
- Backend: Rust; Python der det er hensiktsmessig
- Tilgang: 🔒 kun Tailscale / lokalt nett «Kode15»

Status: ikke påbegynt — spesifiseres i `handover/HANDOVER.md`.
