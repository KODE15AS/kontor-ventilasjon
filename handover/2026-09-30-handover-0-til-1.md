# Handover 0 → 1

Chat 0 avsluttet 2026-09-30. Målbildet står i `HANDOVER.md`; dette er
tilstanden ved overlevering.

## Hvor vi står

Repo, struktur og dokumentasjon er etablert (se `HANDOVER.md` for
avkryssede punkter). De viktigste avklaringene fra chat 0:

- **NILAN:** VPR 560 med CTS 602i, åpen Modbus RTU
  (19200 baud, 8 databiter, Even paritet, 1 stoppbit, **slave 30**).
  Protokolldokument ligger i `nilan/dok/`. Driftshendelse 2026-09-28
  (c03 brannalarm etter åpnet serviceluke) er løst og loggført i
  `nilan/drift/`.
- **REGIN:** 10 soner med RCF-230CTD-EC (Modbus RTU slave over RS485).
  Anleggskonfigurasjonen (`regin/konfig/*.rtc`, ren INI) viser
  **slaveadresse 30** i alle soner. Regio Tool trengs ikke — alt styres
  over Modbus (`regin/dok/README.md`).
- **Kabeltopologi:** stjerne, IKKE buss — én Cat-kabel per REGIN til
  sonens varmebatteri (= koblingsboks med relé). Konsekvens: **én gateway
  per sone**. Veggboksen bak REGIN er opptatt (Finder-impulsrelé), så
  gateway plasseres ved varmebatteriet.
- **Sonepakken** (Dantherm-ordre 2021): Salda RS160EC-vifter (0–10 V),
  Salda EKA160-2,0 kanalbatterier, PT1000-følere, RCF-230CTD-EC —
  10 stk. av hver. Foto av fysisk installasjon: `regin/bilder/`.
- **Tegningsgrunnlag:** eksakt geometri-mal `kode-klima/kontor-mal.svg`
  generert fra CAD-original (DXF) med `kode-klima/verktoy/dxf-til-svg.py`.
  Gjenstår: sonemerker og etiketter oppå malen.

## Pågår (Jørn)

- Innkjøp av **2 stk. Elfin EW11A-0** (RS485-til-WiFi-gateway) for test
  mot NILAN og mot den løse test-REGIN-en («gruppe 10»).
- **USB-RS485-adapter finnes allerede:** Sentera CNVT-USB-RS485 (kjøpt
  2023, se `dok/README.md`). FTDI-basert — plugges rett i raven som
  `/dev/ttyUSB0`. Kan brukes til REGIN-test før Elfin-ene ankommer.

## ✅ Gjennombrudd sent i chat 0 (2026-09-30)

Test-REGIN gruppe 10 ble koblet til raven med USB-adapteren, og **hele
styringssløyfen er bevist** (se `regin/README.md`):

- Funnet med adresseskann: **adresse 247** (ikke 30!), 9600 8E1
- Lest live: romtemp, modus, viftetrinn, pådrag — verifisert mot display
- Skrevet: grunnsettpunkt (HR 284) og settpunkt-offset (HR 76), begge
  verifisert mot display og tilbakestilt (enheten står nøytralt:
  grunnsettpunkt 22,0, offset 0,0)
- Lært: display viser romtemp i hvile, settpunkt under justering;
  regulatoren har 2 °C dødbånd (varmesettpunkt = settpunkt − 1,0)
- Lokale skivejusteringer synlige umiddelbart over Modbus —
  KODE-klima kan være master med REGIN som utførende slave

## Neste steg (chat 1)

1. Elfin EW11A-0 ankommer: konfigurere (WiFi «Kode15», Modbus TCP↔RTU)
   og gjenta testen over WiFi mot test-REGIN.
2. Deretter test mot **NILAN CTS 602i** (19200 8E1, slave 30) — lese
   status/temperaturer før noe skrives.
3. Med fungerende kommunikasjon: Dockerfile og container i drift på
   RAVEN (norm «container»), backend-skjelett som leser begge.
4. Tegning: legge sonemerker (Gr. 1–9b) og Montserrat-etiketter på
   `kontor-mal.svg`, posisjonert etter `dok/omrader-og-grupper.md`.
