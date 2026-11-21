// Einstellungen der Lerntheke. Nach einer Änderung die Datei ins Repo hochladen,
// dann gilt sie für alle Geräte.

export const KONFIG = {
  // Z-Aufgaben eines Themas erst freigeben, wenn G und A dieses Themas bearbeitet sind.
  // false schaltet die Sperre für alle Geräte ab.
  zSperre: true,

  // Auswahlaufgaben geben die BE nur, wenn der erste Prüfversuch richtig ist.
  // false: richtig vor dem Anzeigen der Lösung gibt die BE, wie bei Zahlenaufgaben.
  auswahlNurErsterVersuch: true,

  // „Lösung vergleichen“ wird erst frei, wenn ein falsches Ergebnis eingegeben wurde und seit
  // Beginn der Teilaufgabe genug Zeit vergangen ist: der größere Wert aus mindestMinuten und
  // minutenJeBE mal BE der Teilaufgabe.
  loesungVergleichen: {
    mindestMinuten: 2,
    minutenJeBE: 1,
  },

  // Probetest (Format wie Test 2: 20 BE, 45 Minuten)
  klausur: {
    beMin: 19,
    beMax: 21,
    afbI: [0.25, 0.45],
    afbII: [0.45, 0.70],
    afbIII: [0.05, 0.20],
    anteilBereich: 'Wellen',
    anteilSpanne: [0.45, 0.70],
    hoechstensEineAufgabeJeThema: true,
    versuche: 20000,
  },
};
