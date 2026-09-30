# regin — 10 undersystemer

Anlegget er delt i **10 distinkte undersystemer** («soner»): gruppe 1–8 pluss
9a og 9b, hver styrt av én **Regin RCF-230CTD-EC** (kommuniserende
romregulator for fancoil). Kobling gruppe ↔ områdenavn: se
`../dok/omrader-og-grupper.md`. Brukerne skal styre sonene fra KODE-klima
(`kode-klima/`).

## Datatilkobling (avklart 2026-09-30)

Regulatorene har **innebygd RS485 med Modbus RTU slave** («C» i
modellnavnet = communicating), og RS485-parene er alt kablet i sonene:
A = blå, B = sort på Cat-kabel, se koblingsskjema
`dok/54740T390-2-regin-gruppekontroller.pdf` (2019). Registerlister,
adressering og alle nøkkelfakta: `dok/README.md`. Anleggets
Regio-konfigurasjon fra 2023 ligger i `konfig/`.

I tillegg finnes en **løs test-REGIN («gruppe 10»)** som testinstrument —
naturlig førstemål for kommunikasjonstesting før driftssatte soner røres.

## ✅ Første Modbus-kontakt (2026-09-30)

Test-REGIN gruppe 10, koblet til raven via USB-RS485-adapteren
(Sentera CNVT-USB-RS485, `/dev/ttyUSB0`), svarer på:

- **Adresse 247** (ikke 30 som i konfigmalen — adresseskann 1–247 fant den)
- **9600 baud, 8 databiter, Even paritet, 1 stoppbit**
- Programvare RC v1.4.1.0; temperaturer leses med faktor 10
  (input-register 11 = 216 → 21,6 °C)
- Verifisert mot displayet: romtemp, komfortmodus, varmepådrag og
  viftetrinn stemte
- Verktøy: Python `pymodbus` (skann og lesing tok sekunder — Regio Tool
  trengs ikke)
- **Skrivetest OK samme dag:** grunnsettpunkt (holding-register 284,
  faktor 10) skrevet +1 °C og tilbake, aktivt settpunkt fulgte med.
  Full lese/skrive-sløyfe bevist — alt REGIN kan konfigureres til er
  tilgjengelig over Modbus (manualen kap. 16–17), inkl. driftsmodus,
  viftestyring, regulatorparametre og sperring av lokale knapper.
  KODE-klima kan dermed være master med REGIN som utførende slave;
  lokal regulering fortsetter på siste settpunkt om nettet faller ut.

**Kabeltopologi (bekreftet av Jørn 2026-09-30):** Cat-kablene er IKKE
terminert som felles buss. De går som signalkabler i stjerne, fra hver
enkelt REGIN til sonens varmebatteri, som fungerer som koblingsboks/-skap
(relé m.m.). Konsekvens: fjernstyring krever én gateway per sone —
kandidaten **Elfin EW11A-0** (se `../nilan/README.md`) passer i Ø70
veggboks ved varmebatteriet.

## Fysisk installasjon (foto 2026-09-28)

Foto av REGIN-terminering, veggboks og manifold med Salda-vifter og
Salda-varmebatterier (levert av Dantherm): se `bilder/README.md`.
Merk fra bildene:

- Veggboksen **bak** regulatoren er alt opptatt av et Finder-impulsrelé
  (13.31.8.230.4300) — eventuell gateway må plasseres ved varmebatteriet,
  ikke bak REGIN.
- Varmebatteriets koblingsboks har Wago-klemmer og Finder 97.01-sokkel
  med relé — der terminerer signalkabelen fra sonens REGIN.

Avklares:

- Endelig gateway-valg og plassering per sone (Elfin EW11A-0 ved
  varmebatteriet er arbeidshypotesen)
- Modbus-adresser (ELA) per sone — leses ut/settes med Regio tool
- API mot backend og kobling til KODE-klima
