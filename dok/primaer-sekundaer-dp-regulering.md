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
sonene. PRH-ene betjenes manuelt i dag, men produktdokumentasjonen
(`../nilan/dok/`) viser tre veier til agent-tilgang, i økende grad av
inngrep:

1. **Lese dp (uinvasivt):** PRH har BMS-utgang 4–20 mA med målt trykk.
   En ekstern ADC (f.eks. ESP32) gir agenten kontinuerlig dp-overvåking
   av begge manifolder uten å røre reguleringen. Alarmreléet kan
   overvåkes samtidig.
2. **To dp-nivåer (lavinvasivt — anbefalt første trekk):**
   PRH har **nattsenk-inngang** laget for ekstern tidsstyring
   (potensialfri kontakt). Et agent-styrt relé per PRH gir to nivåer:
   dag-settpunkt (80 Pa) og natt-settpunkt (f.eks. 40–50 Pa, stilles
   én gang manuelt). Reguleringen bor fortsatt trygt i PRH.
3. **Full kontinuerlig dp-styring (mest invasivt — senere ved behov):**
   egen regulator (f.eks. ESP32 med ADC/DAC) overtar sløyfa: leser PTH
   0–10 V, kjører PID i programvare, driver viftesignalet 0–10 V.
   PRH beholdes som fallback via omkoblingsrelé.
