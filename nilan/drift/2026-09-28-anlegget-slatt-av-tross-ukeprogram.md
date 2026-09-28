# 2026-09-28 — Anlegget slått av tross ukeprogram

## Observasjon (Jørn, panelbilder i `../dok/`)

- Hovedskjerm viser **«Slått av»** med både stopp-ikon (rød sirkel-X) og
  **varseltrekant** aktiv (`2026-09-28-panel-1-hovedskjerm-slatt-av.jpeg`)
- Ukeprogram 2 er aktivt (`…-panel-2-ukeprogram-2-aktiv.jpeg`)
- Mandag: Funksjon 1 = 06:00, 20 °C, Trinn 1; Funksjon 2 = 12:00, 22 °C,
  **De-aktiver**; Funksjon 3 = De-aktiveret (`…-panel-3-mandag-funksjoner.jpeg`)
- Forventning: anlegget skulle startet i Trinn 1 kl. 06:00 i dag (mandag)

## Analyse (mot CTS602i-softwareveiledningen)

1. **Ukeprogrammet kan ikke starte et avslått aggregat.** Manualen (s. 9,
   «Tænd for aggregatet»): aggregatet slås på/av under Innstillinger → Drift
   (Slukket/Tændt). Ukeprogrammet styrer bare tid/temperatur/ventilasjonstrinn
   for et aggregat som er PÅ. Står Drift på «Slukket», skjer det ingenting
   kl. 06:00.
2. **Aktiv alarm stopper aggregatet.** Manualen (s. 5): «Alarm viser, at der
   er noget alvorligt galt … Aggregatet er stoppet.» Varseltrekanten på
   hovedskjermen tyder på aktiv advarsel/alarm. En aktiv alarm kan ikke
   nullstilles før årsaken er utbedret (s. 10).
3. **Funksjon 2 mandag ser mistenkelig ut:** «12:00, 22 °C, De-aktiver»
   betyr ventilasjon = Slukket fra kl. 12:00 (manualen s. 12: trinnvalg er
   Trin 1–4 / Slukket). Hvis dette går igjen alle dager, skrur programmet
   selv anlegget av midt på dagen.

## Mest sannsynlige årsak

Aktiv alarm har stoppet aggregatet, og/eller Drift står på «Slukket» —
ukeprogrammet kan uansett ikke vekke det.

## Neste steg (sjekkliste for Jørn ved panelet)

- [ ] Trykk på varseltrekanten: noter alarm-ID og navn (ta bilde)
- [ ] Sjekk Innstillinger → Drift: står den på «Slukket»? Sett «Tændt» når
      alarmen er avklart
- [ ] Sjekk Dato/Tid på anlegget (feil klokke gir feil programtider)
- [ ] Avklar om Funksjon 2 «De-aktiver kl. 12:00» er tilsiktet
- [ ] Dokumenter alarmårsak her og lukk saken
