# Primærkrets, sekundærkrets og dp-regulering

**Krysningspunktet mellom NILAN (primærkrets) og REGIN (sekundærkrets)**
er de to manifoldene i ventilasjonsrommet, som holdes på konstant
differansetrykk. Foto med nummererte punkter:
`2026-09-30-primaer-sekundaer-dp-oversikt.jpg` (Jørn, 2026-09-30).

## Systemprinsipp

- **Primærkrets (NILAN):** aggregatet leverer tilluft til en
  TILLUFT-manifold og henter returluft fra en FRALUFT-manifold.
  Aggregatet regulerer mot **konstant differansetrykk** mellom rom
  (ambient) og manifold: normalt **+80 Pa** på tilluft (Q2/P2) og
  **−80 Pa** på fraluft (Q1/P1).
- **Sekundærkrets (REGIN):** hver av de 10 sonene (gruppe 1–8, 9a, 9b)
  har egen Salda-vifte + varmebatteri som trekker luft fra
  tilluft-manifolden og leverer til sin gruppe; returen går til
  fraluft-manifolden.
- **Poenget med dp-reguleringen:** manifoldene fungerer som trykksatte
  «reservoarer» som frikobler kretsene. Sonene kan variere sin luftmengde
  uavhengig av hverandre — NILAN kompenserer automatisk for samlet
  uttak ved å holde dp konstant.

## Punktene på fotoet

| Nr | Hva |
|---|---|
| 1 | NILAN-aggregatet (VPR 560) |
| 2 | Salda vifte+varmebatteri (10 stk.) som trekker fra TILLUFT-manifolden — 9a og 9b er begge gruppe 9 (Møteområdet), derfor 10 |
| 3 | FRALUFT-manifold for returluft fra de 9 gruppene tilbake til aggregatet |
| 4, 5 | Trykkregulatorer **PRH** — føler dp mellom ambient og hhv. TILLUFT- og FRALUFT-manifold. Innstilling normalt +80 Pa tilluft (Q2/P2), −80 Pa fraluft (Q1/P1) |
| 6, 7 | Trykktransmittere P2 og P1 |
| 8, 9 | dp-målepunktene på selve kanalen |

## Viktig for styring og energioptimalisering

dp er den sentrale koblingsparameteren mellom kretsene: lavere dp =
mindre vifteenergi i primærkretsen, men mindre tilgjengelig trykk for
sonene.

## Valgt plan (2026-09-30): dp-kontrolleren

Vi bygger en **liten kontroller ved aggregatet** som gir agenten på
raven:

- **dp TILLUFT og dp FRALUFT** kontinuerlig, lest fra PRH-enes
  BMS-utganger (4–20 mA med målt trykk) — uinvasivt, reguleringen
  røres ikke
- **Veksling mellom to settpunkt per PRH, uavhengig av hverandre**, via
  PRH-enes nattsenk-innganger (potensialfri kontakt, laget for ekstern
  styring): dag-settpunkt (80 Pa) og natt-settpunkt (stilles én gang
  manuelt på PRH)
- **Trinnvis modulering av dag-settpunktet** via PRH-ens
  temperaturkompensering (oppdaget 2026-09-30): PRH justerer
  dag-settpunktet etter en NTC-uteføler (ETF-serien), med
  konfigurerbart maks (vindu 0/+30 °C) og min (−20/0 °C) — f.eks.
  −25 Pa over båndet. Agenten **emulerer føleren med en motstandsstige
  koblet via reléer** på I/O-modulen: 4 reléer i binær stige gir 16
  «utetemperaturer» = 16 dp-trinn innenfor kompensasjonsbåndet. PRH
  aner ingenting — reguleringen er urørt.

Maskinvarelinje: **Elfin EW11A-0** (samme gateway-type som ellers i
anlegget — erstatter tidligere ESP32-tanke). Elfin er en transparent
RS485↔WiFi-gateway uten egen I/O, så kontrolleren realiseres med en
**Modbus RTU I/O-modul** (2× analog inngang 4–20 mA + 2× relé) bak
Elfin-en.

### Eksperimentrommet: fire + én tilstander

Med føler-emuleringen blir styringsrommet per manifold: **16 trinn på
dag-settpunktet + nattsenk-nivået + av-tilstanden**. Grunnmatrisen med
de to uavhengige nattsenk-vekslerne gir **fire kombinasjoner** å
eksperimentere med for energi- og miljøoptimalisering:

| | Tilluft dag (+80) | Tilluft natt (lav) |
|---|---|---|
| **Fraluft dag (−80)** | normal drift | eksperiment |
| **Fraluft natt (lav)** | eksperiment | lavlast |

I tillegg finnes en **femte tilstand: primærviftene stoppes helt** og
alt tvangskjøres av sekundærkretsen alene. Primærkretsen har ikke
absolutte stengespjeld, så sonene kan trekke luft gjennom det avslåtte
aggregatet. Her kan det også eksperimenteres med **reversering av én
eller flere sonevifter** (Salda), slik at enkelte soner fungerer som
avtrekk for de andre.

Ingen ambisjon per nå om å overta selve PID-sløyfa (full kontinuerlig
dp-styring) — PRH beholder reguleringen; feiler kontrolleren, faller
anlegget tilbake til dag-settpunktene.
