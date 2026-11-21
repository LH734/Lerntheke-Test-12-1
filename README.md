# Lerntheke Test 2 · Physik GK 12

Vorbereitung auf Test 2 (12/I) am Mi 25.11.2026: Mechanische Schwingungen und Wellen. 8 Themen (W1 bis W5 Wellen bis Deck 28, S1 bis S3 Weg-Zeit-Gesetz, v und a, Federschwinger und Resonanz), 32 Aufgaben, 16 Diagnosefragen. Der Probetest zieht bei jedem Start ganze Aufgaben aus dem Pool (19 bis 21 BE, höchstens eine je Thema, 2,2 min je BE).

Gebaut aus der Lerntheke zur Klausur (Oktober 2026). Eigener Speicherschlüssel und eigener Cache, beide Lerntheken stören sich auf github.io nicht.

Statische Web-App ohne Server und ohne Framework. Läuft auf GitHub Pages und offline.

## Aufbau

| Pfad | Inhalt |
|---|---|
| `index.html` | Einstieg |
| `aufgaben.json` | alle Inhalte, erzeugt von `lerntheke_inhalt.py` |
| `lerntheke_inhalt.py` | **einzige Stelle für Inhaltsänderungen** |
| `js/config.js` | Z-Sperre, BE-Regel bei Auswahlaufgaben, Vorgaben des Probetests |
| `js/` | App-Logik (`app.js` Oberfläche, `zahl.js` Zahlenprüfung, `klausur.js` Probetest, `speicher.js` Fortschritt und Code, `abbildungen.js` SVG) |
| `css/app.css` | Gestaltung inkl. Dunkelmodus |
| `lib/` | KaTeX 0.16.11 und qrcode-generator 1.4.4, lokal |
| `sw.js` | Service Worker für den Offline-Betrieb |
| `tests/` | Unit-Tests und Browser-Tests |

## Inhalte ändern

1. `lerntheke_inhalt.py` bearbeiten.
2. Im Projektordner ausführen: `python3 lerntheke_inhalt.py`. Das Skript rechnet nach, prüft die Schreibregeln und schreibt `aufgaben.json` neu.
3. Hochladen (siehe unten). Geräte, die die Lerntheke schon kennen, zeigen beim nächsten Öffnen „Es gibt eine neue Version“.

## Einstellungen (`js/config.js`)

- `zSperre: false` gibt die Z-Aufgaben auf **allen** Geräten frei.
- Unter `?lehrer=1` gibt es die Vorschau aller Aufgaben mit Lösungen. Der Schalter dort wirkt nur auf dem eigenen Gerät.
- `auswahlNurErsterVersuch: true` gibt die BE bei Auswahlaufgaben nur für den ersten Versuch.
- `loesungVergleichen` legt fest, wann „Lösung vergleichen“ frei wird: nach einem falschen Ergebnis und frühestens nach `max(mindestMinuten, minutenJeBE · BE)` Minuten seit Beginn der Teilaufgabe.

## Lokal ansehen

```bash
python3 -m http.server 8000
```

Dann `http://localhost:8000` öffnen. Ein Doppelklick auf `index.html` reicht nicht, weil der Browser `aufgaben.json` dann nicht laden darf.

## Tests

```bash
pip install playwright
python3 tests/run_tests.py --screenshots
# ohne installiertes Google Chrome: playwright install chromium, dann --chromium anhängen
```

Geprüft werden: Zahleneingabe, Toleranz, Vorzeichen, Zehnerpotenz-Hinweis, JSON-Prüfung, 100 Probetest-Ziehungen, Notenpunkte, Fortschritts-Code, alle 32 Aufgaben bei 360 px mit den Lösungswerten, Diagnose, Probetest, Z-Sperre, Lehreransicht, Offline-Betrieb und die Schreibregeln auf allen Seiten. Screenshots landen in `tests/screenshots/`.

## Veröffentlichen auf GitHub Pages

1. Auf github.com ein leeres Repository anlegen, z. B. `Lerntheke-GK12-Test2` (ohne README).
2. Im Projektordner:
   ```bash
   git init -b main
   git add .
   git commit -m "Lerntheke Test 2"
   git remote add origin https://github.com/BENUTZERNAME/Lerntheke-GK12-Test2.git
   git push -u origin main
   ```
3. Im Repository unter **Settings → Pages**: Source „Deploy from a branch“, Branch `main`, Ordner `/ (root)`.
4. Nach etwa einer Minute ist die App unter `https://BENUTZERNAME.github.io/Lerntheke-GK12-Test2/` erreichbar.
5. Spätere Änderungen: `git add . && git commit -m "…" && git push`.

Den Ordner „Übergabe Claude Code“ schließt `.gitignore` aus. Wenn sich die Liste der Dateien in `sw.js` ändert, dort `VERSION` erhöhen.
