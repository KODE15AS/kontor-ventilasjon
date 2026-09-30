# Dokumentregister — regin

Kilde: Jørns Dropbox, overført 2026-09-30. Regulatoren i sonene er
**Regin RCF-230CTD-EC** — kommuniserende romregulator for fancoil.

## Nøkkelfakta (fra databladet og manualen)

- «C» i modellnavnet = **innebygd kommunikasjon**: RS485 med **Modbus RTU
  slave** (9600/19200/38400 bps, automatisk EXOline/Modbus-deteksjon),
  alternativt BACnet MS/TP.
- Modbus-paritet: odd/even + 1 stoppbit, eller ingen paritet + 2 stoppbiter.
- Adressering: etikettadresse `PLA:ELA` — Modbus-adressen er ELA-delen.
- Komplette Modbus-registerlister står i manualen (kap. 16–17: discrete
  inputs, coils, input- og holding-registre).
- Konfigureres med gratisverktøyet **Regio tool**; anleggets egen
  konfigurasjon fra 2023 ligger i `../konfig/`.
- **RS485-bussen er allerede kablet i sonene:** koblingsskjema
  `54740T390-2` (J. Watvedt, 2019) viser A = blå og B = sort på Cat-kabel
  til hver lokalkontroller.

## Filer

| Fil | Innhold |
|---|---|
| `rcf-230ctd-ec-datablad-2019-en.pdf` | Produktdatablad rev 05/2019 (engelsk) |
| `rcf-230-manual-parametere-modbus-2019-en.pdf` | Komplett manual 2019 (engelsk): installasjon, parametere og **Modbus-registerlister** |
| `rcf-230ctd-ec-monteringsanvisning-2019.pdf` | Monteringsanvisning 10523E (05/2019, en/sv/de/fr) |
| `rcf-230ctd-ec-eu-samsvarserklaering.pdf` | EU-samsvarserklæring |
| `rcf-230-miljodeklarasjon.pdf` | Miljødeklarasjon type II, alle RCF(M)-230-modeller |
| `rcf-230-bunnplate-foto.jpg` | Foto av bunnplaten (kobling) fra anlegget |
| `54740T390-1-koblingsskjema-varmebatt-og-vifte.pdf` | Koblingsskjema varmebatteri og vifte (J. Watvedt, 2019) |
| `54740T390-2-regin-gruppekontroller.pdf` | Koblingsskjema REGIN lokalkontroller — **viser RS485 A/B-kabling** (J. Watvedt, 2019) |
| `54740T390-3-dorstolpe-arrangement.pdf` | Dørstolpe-arrangement (J. Watvedt, 2019) |

## Eliminerte duplikater (ikke tatt inn i repoet)

- «Brsojyre MERE INFO RCF-230CTD-EC.pdf» — eldre revisjon (01/2015) av databladet
- «RCF-230CTD-EC Manual Svensk.pdf» — svensk språkvariant av databladet 05/2019
- «Komplett spesifiksjon RCF 230 SE.pdf» — eldre svensk utgave (2016) av manualen
- «Monteringsanvisning RCF-230CTD-EC.pdf» — eldre revisjon 10523D (01/2018) av monteringsanvisningen
