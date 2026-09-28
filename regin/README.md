# regin — 10 undersystemer

Anlegget er delt i **10 distinkte undersystemer** («soner»), hver styrt av én
**REGIN 230 CTD EC**. Regulatorene har ikke egen fjernstyring; hver får
montert en **ESP32** som gjør sonen fjernstyrbar over WiFi (lokalt nett
«Kode15»). Brukerne styrer sonene fra KODE-klima (`kode-klima/`).

Avklares:

- Navneliste for de 10 sonene (identifiseres og navngis senere; mønsteret
  blir én katalog per sone under `regin/`)
- ESP32-design: fastvare, grensesnitt mot REGIN-regulatoren, API mot backend

Status: ikke påbegynt.
