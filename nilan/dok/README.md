# Dokumentregister — nilan

Kilde: Jørns Dropbox (`…\547 Sagveien 15 Vest\50 Leverandører\Nilan aggregater\`),
overført til repoet 2026-09-28.

| Fil | Innhold |
|---|---|
| `2019-09-cts602i-softwareveiledning-vpm-vpr-dk.pdf` | Nilans softwareveiledning for CTS602i HMI, VPM/VPR 120-2200 (dansk, v3.00, 36 s.). Dekker bl.a. kjøling, nattkjøling, temperaturregulering, tilluftkontroll, romtemperaturkontroll og Modbus-adresse. |
| `2020-03-13-ordrebekreftelse-vpr560.pdf` | Ordrebekreftelse 254142-2 fra Nilan Norge: **VPR 560 enhetsaggregat** med **CTS 602i**, høyre versjon, VTZ-kompressor (3×400 V), 14 kW el-batteri, rotor i stedet for heatpipe, trykktransmittere. Levert juni 2020. |
| `2020-03-jorn-notater-bestilling-skannet.pdf` | Jørns håndnotater fra bestillingen (skannede bilder, ikke søkbar tekst). |
| `2024-05-brukeranvisning-display-kode15.pdf` | Jørns egen brukeranvisning for displayet (rev 1): anlegget regulerer på AVTREKK-temperatur (snitt av retur fra sonene), kjøling starter ved hovedsetpunkt + kjølesetpunkt. Inneholder ubesvarte spørsmål til Nilan om tolkning av settpunktene. |
| `2024-11-20-epost-nilan-brukerveiledning.pdf` | E-posttråd med Morten Daniel Olsen (Nilan): oversendelse av veiledning + samme tråd som energiforbruk-e-posten. |
| `2025-03-24-epost-nilan-energiforbruk.pdf` | E-posttråd mars 2025 om styringsproblemet: anlegget varmet (25 °C tilluft) ved 23 °C romtemp i AUTO; KJØL-modus sendte utetemperatur rett inn og ignorerte MIN tilluft. Nilans forklaring: avtrekksregulering, sommer/vinter-skift ved 12 °C ute, kompressor min. 33 % hastighet, hysterese rundt settpunkter. |
| `vpm-120-560-produktdata-no.pdf` | Nilan produktdata VPM 120–560-serien (norsk, M1331NO): aggregater med aktiv varmegjenvinning for næring — teknisk grunnlag for vårt VPR 560 |
| `2023-01-14-fdv-vpr560-elektrisk-komponentliste.pdf` | **Elektrisk FDV for VPR560 m/CTS602i** (varenr. 78125, skannet): prinsippdiagram, forsynings- og kompressorskjemaer (FC302 frekvensomformer m.m.) og komponentliste. Tegninger datert 26/08-2020. |
| `prh-trykkregulator-datablad-en.pdf` | **OJ Electronics PRH-1212** konstanttrykkregulator — datablad |
| `prh-trykkregulator-manual-57407a.pdf` | PRH instruksjoner 57407A (08/12, da/no/sv/en/de) |
| `pth-3202-dr-manual-67546g-en.pdf` | **OJ PTH-3202-DR** trykktransmitter — instruksjoner 67546G (04/21) med menyskjema og plasseringskrav |
| `pth-3202-miljodeklarasjon-oj.pdf` | OJ miljø-/materialdeklarasjon PTH-3202/3502 (2022) |

## Nøkkelfakta PRH (dp-holding av manifoldene, se `../../dok/primaer-sekundaer-dp-regulering.md`)

- PRH er en **selvstendig elektronisk regulator**, ikke en dum boks:
  PTH måler dp (0–10 V inn), PRH justerer vifta direkte med 0–10 V ut
  til målt trykk = settpunkt. Settpunkt stilles på enheten
  (dag 10–200 Pa; vårt anlegg: +80/−80 Pa).
- **Nattsenk-inngang:** potensialfri kontakt (aktiv høy, intern pull-up
  3,3 kΩ) aktiverer et eget **natt-settpunkt (30–600 Pa)** — designet
  for ekstern tidsstyring. Dette er fjernstyringsveien: et relé styrt
  fra raven gir to dp-nivåer per PRH.
- **BMS-utgang 4–20 mA** med målt trykk — kan leses av ekstern ADC for
  kontinuerlig dp-overvåking uten å røre reguleringen.
- **Alarmrelé** (SPDT): aktivt ved trykkavvik utenfor alarmgrenser,
  motorfeil eller bortfall av 230 V.
- Innebygd utetemperatur-kompensering (NTC-føler) finnes også, f.eks.
  −25 Pa mellom +15 og −10 °C ute.
