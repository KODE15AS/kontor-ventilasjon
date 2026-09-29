# regin — 10 undersystemer

Anlegget er delt i **10 distinkte undersystemer** («soner»): gruppe 1–8 pluss
9a og 9b, hver styrt av én **REGIN 230 CTD EC**. Kobling gruppe ↔ områdenavn:
se `../dok/omrader-og-grupper.md`. Regulatorene har ikke egen fjernstyring;
hver får montert en **ESP32** som gjør sonen fjernstyrbar over WiFi (lokalt
nett «Kode15»). Brukerne styrer sonene fra KODE-klima (`kode-klima/`).

I tillegg finnes en **løs test-REGIN («gruppe 10»)** som testinstrument for
validering av kommunikasjon — den er naturlig førstemål for ESP32-utviklingen
før noe monteres i driftssatte soner.

Avklares:

- ESP32-design: fastvare, grensesnitt mot REGIN-regulatoren, API mot backend

Status: ikke påbegynt.
