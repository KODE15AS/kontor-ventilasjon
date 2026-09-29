# kontor-ventilasjon

Samlet område for ventilasjon og energistyring for kontorfellesskapet
**KODE15**. Overordnet web-UI heter **KODE-klima** og er kun tilgjengelig
internt (Tailscale / lokalt nett «Kode15»).

## Lenker

| Hva | Tilgang | URL |
|---|---|---|
| KODE-klima (web-UI) | 🔒 Kun Tailscale | (kommer — settes ved første deploy) |
| Dette repoet på GitHub | 🌐 Offentlig (krever innlogging) | https://github.com/KODE15AS/kontor-ventilasjon |

🌐 Offentlig — kan nås fra internett. 🔒 Kun Tailscale — kun internt.

## Struktur

Felles dokumentasjon ligger i `dok/`: plantegning og **kryssreferansen
områdenavn ↔ gruppenummer ↔ byggfasenavn** (`dok/omrader-og-grupper.md`) som
er nøkkelen til all byggefase-dokumentasjon.

Repoet er delt i ett overordnet UI og tre fysiske integrasjonslag:

- `kode-klima/` — overordnet web-UI for brukerne (KODE15-profil,
  Svelte/TypeScript + Rust-backend etter norm «stack»)
- `nilan/` — hovedventilasjonsanlegget (fabrikat NILAN): operatørstøtte og
  agentstyring direkte over Modbus
- `regin/` — 10 distinkte undersystemer, hver styrt av én REGIN 230 CTD EC
  som fjernstyres via påmontert ESP32 over WiFi
- `smarthus/` — smarthus-komponenter per undersystem (primært Mill
  WiFi-varmeovner, senere Matter m.m.)

Spesifikasjonen bygges i `handover/HANDOVER.md` (norm «handover»).

## Ambisjon

En agent som kontinuerlig optimaliserer styringsstrategier for best mulig
komfort med minst mulig energiforbruk. Eksempel: på en varm dag utsettes
energikrevende kjøling etter kl. 15:30 dersom værvarselet (yr.no-API) viser
at utetemperaturen faller om kvelden — da brukes natten til gratis nedkjøling
og optimalisering mot komforttemperatur neste dag.
