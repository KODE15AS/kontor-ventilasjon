# nilan — hovedventilasjonsanlegget

## Anlegget

- **Aggregat:** NILAN **VPR 560** (ordrebekreftelse 254142-2, levert juni 2020)
- **Styring:** **CTS 602i** HMI → Modbus RTU (adresse settes i servicemenyen,
  se softwareveiledningen)
- **Konfigurasjon:** høyre versjon, VTZ-kompressor (3×400 V), 14 kW
  el-ettervarme, rotorveksler (valgt i stedet for heatpipe), R407C
- **Reguleringsprinsipp:** avtrekksregulert — styrer mot AVTREKK-temperatur
  (snitt av returluft fra sonene); tilluft varierer mellom min/maks
- **Sommer/vinter-skift:** utetemperatur 12 °C (standard) styrer om anlegget
  får kjøre sommerverdier og kjøling

Dokumentasjon: se `dok/README.md`.

## Konkret problemstilling (fra e-posttråd med Nilan, mars 2025)

Styringslogikken passer dårlig for våre forhold og sløser energi:

- I AUTO: varmepumpa pøste inn 25 °C tilluft mens rommet holdt 23 °C
  (avtrekksføleren viste 21 °C — anlegget «så» et varmebehov).
- I KJØL: all luft går forbi varmevekslerne, utetemperatur rett inn,
  MIN tilluft ignoreres.
- Kompressoren kan ikke gå under 33 % hastighet; hysteresene rundt
  settpunktene gjør at anlegget går «litt over» før det stopper.

## Mål

1. **Operatørstøtte** for brukere/driftere.
2. **Agentstyring direkte over Modbus** — fysisk forbindelse fra raven til
   CTS 602i, med trygge grenser for skriving.

## Fysisk forbindelse — valgt kandidat (Jørn, 2026-09-29)

**Elfin EW11A-0** (Hi-Flying): RS485-til-WiFi seriellserver med innebygd
Modbus TCP ↔ RTU-oversetting. Verifisert av Jørn mot NILAN-aggregatet.

- Størrelse 61 × 26 × 17,8 mm (20 g) — får plass i Ø70 veggboks, og er
  dermed også kandidat for REGIN-sonene (se `../regin/`)
- Forsyning 5–36 VDC (A-varianten), ~200 mA / < 700 mW
- WiFi 802.11 b/g/n (2,4 GHz), STA/AP, WPA2, TLS 1.2; «-0» = ekstern antenne
- RS485 via RJ45: pinne 5 = A+, pinne 6 = B−; baud 300–230 400
- Konfigureres via innebygd webside eller IOTService

Oppsett mot CTS 602i: A+/B− til aggregatets Modbus-klemmer, seriell
19 200 baud / 8 databiter / even parity / 1 stoppbit, Modbus TCP-modus.
raven når aggregatet som Modbus TCP-klient over nettet (slaveadresse 30).

Avklares:

- Registerkart-detaljer: protokolldokument ligger i
  `dok/cts602-hmi350t-modbus-protokoll-v20-en.pdf`
- Trygge grenser for agent-skriving
