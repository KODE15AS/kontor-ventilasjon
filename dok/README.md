# Dokumentregister — felles

Dokumenter som gjelder hele anlegget/prosjektet. System-spesifikke
dokumenter ligger i `nilan/dok/` og `regin/dok/`.

## Tegningsgrunnlag

| Fil | Innhold |
|---|---|
| `2026-09-30-kontor-layout.dxf` | CAD-original (binær DXF) — kilde for `kode-klima/kontor-mal.svg` |
| `2026-09-29-kontor-layout.pdf` | Layout-PDF (må roteres 90°) |
| `2026-09-29-kontor-layout-1etg.jpg` | Jørns skisse med sonemarkeringer |
| `omrader-og-grupper.md` | Kryssreferanse sone ↔ gruppe ↔ byggefase-navn |

## Testutstyr

| Fil | Innhold |
|---|---|
| `cnvt-usb-rs485-datablad-en.pdf` | **Sentera CNVT-USB-RS485** — USB-til-RS485-adapter (Jørn har 1 stk., kjøpt 2023). FTDI-basert: støttes av Linux-kjernen (`ftdi_sio`), plugges rett i raven som `/dev/ttyUSB0`. Paritet none/even/odd, 7/8 databiter — dekker både NILAN (19200 8E1) og REGIN. ESD-vern ±15 kV. |
| `2023-03-16-eldi-faktura-usb-rs485-adapter.pdf` | Faktura ELDI AS (solgt som «ELDI-USB-RS485 med vern») |

Ikke tatt inn i repoet: Windows-drivere (FTDI CDM 2.12.28) og Jørns
Windows-installasjonsnotat fra 2023 — irrelevant på raven, ligger i
Dropbox.
