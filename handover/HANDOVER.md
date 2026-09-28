# HANDOVER — kontor-ventilasjon

Levende spesifikasjon (norm «handover»). Hvert punkt krysses av når det er
levert. Når alle punkter er levert, *er* dette prosjektdokumentasjonen.

## Oppsett

- [x] Repo opprettet på RAVEN under `~/dev/kontor-ventilasjon`
- [x] GitHub-repo `KODE15AS/kontor-ventilasjon` opprettet og koblet 1:1
- [x] Repo-struktur: `kode-klima/`, `nilan/`, `regin/`, `smarthus/`
- [ ] Dockerfile og container i drift på RAVEN

## Spesifikasjon

### KODE-klima (web-UI)

- [ ] Web-UI med tittel «KODE-klima», KODE15-profil, 🔒 kun Tailscale
- [ ] Styring av de 10 sonene (regin) fra UI-et
- [ ] Styring av smarthus-komponenter fra UI-et
- [ ] Innsyn i hovedanlegget (nilan)

### nilan (hovedanlegg)

- [ ] NILAN-modell og styringsenhet identifisert (dokumentasjon fra Jørn)
- [ ] Fysisk Modbus-forbindelse raven ↔ NILAN etablert
- [ ] Operatørstøtte for brukere
- [ ] Agentstyring over Modbus med trygge grenser

### regin (10 soner)

- [ ] Navneliste for de 10 sonene
- [ ] ESP32 montert per sone, fjernstyring over WiFi «Kode15»
- [ ] Soner styrbare fra KODE-klima

### smarthus

- [ ] Inventar per sone (Mill WiFi-ovner m.m.)
- [ ] Mill-integrasjon (sky-API eller lokal)
- [ ] Matter-støtte vurdert

### Energioptimalisering (ambisjon)

- [ ] Agent som kontinuerlig optimaliserer komfort vs. energiforbruk
- [ ] Værvarsel fra yr.no-API som beslutningsgrunnlag (eks.: utsett kjøling
      når kvelden blir kald nok til gratis nedkjøling)

## Åpne spørsmål (vurderes per handover)

- **Container-deling (norm «container»):** starter som ett repo / én
  container; splitting i flere repoer vurderes i hver handover.
- **Sikkerhetsstrategi for agent-skriving** til fysisk anlegg (trygt bånd
  vs. norm «bestilling»): Jørn har strategier på gang — kommer.
- **NILAN-dokumentasjon:** lastes opp av Jørn.
- **Sonenavn:** navneliste tas senere.
