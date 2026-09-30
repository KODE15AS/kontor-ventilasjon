# regin — 10 undersystemer

Anlegget er delt i **10 distinkte undersystemer** («soner»): gruppe 1–8 pluss
9a og 9b, hver styrt av én **Regin RCF-230CTD-EC** (kommuniserende
romregulator for fancoil). Kobling gruppe ↔ områdenavn: se
`../dok/omrader-og-grupper.md`. Brukerne skal styre sonene fra KODE-klima
(`kode-klima/`).

## Datatilkobling (avklart 2026-09-30)

Regulatorene har **innebygd RS485 med Modbus RTU slave** («C» i
modellnavnet = communicating), og RS485-bussen er **allerede kablet** i
sonene: A = blå, B = sort på Cat-kabel, se koblingsskjema
`dok/54740T390-2-regin-gruppekontroller.pdf` (2019). Registerlister,
adressering og alle nøkkelfakta: `dok/README.md`. Anleggets
Regio-konfigurasjon fra 2023 ligger i `konfig/`.

I tillegg finnes en **løs test-REGIN («gruppe 10»)** som testinstrument —
naturlig førstemål for kommunikasjonstesting før driftssatte soner røres.

Avklares:

- Gateway-design: én felles RS485-buss til raven via én gateway
  (f.eks. Elfin EW11A-0, se `../nilan/README.md`), eller én Elfin per
  sone i Ø70 veggboks — avhenger av hvordan Cat-kablene er terminert
- Modbus-adresser (ELA) per sone — leses ut/settes med Regio tool
- API mot backend og kobling til KODE-klima
