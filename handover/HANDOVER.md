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
- [x] Geometri-mal for plantegning: `kode-klima/kontor-mal.svg`, generert
      eksakt fra CAD-original (DXF) med `kode-klima/verktoy/dxf-til-svg.py`
      — gjenstår: sonemerker og etiketter oppå malen
- [ ] Styring av de 10 sonene (regin) fra UI-et
- [ ] Styring av smarthus-komponenter fra UI-et
- [ ] Innsyn i hovedanlegget (nilan)

### nilan (hovedanlegg)

- [x] NILAN-modell og styringsenhet identifisert: VPR 560 med CTS 602i
      (Modbus RTU) — se `nilan/README.md` og `nilan/dok/`
- [ ] Fysisk Modbus-forbindelse raven ↔ NILAN etablert
      (Elfin EW11A-0 valgt 2026-09-29; **innkjøp av 2 stk. pågår
      2026-09-30** for test mot NILAN og test-REGIN — gjenstår:
      montering, konfigurasjon)
- [ ] Operatørstøtte for brukere
- [ ] Agentstyring over Modbus med trygge grenser

### regin (10 soner)

- [x] Regulator identifisert: Regin RCF-230CTD-EC med innebygd Modbus RTU
      over RS485 (skjema 54740T390-2), se `regin/dok/`
- [x] Kabeltopologi avklart 2026-09-30: Cat-kablene er IKKE felles buss,
      men stjerne — én signalkabel per REGIN til sonens varmebatteri
      (fungerer som koblingsboks/-skap). Fjernstyring krever gateway per
      sone; arbeidshypotese Elfin EW11A-0 i Ø70 veggboks.
- [x] **Første Modbus-kontakt 2026-09-30:** test-REGIN (gruppe 10) lest
      via USB-RS485 på raven — adresse 247, 9600 8E1, pymodbus.
      Se `regin/README.md`
- [x] **Skrivetest 2026-09-30:** settpunkt endret og tilbakestilt over
      Modbus — full styringssløyfe bevist, KODE-klima kan være master
- [ ] Endelig gateway-valg og plassering per sone
- [ ] Modbus-adresser (ELA) kartlagt per sone (driftssatte soner antatt
      adresse 30 per konfigmalen — må verifiseres)
- [ ] Soner styrbare fra KODE-klima

### smarthus

- [ ] Inventar per sone (Mill WiFi-ovner m.m.)
- [ ] Mill-integrasjon (sky-API eller lokal)
- [ ] Matter-støtte vurdert

### Energioptimalisering (ambisjon)

- [ ] Agent som kontinuerlig optimaliserer komfort vs. energiforbruk
- [ ] Værvarsel fra yr.no-API som beslutningsgrunnlag (eks.: utsett kjøling
      når kvelden blir kald nok til gratis nedkjøling)

### Systemarkitektur

- [x] **Krysningspunkt NILAN ↔ REGIN avklart 2026-09-30:** primærkrets
      (NILAN) holder manifoldene på konstant dp (+80/−80 Pa, PRH-
      regulatorer med P1/P2-transmittere); sekundærkrets (REGIN-sonene)
      trekker fritt fra manifoldene. Se
      `dok/primaer-sekundaer-dp-regulering.md`
- [ ] PRH- og PTH-dokumentasjon arkiveres (Jørn laster opp)
- [ ] dp-settpunktene er manuelle i dag — vurdere fjernavlesning/
      -styring for energioptimalisering

## Åpne spørsmål (vurderes per handover)

- **Container-deling (norm «container»):** starter som ett repo / én
  container; splitting i flere repoer vurderes i hver handover.
- **Sikkerhetsstrategi for agent-skriving** til fysisk anlegg (trygt bånd
  vs. norm «bestilling»): Jørn har strategier på gang — kommer.
- ~~9 eller 10 soner?~~ **Avklart 2026-09-29:** 10 REGIN-regulatorer i
  drift (gruppe 1–8 + 9a + 9b); NILAN ser 9 avtrekkssoner (1–9). I tillegg
  finnes en løs test-REGIN («gruppe 10») for kommunikasjonstesting.
  Se `dok/omrader-og-grupper.md`.
- **Sonenavn:** gruppenummer ↔ områdenavn er på plass i
  `dok/omrader-og-grupper.md`.
- **Modbus-registerkart for CTS602:** protokolldokument må skaffes fra Nilan.
