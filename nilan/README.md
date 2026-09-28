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

Avklares:

- Fysisk vei: USB-til-RS485-adapter, Modbus TCP-gateway eller annet
- Registerkart for CTS602 (Modbus-protokolldokument fra Nilan)
- Trygge grenser for agent-skriving
