# -*- coding: utf-8 -*-
"""Inhalt der digitalen Lerntheke zu Test 2 (12/I) GK 12: Mechanische Schwingungen und
Wellen, Stand 17.11.2026.

Gleicher Aufbau wie die Lerntheke zur Klausur (Oktober 2026). Erzeugt aufgaben.json für
die Web-App. Alle Zahlenwerte werden hier nachgerechnet (assert), die JSON-Werte stammen
aus denselben Rechnungen.

Stoff wie Test 2: Wellen bis Deck 28 (Entstehung, Arten, Trägermedium, Polarisation,
c und v, harmonische Welle, c = λ · f, Phase) und aus den Schwingungen das Weg-Zeit-Gesetz,
v(t), a(t), T = 2π · √(m/D) und Resonanz.

Regeln (Lukas 17.11.):
- Keine Formel aus einem Sachzusammenhang neu herleiten lassen. Erlaubt ist, bekannte
  Formeln zusammenzusetzen oder mit einem zuvor berechneten Wert weiterzurechnen.
- Die Aufgaben des Tests selbst stehen nicht im Pool.

Konventionen: Amplitude y_max, Elongation y, Kreisfrequenz ω, positive Richtung oben.
Kein „Takt“, nichts Umgangssprachliches, keine Gedankenstriche im Satz, kein Komma vor
„und“, keine Semikolons, keine Quellen im Schülertext. Formeln in LaTeX zwischen $…$.
"""
import json
import math

PI = math.pi
G = 9.81


def r(x, n=3):
    """auf n signifikante Stellen runden"""
    if x == 0:
        return 0.0
    return round(x, -int(math.floor(math.log10(abs(x)))) + (n - 1))


def ZAHL(text, wert, einheit, be, afb, hilfen, loesung, tol=0.02, vorzeichen="streng"):
    return {"text": text, "be": be, "afb": afb,
            "pruefung": {"typ": "zahl", "wert": wert, "einheit": einheit,
                         "toleranz_rel": tol, "vorzeichen": vorzeichen},
            "hilfen": hilfen, "loesung": loesung}


def WAHL(text, optionen, richtig, be, afb, hilfen, loesung, mehrfach=False):
    return {"text": text, "be": be, "afb": afb,
            "pruefung": {"typ": "auswahl", "optionen": optionen, "richtig": richtig,
                         "mehrfach": mehrfach},
            "hilfen": hilfen, "loesung": loesung}


def SELBST(text, be, afb, kriterien, hilfen, loesung):
    assert len(kriterien) >= be, text
    return {"text": text, "be": be, "afb": afb,
            "pruefung": {"typ": "selbst", "kriterien": kriterien},
            "hilfen": hilfen, "loesung": loesung}


THEMEN = []
AUFGABEN = []
DIAGNOSE = []
BEREICHE = [{"id": "Wellen", "name": "Mechanische Wellen"},
            {"id": "Schwingungen", "name": "Mechanische Schwingungen"}]


def thema(tid, bereich, titel, stunden, checkliste):
    THEMEN.append({"id": tid, "bereich": bereich, "titel": titel,
                   "hefter": stunden, "checkliste": checkliste})


def aufgabe(aid, tid, stufe, titel, kontext, teile, abbildung=None):
    for i, t in enumerate(teile):
        t["id"] = "abcdefgh"[i]
    AUFGABEN.append({"id": aid, "thema": tid, "stufe": stufe, "titel": titel,
                     "kontext": kontext, "abbildung": abbildung, "teile": teile})


def diag(tid, frage, optionen, richtig):
    DIAGNOSE.append({"thema": tid, "frage": frage, "optionen": optionen,
                     "richtig": richtig})


MS = "\\,\\tfrac{m}{s}"
PS = "\\,\\tfrac{1}{s}"
MS2 = "\\,\\tfrac{m}{s^2}"

# ========================================================================
#  MECHANISCHE WELLEN
# ========================================================================

# ------------------------------------------------------------------ W1
thema("W1", "Wellen", "Entstehung einer Welle", "Deck 26",
      ["Ein Oszillator braucht eine Rückstellkraft, die Trägheit lässt ihn über die "
       "Ruhelage hinausschwingen.",
       "Gekoppelte Oszillatoren geben die Schwingung zeitversetzt weiter.",
       "Eine Welle transportiert Energie und Impuls, aber keine Materie.",
       "Alle Oszillatoren schwingen mit der Frequenz des Erregers.",
       "$c = \\dfrac{\\Delta s}{\\Delta t}$ für die Ausbreitung einer Störung"])

aufgabe("W1-G1", "W1", "G", "Wellenmaschine",
        "Bei der Wellenmaschine sind viele Stäbe drehbar an einem gemeinsamen Band befestigt. "
        "Der erste Stab wird angestoßen, danach beginnen nacheinander alle Stäbe zu "
        "schwingen.",
        [WAHL("Wodurch wird die Schwingung von einem Stab an den nächsten weitergegeben?",
              ["durch die Kopplung über das Band", "durch Stöße der Stäbe aneinander",
               "durch die Luft zwischen den Stäben", "durch die Gewichtskraft der Stäbe"],
              [0], 1, "I",
              ["Was verbindet die Stäbe miteinander?"],
              ["Die Stäbe sind über das Band gekoppelt. Jeder Stab zieht über das Band am "
               "nächsten und gibt die Schwingung zeitversetzt weiter."]),
         WAHL("Was transportiert die Welle entlang der Maschine? Wähle alle richtigen "
              "Antworten.",
              ["Energie", "Impuls", "die Stäbe", "das Band"], [0, 1], 1, "I",
              ["Bewegen sich die Stäbe von einem Ende zum anderen?",
               "Die Stäbe bleiben an ihrem Ort, weiter läuft nur ihr Schwingungszustand."],
              ["Transportiert werden Energie und Impuls. Stäbe und Band bleiben an ihrem "
               "Ort."], mehrfach=True)])

aufgabe("W1-G2", "W1", "G", "Der Oszillator",
        "Ein Körper hängt an einer Feder. Er wird nach unten gezogen und losgelassen.",
        [SELBST("Erkläre, warum der Körper über die Ruhelage hinausschwingt.", 2, "I",
                ["Die Rückstellkraft der Feder beschleunigt den Körper zur Ruhelage hin.",
                 "In der Ruhelage ist er am schnellsten. Wegen seiner Trägheit bewegt er sich "
                 "weiter, bis die Rückstellkraft ihn auf der anderen Seite abbremst."],
                ["Welche Kraft wirkt, solange der Körper ausgelenkt ist?",
                 "Welche Eigenschaft eines Körpers sorgt dafür, dass er sich weiterbewegt?"],
                ["Rückstellkraft zur Ruhelage hin", "Trägheit: in der Ruhelage größte "
                 "Geschwindigkeit, Bewegung geht weiter"]),
         WAHL("Viele solche Oszillatoren sind zu einer Kette gekoppelt. Der erste wird mit "
              "2,0 Hz auf und ab bewegt. Mit welcher Frequenz schwingt der zehnte "
              "Oszillator?",
              ["2,0 Hz", "0,20 Hz", "20 Hz", "mit seiner eigenen, beliebigen Frequenz"],
              [0], 1, "I",
              ["Wer gibt in einer Welle die Frequenz vor?"],
              ["Alle Oszillatoren schwingen mit der Frequenz des Erregers, also mit 2,0 Hz."])])

C_SEIL = 15 / 2.5
assert abs(C_SEIL - 6.0) < 1e-12
aufgabe("W1-A", "W1", "A", "Trainingsseil",
        "Ein Sportler bewegt das Ende eines 15 m langen Trainingsseils dreimal pro Sekunde auf "
        "und ab. Der erste Wellenberg erreicht das andere Ende nach 2,5 s.",
        [ZAHL("Berechne die Ausbreitungsgeschwindigkeit der Welle.", C_SEIL, "m/s", 1, "I",
              ["Welche Strecke legt der Wellenberg in welcher Zeit zurück?",
               "$c = \\dfrac{\\Delta s}{\\Delta t}$"],
              ["$c = \\dfrac{\\Delta s}{\\Delta t} = \\dfrac{15\\,m}{2{,}5\\,s} = 6{,}0" + MS + "$"]),
         ZAHL("Gib die Frequenz an, mit der ein Seilstück in der Mitte schwingt.", 3.0, "Hz",
              1, "II",
              ["Wer bestimmt die Frequenz der Seilstücke?"],
              ["Alle Seilstücke schwingen mit der Frequenz des Erregers: dreimal pro Sekunde, "
               "also 3,0 Hz."]),
         SELBST("Ein Mitschüler meint: „Mit jeder Welle wird das Seil ein Stück zum anderen "
                "Ende geschoben.“ Nimm Stellung.", 2, "II",
                ["Die Aussage ist falsch. Jedes Seilstück schwingt nur um seine Ruhelage auf "
                 "und ab.",
                 "Weiter läuft der Schwingungszustand. Transportiert wird Energie, keine "
                 "Materie."],
                ["Wohin bewegt sich ein einzelnes Seilstück?",
                 "Was läuft dann eigentlich über das Seil?"],
                ["falsch: Seilstücke schwingen um ihre Ruhelage",
                 "Energietransport ohne Materietransport"])])

C_TS = 3600e3 / (5.0 * 3600)
assert abs(C_TS - 200) < 1e-9
aufgabe("W1-Z", "W1", "Z", "Welle oder nicht?",
        "Zwei Vorgänge werden verglichen: Eine Reihe Dominosteine fällt nacheinander um. "
        "Ein Tsunami läuft über den offenen Ozean.",
        [SELBST("Beurteile, ob die fallenden Dominosteine eine mechanische Welle sind.", 2,
                "III",
                ["Ein Dominostein hat keine Rückstellkraft zu einer Ruhelage hin, er kehrt "
                 "nicht zurück. Er ist kein Oszillator.",
                 "Es wird keine Schwingung weitergegeben, nur ein einmaliger Umfallvorgang. "
                 "Die Dominoreihe ist keine mechanische Welle."],
                ["Was braucht ein Oszillator?",
                 "Schwingt ein Dominostein nach dem Umfallen um eine Ruhelage?"],
                ["kein Oszillator: keine Rückstellkraft, keine Rückkehr",
                 "keine Schwingung, die weitergegeben wird: keine Welle"]),
         ZAHL("Der Tsunami legt 3600 km in 5,0 h zurück. Berechne seine "
              "Ausbreitungsgeschwindigkeit in $\\tfrac{m}{s}$.", C_TS, "m/s", 1, "II",
              ["Rechne Kilometer in Meter und Stunden in Sekunden um."],
              ["$c = \\dfrac{3600 \\cdot 10^3\\,m}{5{,}0 \\cdot 3600\\,s} = 200" + MS + "$"]),
         WAHL("Auf dem offenen Ozean wird das Wasser kaum mitbewegt. Warum richtet der "
              "Tsunami an der Küste trotzdem große Schäden an?",
              ["Die Welle transportiert sehr viel Energie zur Küste.",
               "Das Wasser des offenen Ozeans wird zur Küste transportiert.",
               "An der Küste ändert sich die Frequenz stark.",
               "Der Tsunami ist keine Welle."], [0], 1, "II",
              ["Was transportiert eine Welle?"],
              ["Eine Welle transportiert Energie. Diese Energie wird an der Küste frei."])])

diag("W1", "Was transportiert eine mechanische Welle?",
     ["Energie, aber keine Materie", "Materie und Energie", "nur Materie",
      "weder Energie noch Materie"], 0)
diag("W1", "Mit welcher Frequenz schwingen die Oszillatoren einer Welle?",
     ["mit der Frequenz des Erregers", "jeder mit seiner eigenen Frequenz",
      "mit abnehmender Frequenz", "mit der doppelten Erregerfrequenz"], 0)

# ------------------------------------------------------------------ W2
thema("W2", "Wellen", "Wellenarten und Trägermedium", "Deck 27",
      ["transversal: Schwingungsrichtung senkrecht zur Ausbreitungsrichtung",
       "longitudinal: Schwingungsrichtung parallel zur Ausbreitungsrichtung",
       "mechanische Wellen brauchen ein Trägermedium, in Gasen nur longitudinal",
       "stärkere Kopplung, größeres c: Luft $340" + MS + "$, Wasser $1480" + MS + "$, "
       "Stahl $5100" + MS + "$",
       "Polarisation gibt es nur bei Transversalwellen"])

aufgabe("W2-G1", "W2", "G", "Quer oder längs?",
        "Ordne die Wellen zu.",
        [WAHL("Ein Seil wird am Ende auf und ab bewegt.",
              ["Transversalwelle", "Longitudinalwelle"], [0], 1, "I",
              ["Vergleiche die Schwingungsrichtung mit der Ausbreitungsrichtung."],
              ["Die Seilstücke schwingen senkrecht zur Ausbreitungsrichtung: transversal."]),
         WAHL("Schall breitet sich in Luft aus.",
              ["Longitudinalwelle", "Transversalwelle"], [0], 1, "I",
              ["In welche Richtung schwingen die Luftteilchen?"],
              ["Die Luftteilchen schwingen in Ausbreitungsrichtung hin und her: "
               "longitudinal."])])

aufgabe("W2-G2", "W2", "G", "Trägermedium",
        "In einem Science-Fiction-Film explodiert ein Raumschiff im Weltall mit einem lauten "
        "Knall.",
        [SELBST("Begründe, warum man im Weltall keinen Knall hören kann.", 2, "I",
                ["Schall ist eine mechanische Welle und braucht ein Trägermedium aus "
                 "gekoppelten Teilchen.",
                 "Im Vakuum des Weltalls gibt es keine Teilchen, die die Schwingung "
                 "weitergeben können."],
                ["Was braucht eine mechanische Welle, um sich auszubreiten?",
                 "Gibt es im Weltall ein solches Medium?"],
                ["Schall braucht ein Trägermedium", "Vakuum: keine Teilchen, keine Kopplung"]),
         WAHL("Welche Wellen lassen sich polarisieren? Wähle alle richtigen Antworten.",
              ["eine Seilwelle mit senkrechter Schwingung",
               "eine Querwelle auf einer Schraubenfeder",
               "Schall in Luft", "eine Längswelle auf einer Schraubenfeder"], [0, 1], 1, "I",
              ["Polarisation gibt es nur bei einer Wellenart."],
              ["Nur Transversalwellen lassen sich polarisieren."], mehrfach=True)])

T_ST = 102 / 5100
T_LU = 102 / 340
assert abs(T_ST - 0.020) < 1e-12 and abs(T_LU - 0.30) < 1e-12
aufgabe("W2-A", "W2", "A", "Hammerschlag auf die Schiene",
        "Am Ende einer 102 m langen Stahlschiene schlägt jemand mit dem Hammer auf die "
        "Schiene. Am anderen Ende hält eine Person ein Ohr an die Schiene. Sie hört zwei "
        "Knalle. Schall breitet sich in Stahl mit $5100" + MS + "$ und in Luft mit "
        "$340" + MS + "$ aus.",
        [ZAHL("Berechne die Laufzeit des Schalls durch die Schiene in Sekunden.", T_ST, "s",
              1, "I",
              ["Stelle $c = \\dfrac{\\Delta s}{\\Delta t}$ nach $\\Delta t$ um."],
              ["$\\Delta t = \\dfrac{102\\,m}{5100" + MS + "} = 0{,}020\\,s$"]),
         ZAHL("Berechne die Laufzeit des Schalls durch die Luft.", T_LU, "s", 1, "I",
              ["Gleiche Rechnung mit der Schallgeschwindigkeit in Luft."],
              ["$\\Delta t = \\dfrac{102\\,m}{340" + MS + "} = 0{,}30\\,s$"]),
         ZAHL("Berechne den zeitlichen Abstand der beiden Knalle.", r(T_LU - T_ST), "s", 1,
              "II",
              ["Nutze deine Ergebnisse aus a) und b)."],
              ["$0{,}30\\,s - 0{,}020\\,s = 0{,}28\\,s$"]),
         WAHL("Warum ist der Schall in Stahl schneller als in Luft?",
              ["Die Teilchen im Stahl sind viel stärker gekoppelt.",
               "Die Teilchen im Stahl fliegen schneller.",
               "Stahl hat weniger Teilchen als Luft.",
               "Im Stahl ist die Frequenz höher."], [0], 1, "II",
              ["Wovon hängt die Ausbreitungsgeschwindigkeit ab?"],
              ["Je stärker die Oszillatoren gekoppelt sind, desto schneller wird die "
               "Schwingung weitergegeben."])])

aufgabe("W2-Z", "W2", "Z", "Quer oder längs nachweisen",
        "Auf einer langen Schraubenfeder läuft eine Welle. Die Feder wird durch einen "
        "schmalen senkrechten Spalt in einer Holzplatte geführt.",
        [SELBST("Plane mit dem Spalt ein Experiment, mit dem man entscheidet, ob die Welle "
                "transversal oder longitudinal ist.", 2, "III",
                ["Man beobachtet hinter dem Spalt, ob die Welle weiterläuft. Dann dreht man den "
                 "Spalt um 90°.",
                 "Eine Querwelle läuft nur durch, wenn der Spalt parallel zur "
                 "Schwingungsrichtung steht. Eine Längswelle läuft in jeder Stellung durch."],
                ["Was passiert mit einer Querwelle, deren Schwingungsrichtung quer zum Spalt "
                 "steht?",
                 "Spielt die Stellung des Spalts für eine Längswelle eine Rolle?"],
                ["Spalt drehen und hinter dem Spalt beobachten",
                 "quer: nur in einer Stellung durch, längs: in jeder Stellung durch"]),
         SELBST("Ein Mitschüler beobachtet, dass die Welle in beiden Spaltstellungen "
                "durchläuft. Er folgert: „Es ist eine Querwelle.“ Nimm Stellung.", 2, "II",
                ["Die Folgerung ist falsch.",
                 "Eine Querwelle würde in der gekreuzten Stellung blockiert. Die Beobachtung "
                 "spricht für eine Längswelle."],
                ["Was müsste bei einer Querwelle in einer der beiden Stellungen passieren?"],
                ["falsch", "Querwelle würde blockiert, also Längswelle"])])

diag("W2", "Schall in Luft ist eine …",
     ["Longitudinalwelle", "Transversalwelle", "Welle ohne Trägermedium",
      "Welle, die sich polarisieren lässt"], 0)
diag("W2", "In welchem Medium ist Schall am schnellsten?",
     ["Stahl", "Wasser", "Luft", "Vakuum"], 0)

# ------------------------------------------------------------------ W3
thema("W3", "Wellen", "Ausbreitungsgeschwindigkeit und Oszillatorgeschwindigkeit",
      "Decks 27 und 28",
      ["c: Ausbreitung des Schwingungszustands, konstant, vom Medium bestimmt",
       "v: Geschwindigkeit eines Oszillators, ändert sich ständig, in der Ruhelage am "
       "größten, in den Umkehrpunkten null",
       "$v_{max} = y_{max} \\cdot \\omega$ mit $\\omega = 2\\pi \\cdot f$",
       "Bewegungsrichtung eines Punktes mit der Nachbarregel bestimmen"])

aufgabe("W3-G1", "W3", "G", "Zwei Geschwindigkeiten",
        "Auf einem Seil läuft eine harmonische Welle.",
        [WAHL("Wo ist die Geschwindigkeit eines Seilstücks am größten?",
              ["in der Ruhelage", "im Wellenberg", "im Wellental",
               "überall gleich groß"], [0], 1, "I",
              ["Jedes Seilstück ist ein Oszillator. Wo ist ein Oszillator am schnellsten?"],
              ["Wie jeder Oszillator ist das Seilstück in der Ruhelage am schnellsten, im "
               "Berg und im Tal ist es kurz in Ruhe."]),
         WAHL("Wovon hängt die Ausbreitungsgeschwindigkeit c ab?",
              ["vom Medium, hier vom Seil", "von der Amplitude", "von der Frequenz",
               "von der Geschwindigkeit der Seilstücke"], [0], 1, "I",
              ["Welche Größe bleibt gleich, wenn man schneller oder stärker schüttelt?"],
              ["c wird vom Medium bestimmt: Material und Spannung des Seils."])])

V3 = 0.050 * 2 * PI * 2.0
assert abs(V3 - 0.628) < 0.001
aufgabe("W3-G2", "W3", "G", "Wie schnell ist ein Seilstück?",
        "Eine Seilwelle hat die Frequenz 2,0 Hz, die Amplitude 5,0 cm und die "
        "Ausbreitungsgeschwindigkeit $3{,}0" + MS + "$.",
        [ZAHL("Berechne die größte Geschwindigkeit eines Seilstücks.", r(V3, 2), "m/s", 2,
              "II",
              ["Zuerst $\\omega = 2\\pi \\cdot f$.", "$v_{max} = y_{max} \\cdot \\omega$, "
               "Amplitude in Meter."],
              ["$\\omega = 2\\pi \\cdot 2{,}0\\,Hz \\approx 12{,}6" + PS + "$",
               "$v_{max} = 0{,}050\\,m \\cdot 12{,}6" + PS + " \\approx 0{,}63" + MS + "$"],
              tol=0.03),
         WAHL("Vergleiche mit der Ausbreitungsgeschwindigkeit.",
              ["$v_{max}$ ist kleiner als c.", "$v_{max}$ ist gleich c.",
               "$v_{max}$ ist größer als c.", "Man kann beide nicht vergleichen."], [0], 1,
              "II", ["Vergleiche $0{,}63" + MS + "$ mit $3{,}0" + MS + "$."],
              ["$0{,}63" + MS + " < 3{,}0" + MS + "$. Die Seilstücke sind viel langsamer als "
               "die Welle."])])

aufgabe("W3-A", "W3", "A", "Nachbarregel",
        "Die Momentaufnahme zeigt eine Seilwelle, die nach rechts läuft.",
        [WAHL("In welche Richtung bewegt sich das Seilstück A gerade?",
              ["nach unten", "nach oben", "nach rechts", "es ist in Ruhe"], [0], 1, "II",
              ["Nachbarregel: Ein Seilstück macht als Nächstes, was sein Nachbar auf der "
               "Seite des Erregers gerade macht.",
               "Der Erreger ist links. Wo ist der linke Nachbar von A?"],
              ["Der linke Nachbar von A liegt tiefer. A bewegt sich nach unten."]),
         WAHL("In welche Richtung bewegt sich das Seilstück C gerade?",
              ["nach oben", "nach unten", "nach links", "es ist in Ruhe"], [0], 1, "II",
              ["Wo liegt der linke Nachbar von C?"],
              ["Der linke Nachbar von C liegt höher. C bewegt sich nach oben."]),
         WAHL("Welche Seilstücke sind in diesem Moment in Ruhe? Wähle alle richtigen "
              "Antworten.",
              ["B", "D", "A", "C"], [0, 1], 1, "I",
              ["Wo ist die Geschwindigkeit eines Oszillators null?"],
              ["B ist im Berg, D im Tal. In den Umkehrpunkten ist v = 0."], mehrfach=True),
         WAHL("Welche Seilstücke bewegen sich gerade am schnellsten? Wähle alle richtigen "
              "Antworten.",
              ["A", "C", "B", "D"], [0, 1], 1, "II",
              ["Wo ist ein Oszillator am schnellsten?"],
              ["A und C gehen gerade durch die Ruhelage, dort ist v am größten."],
              mehrfach=True)],
        abbildung={"typ": "yx_diagramm", "funktion": "sin", "ymax": 2.0, "lambda": 1.2,
                   "xmax": 2.4, "einheit_y": "cm", "einheit_x": "m", "raster": True,
                   "richtung": "rechts",
                   "punkte": [["A", 1.2], ["B", 1.5], ["C", 1.8], ["D", 2.1]]})

V_MEM = 0.050e-3 * 2 * PI * 1000
assert abs(V_MEM - 0.314) < 0.001
aufgabe("W3-Z", "W3", "Z", "Wie schnell ist die Luft?",
        "Eine Lautsprechermembran schwingt mit 1000 Hz und der Amplitude 0,050 mm. Die "
        "Luft vor der Membran schwingt mit derselben Amplitude.",
        [ZAHL("Berechne die größte Geschwindigkeit der Membran.", r(V_MEM, 2), "m/s", 2, "II",
              ["$v_{max} = y_{max} \\cdot \\omega$ mit $\\omega = 2\\pi \\cdot f$",
               "0,050 mm = $5{,}0 \\cdot 10^{-5}\\,m$"],
              ["$\\omega = 2\\pi \\cdot 1000\\,Hz \\approx 6280" + PS + "$",
               "$v_{max} = 5{,}0 \\cdot 10^{-5}\\,m \\cdot 6280" + PS + " \\approx 0{,}31" + MS + "$"],
              tol=0.03),
         SELBST("Ein Mitschüler sagt: „Die Luftteilchen fliegen mit $340" + MS + "$ vom "
                "Lautsprecher zum Ohr.“ Nimm Stellung.", 2, "III",
                ["Die Aussage ist falsch. Die Luftteilchen schwingen nur um ihre Ruhelage, "
                 "mit höchstens etwa $0{,}31" + MS + "$.",
                 "$340" + MS + "$ ist die Ausbreitungsgeschwindigkeit c. So schnell läuft der "
                 "Schwingungszustand und damit die Energie durch die Luft."],
                ["Was bedeutet dein Ergebnis aus a) für die Luftteilchen?",
                 "Welche Geschwindigkeit sind $340" + MS + "$?"],
                ["falsch: Teilchen schwingen um die Ruhelage, etwa $0{,}31" + MS + "$",
                 "$340" + MS + "$ ist c, die Ausbreitung des Schwingungszustands"])])

diag("W3", "Ein Seilstück ist gerade im Wellenberg. Seine Geschwindigkeit ist …",
     ["null", "am größten", "gleich c", "doppelt so groß wie c"], 0)
diag("W3", "Die Ausbreitungsgeschwindigkeit c einer Welle …",
     ["ist konstant und hängt vom Medium ab", "ändert sich ständig",
      "ist in der Ruhelage am größten", "hängt von der Amplitude ab"], 0)

# ------------------------------------------------------------------ W4
thema("W4", "Wellen", "Die harmonische Welle", "Deck 28",
      ["Das y(x)-Diagramm ist eine Momentaufnahme. Es liefert $y_{max}$ und λ.",
       "Das y(t)-Diagramm zeigt einen Oszillator. Es liefert $y_{max}$ und T.",
       "$c = \\dfrac{\\lambda}{T} = \\lambda \\cdot f$",
       "f bestimmt der Erreger, c bestimmt das Medium"])

aufgabe("W4-G1", "W4", "G", "Momentaufnahme ablesen",
        "Das Diagramm zeigt eine Momentaufnahme einer Seilwelle.",
        [ZAHL("Lies die Wellenlänge ab.", 1.2, "m", 1, "I",
              ["Die Wellenlänge ist der Abstand zweier benachbarter Wellenberge."],
              ["Benachbarte Berge liegen bei 0,3 m und 1,5 m: λ = 1,2 m."]),
         ZAHL("Lies die Amplitude ab.", 3.0, "cm", 1, "I",
              ["Die Amplitude ist der Abstand von der Ruhelage bis zum Berg."],
              ["$y_{max} = 3{,}0\\,cm$"])],
        abbildung={"typ": "yx_diagramm", "funktion": "sin", "ymax": 3.0, "lambda": 1.2,
                   "xmax": 2.4, "einheit_y": "cm", "einheit_x": "m", "raster": True,
                   "richtung": None, "punkte": []})

C4 = 4.0 * 0.50
assert abs(C4 - 2.0) < 1e-12
aufgabe("W4-G2", "W4", "G", "Wasserwelle",
        "Eine Wasserwelle hat die Wellenlänge 4,0 m. Ein Korken schwingt mit 0,50 Hz.",
        [ZAHL("Berechne die Ausbreitungsgeschwindigkeit.", C4, "m/s", 2, "I",
              ["$c = \\lambda \\cdot f$"],
              ["$c = \\lambda \\cdot f = 4{,}0\\,m \\cdot 0{,}50\\,Hz = 2{,}0" + MS + "$"]),
         ZAHL("Berechne die Periodendauer des Korkens.", 2.0, "s", 1, "I",
              ["$T = \\dfrac{1}{f}$"],
              ["$T = \\dfrac{1}{0{,}50\\,Hz} = 2{,}0\\,s$"])])

C4A = 2.4 / 1.6
assert abs(C4A - 1.5) < 1e-12
aufgabe("W4-A", "W4", "A", "Modellboot im Becken",
        "In einem Wellenbecken haben benachbarte Wellenberge den Abstand 2,4 m. Das Diagramm "
        "zeigt die Auslenkung eines Modellboots.",
        [ZAHL("Lies die Periodendauer ab.", 1.6, "s", 1, "I",
              ["Die Periodendauer ist die Zeit für eine volle Schwingung."],
              ["Nach 1,6 s wiederholt sich die Kurve: T = 1,6 s."]),
         ZAHL("Berechne die Ausbreitungsgeschwindigkeit der Welle.", C4A, "m/s", 1, "II",
              ["λ steht im Text, T hast du abgelesen.", "$c = \\dfrac{\\lambda}{T}$"],
              ["$c = \\dfrac{2{,}4\\,m}{1{,}6\\,s} = 1{,}5" + MS + "$"]),
         WAHL("Die Wellenmaschine wird auf die doppelte Frequenz gestellt. Was gilt?",
              ["c bleibt gleich, λ halbiert sich.", "c verdoppelt sich, λ bleibt gleich.",
               "c und λ verdoppeln sich.", "c halbiert sich, λ bleibt gleich."], [0], 1, "II",
              ["Wer bestimmt c?", "$c = \\lambda \\cdot f$ bleibt gleich, f wird doppelt so "
               "groß."],
              ["c hängt vom Wasser ab und bleibt gleich. Mit doppelter Frequenz wird λ halb "
               "so groß."]),
         ZAHL("Berechne die neue Wellenlänge.", 1.2, "m", 1, "II",
              ["Nutze dein Ergebnis aus b) mit der neuen Frequenz."],
              ["$f = \\dfrac{2}{1{,}6\\,s} = 1{,}25\\,Hz$, "
               "$\\lambda = \\dfrac{c}{f} = \\dfrac{1{,}5" + MS + "}{1{,}25\\,Hz} = 1{,}2\\,m$"])],
        abbildung={"typ": "yt_diagramm", "funktion": "sin", "ymax": 4.0, "T": 1.6,
                   "tmax": 3.2, "einheit_y": "cm", "raster": True})

L_LU = 340 / 440
L_WA = 1480 / 440
assert abs(L_LU - 0.773) < 0.001 and abs(L_WA - 3.36) < 0.01
aufgabe("W4-Z", "W4", "Z", "Stimmgabel unter Wasser",
        "Eine Stimmgabel schwingt mit 440 Hz. Ihr Ton wird einmal in Luft "
        "($340" + MS + "$) und einmal unter Wasser ($1480" + MS + "$) gemessen.",
        [ZAHL("Berechne die Wellenlänge in Luft.", r(L_LU, 2), "m", 1, "II",
              ["$\\lambda = \\dfrac{c}{f}$"],
              ["$\\lambda = \\dfrac{340" + MS + "}{440\\,Hz} \\approx 0{,}77\\,m$"], tol=0.03),
         ZAHL("Berechne die Wellenlänge im Wasser.", r(L_WA, 2), "m", 1, "II",
              ["Gleiche Frequenz, andere Ausbreitungsgeschwindigkeit."],
              ["$\\lambda = \\dfrac{1480" + MS + "}{440\\,Hz} \\approx 3{,}4\\,m$"], tol=0.03),
         SELBST("Ein Mitschüler meint: „Unter Wasser ist der Ton höher, weil sich der Schall "
                "dort schneller ausbreitet.“ Bewerte die Aussage.", 2, "III",
                ["Die Aussage ist falsch. Die Frequenz und damit die Tonhöhe bestimmt die "
                 "Stimmgabel als Erreger, sie bleibt 440 Hz.",
                 "Die größere Ausbreitungsgeschwindigkeit ändert nur die Wellenlänge: "
                 "$\\lambda = \\dfrac{c}{f}$ wird größer."],
                ["Wer bestimmt die Frequenz einer Welle?",
                 "Was ändert sich stattdessen?"],
                ["falsch: f vom Erreger, bleibt 440 Hz",
                 "größeres c gibt größeres λ"])])

diag("W4", "Aus welchem Diagramm liest man die Wellenlänge ab?",
     ["aus dem y(x)-Diagramm", "aus dem y(t)-Diagramm", "aus beiden", "aus keinem"], 0)
diag("W4", "λ = 2,0 m und f = 3,0 Hz. Die Ausbreitungsgeschwindigkeit ist …",
     ["$6{,}0" + MS + "$", "$0{,}67" + MS + "$", "$1{,}5" + MS + "$", "$5{,}0" + MS + "$"], 0)

# ------------------------------------------------------------------ W5
thema("W5", "Wellen", "Phase", "Deck 28",
      ["gleichphasig: $\\Delta s = k \\cdot \\lambda$",
       "gegenphasig: $\\Delta s = (2k + 1) \\cdot \\dfrac{\\lambda}{2}$",
       "$\\Delta \\varphi = 2\\pi \\cdot \\dfrac{\\Delta s}{\\lambda}$",
       "Eine Phasenbeziehung legt λ nur bis auf ganze Vielfache fest."])

aufgabe("W5-G1", "W5", "G", "Gleich- oder gegenphasig?",
        "Eine Seilwelle hat die Wellenlänge 0,80 m.",
        [WAHL("Zwei Seilstücke liegen 1,6 m auseinander. Sie schwingen …",
              ["gleichphasig", "gegenphasig", "weder gleich- noch gegenphasig"], [0], 1, "I",
              ["Wie viele Wellenlängen sind 1,6 m?"],
              ["$1{,}6\\,m = 2 \\cdot \\lambda$: gleichphasig"]),
         WAHL("Zwei Seilstücke liegen 1,2 m auseinander. Sie schwingen …",
              ["gegenphasig", "gleichphasig", "weder gleich- noch gegenphasig"], [0], 1, "I",
              ["Wie viele Wellenlängen sind 1,2 m?"],
              ["$1{,}2\\,m = 1{,}5 \\cdot \\lambda$, ungerades Vielfaches von "
               "$\\dfrac{\\lambda}{2}$: gegenphasig"])])

aufgabe("W5-G2", "W5", "G", "Phasendifferenz berechnen",
        "Die Momentaufnahme zeigt eine Seilwelle mit den Seilstücken P und Q.",
        [ZAHL("Lies den Abstand von P und Q ab.", 3.0, "m", 1, "I",
              ["Lies die x-Werte von P und Q ab und bilde die Differenz."],
              ["P bei 0,5 m, Q bei 3,5 m: $\\Delta s = 3{,}0\\,m$"]),
         ZAHL("Berechne die Phasendifferenz. Gib sie als Vielfaches von π an.", 3.0, "π", 1,
              "II",
              ["Lies zuerst λ ab.", "$\\Delta \\varphi = 2\\pi \\cdot "
               "\\dfrac{\\Delta s}{\\lambda}$"],
              ["λ = 2,0 m, $\\Delta \\varphi = 2\\pi \\cdot \\dfrac{3{,}0\\,m}{2{,}0\\,m} = "
               "3\\pi$"]),
         WAHL("Wie schwingen P und Q zueinander?",
              ["gegenphasig", "gleichphasig", "um eine Viertelperiode versetzt"], [0], 1, "II",
              ["Ist $3\\pi$ ein gerades oder ungerades Vielfaches von π?"],
              ["Ungerades Vielfaches von π: gegenphasig. Im Bild ist P im Berg und Q im "
               "Tal."])],
        abbildung={"typ": "yx_diagramm", "funktion": "sin", "ymax": 2.0, "lambda": 2.0,
                   "xmax": 4.0, "einheit_y": "cm", "einheit_x": "m", "raster": True,
                   "richtung": None, "punkte": [["P", 0.5], ["Q", 3.5]]})

assert abs(2 * 3.0 - 6.0) < 1e-12 and abs(1.5 / 6.0 - 0.25) < 1e-12
assert abs(3.0 / 2.0 - 1.5) < 1e-12 and abs(3.0 / 1.2 - 2.5) < 1e-12
aufgabe("W5-A", "W5", "A", "Zwei Korken",
        "Auf einem See schwimmen zwei Korken im Abstand von 3,0 m hintereinander in "
        "Ausbreitungsrichtung. Sie schwingen gegenphasig. Zwischen ihnen gibt es keine "
        "weitere Stelle, die gegenphasig zum ersten Korken schwingt. Die Welle breitet sich "
        "mit $1{,}5" + MS + "$ aus.",
        [ZAHL("Gib die Wellenlänge an.", 6.0, "m", 1, "II",
              ["Benachbarte gegenphasige Stellen liegen eine halbe Wellenlänge auseinander."],
              ["$\\dfrac{\\lambda}{2} = 3{,}0\\,m$, also λ = 6,0 m"]),
         ZAHL("Berechne die Frequenz, mit der die Korken schwingen.", 0.25, "Hz", 1, "II",
              ["Nutze dein Ergebnis aus a).", "$f = \\dfrac{c}{\\lambda}$"],
              ["$f = \\dfrac{1{,}5" + MS + "}{6{,}0\\,m} = 0{,}25\\,Hz$"]),
         WAHL("Ohne den Satz über die Stellen dazwischen wäre λ nicht eindeutig. Welche "
              "Wellenlängen würden dann ebenfalls passen? Wähle alle richtigen Antworten.",
              ["2,0 m", "1,2 m", "3,0 m", "1,5 m"], [0, 1], 1, "II",
              ["Gegenphasig heißt $\\Delta s = (2k + 1) \\cdot \\dfrac{\\lambda}{2}$.",
               "Prüfe für jede Wellenlänge, ob 3,0 m ein ungerades Vielfaches von "
               "$\\dfrac{\\lambda}{2}$ ist."],
              ["2,0 m: $3{,}0\\,m = 1{,}5 \\cdot \\lambda$, gegenphasig",
               "1,2 m: $3{,}0\\,m = 2{,}5 \\cdot \\lambda$, gegenphasig",
               "3,0 m und 1,5 m geben ganze Vielfache von λ: gleichphasig"], mehrfach=True),
         WAHL("Gib die Phasendifferenz der Korken für λ = 6,0 m an.",
              ["π", "2π", "$\\dfrac{\\pi}{2}$", "0"], [0], 1, "I",
              ["$\\Delta \\varphi = 2\\pi \\cdot \\dfrac{\\Delta s}{\\lambda}$"],
              ["$\\Delta \\varphi = 2\\pi \\cdot \\dfrac{3{,}0\\,m}{6{,}0\\,m} = \\pi$"])])

T5 = 1 / 2.5
DPHI5 = 2 * PI * 0.10 / T5
LAM5 = 2 * PI * 0.30 / DPHI5
assert abs(DPHI5 / PI - 0.5) < 1e-12 and abs(LAM5 - 1.2) < 1e-12
assert abs(LAM5 * 2.5 - 3.0) < 1e-12 and abs(0.30 / 0.10 - 3.0) < 1e-12
aufgabe("W5-Z", "W5", "Z", "Viertelperiode später",
        "Auf einem Seil läuft eine Welle mit 2,5 Hz. Das Seilstück Q liegt 0,30 m weiter vom "
        "Erreger entfernt als P. Q erreicht seinen höchsten Punkt 0,10 s später als P. "
        "Dazwischen erreicht kein anderer Wellenberg Q.",
        [ZAHL("Berechne die Phasendifferenz zwischen P und Q. Gib sie als Vielfaches von π "
              "an.", 0.5, "π", 1, "II",
              ["Welcher Bruchteil der Periodendauer sind 0,10 s?",
               "Eine ganze Periode entspricht $2\\pi$."],
              ["$T = \\dfrac{1}{2{,}5\\,Hz} = 0{,}40\\,s$",
               "$\\Delta \\varphi = 2\\pi \\cdot \\dfrac{0{,}10\\,s}{0{,}40\\,s} = "
               "\\dfrac{\\pi}{2}$"]),
         ZAHL("Berechne die Wellenlänge.", LAM5, "m", 1, "II",
              ["Stelle $\\Delta \\varphi = 2\\pi \\cdot \\dfrac{\\Delta s}{\\lambda}$ nach λ "
               "um und nutze dein Ergebnis aus a)."],
              ["$\\lambda = 2\\pi \\cdot \\dfrac{\\Delta s}{\\Delta \\varphi} = 2\\pi \\cdot "
               "\\dfrac{0{,}30\\,m}{\\pi / 2} = 1{,}2\\,m$"]),
         ZAHL("Berechne die Ausbreitungsgeschwindigkeit.", 3.0, "m/s", 1, "II",
              ["$c = \\lambda \\cdot f$"],
              ["$c = 1{,}2\\,m \\cdot 2{,}5\\,Hz = 3{,}0" + MS + "$",
               "Kontrolle: Der Berg legt 0,30 m in 0,10 s zurück, auch das gibt "
               "$3{,}0" + MS + "$."]),
         SELBST("Ein Mitschüler meint: „P und Q schwingen gleichphasig, denn beide "
                "erreichen denselben Wellenberg.“ Bewerte die Aussage.", 1, "III",
                ["Falsch: Gleichphasig hieße, beide erreichen den Berg gleichzeitig. Q ist "
                 "eine Viertelperiode später dran, die Phasendifferenz ist "
                 "$\\dfrac{\\pi}{2}$."],
                ["Was bedeutet gleichphasig?"],
                ["falsch, Q ist eine Viertelperiode später: $\\Delta \\varphi = "
                 "\\dfrac{\\pi}{2}$"])])

diag("W5", "λ = 1,0 m, $\\Delta s$ = 2,5 m. Die beiden Punkte schwingen …",
     ["gegenphasig", "gleichphasig", "um eine Viertelperiode versetzt", "gar nicht"], 0)
diag("W5", "Zwei Punkte schwingen gleichphasig. Ihr Abstand ist …",
     ["ein ganzes Vielfaches von λ", "ein ungerades Vielfaches von $\\dfrac{\\lambda}{2}$",
      "immer genau λ", "immer kleiner als λ"], 0)

# ========================================================================
#  MECHANISCHE SCHWINGUNGEN
# ========================================================================

# ------------------------------------------------------------------ S1
thema("S1", "Schwingungen", "Das Weg-Zeit-Gesetz", "Deck 18",
      ["$y(t) = y_{max} \\cdot \\sin(\\omega \\cdot t)$ mit $\\omega = \\dfrac{2\\pi}{T}$",
       "vier Startfälle: Ruhelage nach oben sin, oberer Umkehrpunkt cos, Ruhelage nach "
       "unten −sin, unterer Umkehrpunkt −cos",
       "Taschenrechner im Bogenmaß (RAD)"])

OM_S1 = 2 * PI / 0.80
assert abs(OM_S1 - 7.85) < 0.01
aufgabe("S1-G1", "S1", "G", "Start im oberen Umkehrpunkt",
        "Ein Federschwinger wird 2,5 cm nach oben ausgelenkt und losgelassen. Die "
        "Periodendauer beträgt 0,80 s.",
        [ZAHL("Berechne die Kreisfrequenz.", r(OM_S1), "1/s", 1, "I",
              ["$\\omega = \\dfrac{2\\pi}{T}$"],
              ["$\\omega = \\dfrac{2\\pi}{0{,}80\\,s} \\approx 7{,}85" + PS + "$"]),
         WAHL("Welches Weg-Zeit-Gesetz gilt? Gib y(t) an.",
              ["$2{,}5\\,cm \\cdot \\cos(7{,}85" + PS + " \\cdot t)$",
               "$2{,}5\\,cm \\cdot \\sin(7{,}85" + PS + " \\cdot t)$",
               "$-2{,}5\\,cm \\cdot \\cos(7{,}85" + PS + " \\cdot t)$",
               "$2{,}5\\,cm \\cdot \\cos(0{,}80\\,s \\cdot t)$"], [0], 1, "I",
              ["Welche Funktion hat bei t = 0 ihren größten Wert?"],
              ["Start im oberen Umkehrpunkt: cos mit positiver Amplitude"])])

Y_S1 = -3.0 * math.sin(2 * PI / 1.2 * 0.20)
assert abs(Y_S1 + 2.60) < 0.01
aufgabe("S1-G2", "S1", "G", "Gesetz aus dem Diagramm",
        "Das Diagramm zeigt die Elongation eines Federschwingers.",
        [WAHL("Welcher Startfall liegt vor?",
              ["Ruhelage nach unten, −sin", "Ruhelage nach oben, sin",
               "oberer Umkehrpunkt, cos", "unterer Umkehrpunkt, −cos"], [0], 1, "I",
              ["Wo beginnt die Kurve und wohin geht sie zuerst?"],
              ["Die Kurve beginnt bei null und geht nach unten: −sin."]),
         ZAHL("Lies die Periodendauer ab.", 1.2, "s", 1, "I",
              ["Nach welcher Zeit wiederholt sich die Kurve?"],
              ["T = 1,2 s"]),
         ZAHL("Berechne die Elongation nach 0,20 s.", r(Y_S1, 2), "cm", 1, "II",
              ["Stelle zuerst das Gesetz auf: $y(t) = -3{,}0\\,cm \\cdot \\sin(\\omega t)$.",
               "Taschenrechner im Bogenmaß, Vorzeichen beachten."],
              ["$\\omega = \\dfrac{2\\pi}{1{,}2\\,s} \\approx 5{,}24" + PS + "$",
               "$\\omega \\cdot t = 5{,}24" + PS + " \\cdot 0{,}20\\,s \\approx 1{,}05$",
               "$y = -3{,}0\\,cm \\cdot \\sin(1{,}05) \\approx -2{,}6\\,cm$"], tol=0.03)],
        abbildung={"typ": "yt_diagramm", "funktion": "-sin", "ymax": 3.0, "T": 1.2,
                   "tmax": 2.4, "einheit_y": "cm", "raster": True})

T_A = 16 / 20
OM_A = 2 * PI / T_A
Y_A = -5.0 * math.cos(OM_A * 0.30)
assert abs(T_A - 0.80) < 1e-12 and abs(Y_A - 3.54) < 0.01
aufgabe("S1-A", "S1", "A", "Losgelassen von unten",
        "Ein Körper an einer Feder wird 5,0 cm nach unten gezogen und zum Zeitpunkt t = 0 "
        "losgelassen. Er macht 20 Schwingungen in 16 s.",
        [ZAHL("Berechne die Periodendauer.", T_A, "s", 1, "I",
              ["Zeit durch Anzahl der Schwingungen."],
              ["$T = \\dfrac{16\\,s}{20} = 0{,}80\\,s$"]),
         WAHL("Welches Weg-Zeit-Gesetz gilt? Gib y(t) an.",
              ["$-5{,}0\\,cm \\cdot \\cos(7{,}85" + PS + " \\cdot t)$",
               "$5{,}0\\,cm \\cdot \\cos(7{,}85" + PS + " \\cdot t)$",
               "$-5{,}0\\,cm \\cdot \\sin(7{,}85" + PS + " \\cdot t)$",
               "$-5{,}0\\,cm \\cdot \\cos(0{,}80" + PS + " \\cdot t)$"], [0], 1, "II",
              ["Start im unteren Umkehrpunkt.", "Berechne ω aus deinem Ergebnis aus a)."],
              ["Start unten: −cos, $\\omega = \\dfrac{2\\pi}{0{,}80\\,s} \\approx "
               "7{,}85" + PS + "$"]),
         ZAHL("Berechne die Elongation nach 0,30 s.", r(Y_A, 2), "cm", 1, "II",
              ["Setze in das Gesetz aus b) ein, Taschenrechner im Bogenmaß."],
              ["$\\omega \\cdot t = 7{,}85" + PS + " \\cdot 0{,}30\\,s \\approx 2{,}36$",
               "$y = -5{,}0\\,cm \\cdot \\cos(2{,}36) \\approx 3{,}5\\,cm$"], tol=0.03),
         ZAHL("Gib an, wann der Körper zum ersten Mal den oberen Umkehrpunkt erreicht.", 0.40,
              "s", 1, "II",
              ["Vom unteren zum oberen Umkehrpunkt ist es eine halbe Periode."],
              ["$t = \\dfrac{T}{2} = 0{,}40\\,s$"])])

assert abs(-10 * math.sin(PI * (7 / 6)) - 5.0) < 1e-9
assert abs(7 / 6 - 1.1667) < 1e-3
aufgabe("S1-Z", "S1", "Z", "Wann ist er oben?",
        "Ein Federschwinger ist zum Zeitpunkt t = 0 in der Ruhelage und bewegt sich nach "
        "unten. Amplitude 10 cm, Periodendauer 2,0 s.",
        [WAHL("Welches Weg-Zeit-Gesetz gilt? Gib y(t) an.",
              ["$-10\\,cm \\cdot \\sin(3{,}14" + PS + " \\cdot t)$",
               "$10\\,cm \\cdot \\sin(3{,}14" + PS + " \\cdot t)$",
               "$-10\\,cm \\cdot \\cos(3{,}14" + PS + " \\cdot t)$",
               "$-10\\,cm \\cdot \\sin(2{,}0" + PS + " \\cdot t)$"], [0], 1, "II",
              ["Start in der Ruhelage nach unten.", "$\\omega = \\dfrac{2\\pi}{2{,}0\\,s}$"],
              ["−sin, $\\omega = \\pi" + PS + " \\approx 3{,}14" + PS + "$"]),
         ZAHL("Berechne, wann der Körper zum ersten Mal 5,0 cm über der Ruhelage ist.",
              r(7 / 6), "s", 2, "III",
              ["Setze y = 5,0 cm in das Gesetz aus a) ein und stelle nach "
               "$\\sin(\\omega t)$ um.",
               "$\\sin(\\pi \\cdot t) = -0{,}5$. Der Taschenrechner liefert eine negative "
               "Zeit. Überlege mit dem Verlauf der Kurve, wann der Körper zum ersten Mal "
               "oben ankommt.",
               "Nach einer halben Periode (1,0 s) geht er wieder durch die Ruhelage nach "
               "oben. Danach braucht er für 5,0 cm noch $\\dfrac{T}{12}$."],
              ["$-10\\,cm \\cdot \\sin(\\pi \\cdot t) = 5{,}0\\,cm$",
               "also $\\sin(\\pi \\cdot t) = -0{,}5$",
               "Zuerst geht der Körper nach unten. Nach 1,0 s ist er wieder in der Ruhelage "
               "und bewegt sich nach oben.",
               "$\\pi \\cdot t = \\pi + \\dfrac{\\pi}{6}$, also $t = \\dfrac{7}{6}\\,s "
               "\\approx 1{,}17\\,s$"], tol=0.03),
         WAHL("In welche Richtung bewegt sich der Körper zu diesem Zeitpunkt?",
              ["nach oben", "nach unten", "er ist in Ruhe"], [0], 1, "II",
              ["Wo war er 0,17 s vorher?"],
              ["Er kommt aus der Ruhelage und ist auf dem Weg zum oberen Umkehrpunkt: nach "
               "oben."])])

diag("S1", "Ein Schwinger startet im unteren Umkehrpunkt. Das Gesetz enthält …",
     ["−cos", "cos", "sin", "−sin"], 0)
diag("S1", "T = 0,50 s. Die Kreisfrequenz ist …",
     ["$12{,}6" + PS + "$", "$3{,}14" + PS + "$", "$2{,}0" + PS + "$", "$0{,}50" + PS + "$"], 0)

# ------------------------------------------------------------------ S2
thema("S2", "Schwingungen", "Geschwindigkeit und Beschleunigung", "Deck 19",
      ["$v(t) = y'(t)$ und $a(t) = y''(t)$ (nach t ableiten, Kettenregel)",
       "$v_{max} = y_{max} \\cdot \\omega$ in der Ruhelage",
       "$a_{max} = y_{max} \\cdot \\omega^2$ in den Umkehrpunkten",
       "a zeigt immer zur Ruhelage"])

aufgabe("S2-G1", "S2", "G", "Größte Werte",
        "Für einen Federschwinger gilt $y(t) = 4{,}0\\,cm \\cdot \\sin(10" + PS + " \\cdot t)$.",
        [ZAHL("Berechne die größte Geschwindigkeit.", 0.40, "m/s", 1, "I",
              ["$v_{max} = y_{max} \\cdot \\omega$, Amplitude in Meter."],
              ["$v_{max} = 0{,}040\\,m \\cdot 10" + PS + " = 0{,}40" + MS + "$"]),
         ZAHL("Berechne die größte Beschleunigung.", 4.0, "m/s²", 1, "I",
              ["$a_{max} = y_{max} \\cdot \\omega^2$"],
              ["$a_{max} = 0{,}040\\,m \\cdot (10" + PS + ")^2 = 4{,}0" + MS2 + "$"])])

aufgabe("S2-G2", "S2", "G", "Ableiten und deuten",
        "Ein Federschwinger startet im oberen Umkehrpunkt: "
        "$y(t) = y_{max} \\cdot \\cos(\\omega \\cdot t)$.",
        [WAHL("Welches v-t-Gesetz gilt?",
              ["$v(t) = -y_{max} \\cdot \\omega \\cdot \\sin(\\omega t)$",
               "$v(t) = y_{max} \\cdot \\omega \\cdot \\sin(\\omega t)$",
               "$v(t) = y_{max} \\cdot \\omega \\cdot \\cos(\\omega t)$",
               "$v(t) = -y_{max} \\cdot \\sin(\\omega t)$"], [0], 1, "II",
              ["Die Ableitung von cos ist −sin.", "Kettenregel: innere Ableitung ω."],
              ["$v(t) = y'(t) = -y_{max} \\cdot \\omega \\cdot \\sin(\\omega t)$"]),
         WAHL("Wo ist die Beschleunigung am größten?",
              ["in den Umkehrpunkten", "in der Ruhelage", "überall gleich",
               "auf halbem Weg"], [0], 1, "I",
              ["$a = -\\omega^2 \\cdot y$"],
              ["Bei größter Auslenkung ist $|a|$ am größten: in den Umkehrpunkten."]),
         WAHL("Der Körper ist gerade über der Ruhelage. Wohin zeigt seine Beschleunigung?",
              ["nach unten, zur Ruhelage", "nach oben", "in Bewegungsrichtung",
               "sie ist null"], [0], 1, "I",
              ["Die Rückstellkraft zeigt zur Ruhelage."],
              ["a zeigt immer zur Ruhelage, hier also nach unten."])])

OM_N = 2 * PI * 10
V_N = 0.015 * OM_N
A_N = 0.015 * OM_N ** 2
V_N01 = -0.015 * OM_N * math.cos(OM_N * 0.010)
assert abs(V_N - 0.942) < 0.001 and abs(A_N - 59.2) < 0.1 and abs(V_N01 + 0.762) < 0.001
aufgabe("S2-A", "S2", "A", "Nähmaschinennadel",
        "Die Nadel einer Nähmaschine bewegt sich näherungsweise harmonisch mit der Frequenz "
        "10 Hz und der Amplitude 1,5 cm. Zum Zeitpunkt t = 0 geht sie durch die Ruhelage nach "
        "unten.",
        [ZAHL("Berechne die größte Geschwindigkeit der Nadel.", r(V_N, 2), "m/s", 1, "II",
              ["Zuerst $\\omega = 2\\pi \\cdot f$.", "$v_{max} = y_{max} \\cdot \\omega$"],
              ["$\\omega = 2\\pi \\cdot 10\\,Hz \\approx 62{,}8" + PS + "$",
               "$v_{max} = 0{,}015\\,m \\cdot 62{,}8" + PS + " \\approx 0{,}94" + MS + "$"],
              tol=0.03),
         ZAHL("Berechne die größte Beschleunigung der Nadel.", r(A_N, 2), "m/s²", 1, "II",
              ["$a_{max} = y_{max} \\cdot \\omega^2$"],
              ["$a_{max} = 0{,}015\\,m \\cdot (62{,}8" + PS + ")^2 \\approx 59" + MS2 + "$"],
              tol=0.03),
         ZAHL("Berechne die Geschwindigkeit der Nadel 0,010 s nach dem Start (oben "
              "positiv).", r(V_N01, 2), "m/s", 1, "II",
              ["Startfall Ruhelage nach unten: $y(t) = -y_{max} \\cdot \\sin(\\omega t)$.",
               "Ableiten: $v(t) = -y_{max} \\cdot \\omega \\cdot \\cos(\\omega t)$. "
               "Bogenmaß!"],
              ["$\\omega \\cdot t = 62{,}8" + PS + " \\cdot 0{,}010\\,s \\approx 0{,}628$",
               "$v = -0{,}94" + MS + " \\cdot \\cos(0{,}628) \\approx -0{,}76" + MS + "$",
               "Die Nadel bewegt sich nach unten."], tol=0.03),
         WAHL("Wie oft pro Sekunde erreicht die Nadel ihre größte Geschwindigkeit (nach oben "
              "oder unten)?",
              ["20-mal", "10-mal", "5-mal", "40-mal"], [0], 1, "II",
              ["Wie oft geht die Nadel in einer Periode durch die Ruhelage?"],
              ["Zweimal pro Periode, bei 10 Hz also 20-mal pro Sekunde."])])

YMAX_B = G / (2 * PI * 50) ** 2
assert abs(YMAX_B * 1000 - 0.0994) < 0.0005
aufgabe("S2-Z", "S2", "Z", "Der hüpfende Ball",
        "Auf einer waagerechten Platte liegt ein leichter Ball. Die Platte schwingt mit 50 Hz "
        "auf und ab. Erhöht man die Amplitude langsam, beginnt der Ball ab einer bestimmten "
        "Amplitude zu hüpfen.",
        [SELBST("Begründe, an welcher Stelle der Schwingung der Ball zuerst abhebt und unter "
                "welcher Bedingung.", 2, "III",
                ["Im oberen Umkehrpunkt ist die Beschleunigung der Platte am größten und zeigt "
                 "nach unten.",
                 "Ist sie größer als die Fallbeschleunigung g, kann der Ball der Platte nicht "
                 "mehr folgen und hebt ab: $a_{max} > g$."],
                ["Wo ist die Beschleunigung am größten und wohin zeigt sie dort?",
                 "Mit welcher Beschleunigung fällt der Ball höchstens nach unten?"],
                ["oberer Umkehrpunkt: a maximal, nach unten",
                 "Bedingung $a_{max} > g$"]),
         ZAHL("Berechne die Amplitude, ab der der Ball abhebt. Gib sie in mm an.",
              r(YMAX_B * 1000, 2), "mm", 2, "II",
              ["Setze $a_{max} = g$.", "$y_{max} = \\dfrac{g}{\\omega^2}$ mit "
               "$\\omega = 2\\pi \\cdot 50\\,Hz$"],
              ["$\\omega = 2\\pi \\cdot 50\\,Hz \\approx 314" + PS + "$",
               "$y_{max} = \\dfrac{9{,}81" + MS2 + "}{(314" + PS + ")^2} \\approx "
               "9{,}9 \\cdot 10^{-5}\\,m$",
               "Das sind etwa 0,099 mm."], tol=0.03)])

diag("S2", "Wo ist die Geschwindigkeit eines Federschwingers null?",
     ["in den Umkehrpunkten", "in der Ruhelage", "nirgends", "überall"], 0)
diag("S2", "Die größte Beschleunigung ist …",
     ["$y_{max} \\cdot \\omega^2$", "$y_{max} \\cdot \\omega$", "$\\omega^2$",
      "$\\dfrac{y_{max}}{\\omega}$"], 0)

# ------------------------------------------------------------------ S3
thema("S3", "Schwingungen", "Federschwinger und Resonanz", "Decks 14 und 21",
      ["$T = 2\\pi \\cdot \\sqrt{\\dfrac{m}{D}}$ und $f_0 = \\dfrac{1}{T}$",
       "Erregerfrequenz und Eigenfrequenz unterscheiden",
       "kleiner als $f_0$: gleichphasig, etwa Erregeramplitude. Größer als $f_0$: "
       "gegenphasig, sehr kleine Amplitude",
       "Resonanz bei Erregerfrequenz gleich Eigenfrequenz: Energiezufuhr in jeder Periode",
       "Schutz: Eigenfrequenz verschieben, Dämpfung erhöhen"])

T_S3 = 2 * PI * math.sqrt(0.50 / 20)
assert abs(T_S3 - 0.993) < 0.001
aufgabe("S3-G1", "S3", "G", "Eigenfrequenz",
        "Ein Körper der Masse 500 g schwingt an einer Feder mit $D = 20\\,\\tfrac{N}{m}$.",
        [ZAHL("Berechne die Periodendauer.", r(T_S3, 2), "s", 1, "I",
              ["$T = 2\\pi \\cdot \\sqrt{\\dfrac{m}{D}}$, Masse in kg."],
              ["$T = 2\\pi \\cdot \\sqrt{\\dfrac{0{,}50\\,kg}{20\\,\\tfrac{N}{m}}} \\approx "
               "0{,}99\\,s$"], tol=0.03),
         ZAHL("Berechne die Eigenfrequenz.", r(1 / T_S3, 2), "Hz", 1, "I",
              ["$f_0 = \\dfrac{1}{T}$ mit deinem Ergebnis aus a)."],
              ["$f_0 = \\dfrac{1}{0{,}99\\,s} \\approx 1{,}0\\,Hz$"], tol=0.03)])

aufgabe("S3-G2", "S3", "G", "Erzwungene Schwingung",
        "Ein Federschwinger mit der Eigenfrequenz $f_0$ wird am oberen Federende periodisch "
        "angeregt.",
        [WAHL("Die Erregerfrequenz ist deutlich kleiner als $f_0$. Der Körper schwingt …",
              ["gleichphasig mit etwa der Amplitude des Erregers",
               "gegenphasig mit sehr kleiner Amplitude", "mit wachsender Amplitude",
               "mit seiner Eigenfrequenz"], [0], 1, "I",
              ["Bei langsamer Anregung bewegt sich der Körper mit."],
              ["kleiner als $f_0$: gleichphasig, etwa Erregeramplitude"]),
         WAHL("Die Erregerfrequenz ist deutlich größer als $f_0$. Der Körper schwingt …",
              ["gegenphasig mit sehr kleiner Amplitude",
               "gleichphasig mit etwa der Amplitude des Erregers",
               "mit wachsender Amplitude", "gar nicht"], [0], 1, "I",
              ["Kann der träge Körper einer schnellen Anregung folgen?"],
              ["größer als $f_0$: gegenphasig, sehr kleine Amplitude"]),
         WAHL("Die Erregerfrequenz ist gleich $f_0$. Was geschieht?",
              ["Resonanz: In jeder Periode wird Energie zugeführt, die Amplitude wächst.",
               "Die Schwingung kommt zur Ruhe.",
               "Der Körper schwingt mit doppelter Frequenz.",
               "Die Amplitude bleibt genau gleich der des Erregers."], [0], 1, "I",
              ["Wann wird in jeder Periode Energie zugeführt?"],
              ["Resonanz: Energiezufuhr in jeder Periode, die Amplitude wächst bis zur "
               "Grenze durch die Dämpfung."])])

F0_SP = 1 / (2 * PI) * math.sqrt(320 / 0.20)
assert abs(F0_SP - 6.37) < 0.01 and abs(F0_SP * 60 - 382) < 1
aufgabe("S3-A", "S3", "A", "Zitternder Rückspiegel",
        "Der Rückspiegel eines Motorrads verhält sich wie ein Federschwinger mit der Masse "
        "0,20 kg und $D = 320\\,\\tfrac{N}{m}$. Der Motor regt ihn bei jeder Umdrehung "
        "einmal an. Die Drehzahl wird in Umdrehungen pro Minute angegeben.",
        [ZAHL("Berechne die Eigenfrequenz des Spiegels.", r(F0_SP, 2), "Hz", 1, "I",
              ["$T = 2\\pi \\cdot \\sqrt{\\dfrac{m}{D}}$, dann $f_0 = \\dfrac{1}{T}$."],
              ["$T = 2\\pi \\cdot \\sqrt{\\dfrac{0{,}20\\,kg}{320\\,\\tfrac{N}{m}}} \\approx "
               "0{,}157\\,s$, $f_0 \\approx 6{,}4\\,Hz$"], tol=0.03),
         ZAHL("Berechne die Drehzahl, bei der der Spiegel besonders stark zittert.",
              r(F0_SP * 60, 2), "1/min", 1, "II",
              ["Resonanz: Erregerfrequenz gleich Eigenfrequenz.",
               "Die Erregerfrequenz in Hz gibt die Umdrehungen pro Sekunde an. Rechne in "
               "Umdrehungen pro Minute um."],
              ["Resonanz bei 6,4 Umdrehungen pro Sekunde",
               "$6{,}37\\,Hz \\cdot 60\\,s \\approx 380$ Umdrehungen pro Minute"], tol=0.03),
         SELBST("Schlage zwei Maßnahmen gegen das Zittern vor und begründe sie.", 2, "II",
                ["Eigenfrequenz verschieben, z. B. steifere Halterung (größeres D, größeres "
                 "$f_0$), sodass die Resonanz bei einer Drehzahl liegt, die kaum gefahren "
                 "wird.",
                 "Dämpfung erhöhen, z. B. Gummilager: Die Amplitude bleibt auch bei Resonanz "
                 "klein."],
                ["Wovon hängt die Eigenfrequenz ab?",
                 "Was begrenzt die Amplitude bei Resonanz?"],
                ["Eigenfrequenz verschieben (D oder m ändern)", "Dämpfung erhöhen"])])

F0_KW = 1 / (2 * PI) * math.sqrt(2400 / 12)
T0_KW = 1 / F0_KW
assert abs(F0_KW - 2.25) < 0.01 and abs(0.50 / 1.0 - 0.50) < 1e-12
assert abs(0.50 / T0_KW - 1.125) < 0.005
aufgabe("S3-Z", "S3", "Z", "Kinderwagen auf Gehwegplatten",
        "Ein Kinderwagen wird über einen Gehweg geschoben. Die Fugen zwischen den Platten "
        "liegen 0,50 m auseinander. Bei jeder Fuge wird die Wanne einmal angestoßen. Die "
        "Wanne mit Kind (12 kg) schwingt auf Federn mit insgesamt "
        "$D = 2400\\,\\tfrac{N}{m}$.",
        [ZAHL("Berechne die Eigenfrequenz der Wanne.", r(F0_KW, 2), "Hz", 1, "I",
              ["$T = 2\\pi \\cdot \\sqrt{\\dfrac{m}{D}}$, $f_0 = \\dfrac{1}{T}$"],
              ["$T = 2\\pi \\cdot \\sqrt{\\dfrac{12\\,kg}{2400\\,\\tfrac{N}{m}}} \\approx "
               "0{,}44\\,s$, $f_0 \\approx 2{,}3\\,Hz$"], tol=0.03),
         ZAHL("Der Wagen wird mit $1{,}0" + MS + "$ geschoben. Berechne die Frequenz, mit der "
              "die Wanne angeregt wird.", 2.0, "Hz", 1, "II",
              ["Berechne zuerst die Zeit von Fuge zu Fuge mit "
               "$v = \\dfrac{s}{t}$.", "Die Erregerfrequenz ist der Kehrwert dieser Zeit."],
              ["$t = \\dfrac{0{,}50\\,m}{1{,}0" + MS + "} = 0{,}50\\,s$, "
               "$f = \\dfrac{1}{0{,}50\\,s} = 2{,}0\\,Hz$"]),
         ZAHL("Berechne die Geschwindigkeit, bei der die Wanne am stärksten schwingt.",
              r(0.50 / T0_KW, 2), "m/s", 1, "II",
              ["Resonanz: Die Zeit von Fuge zu Fuge ist gleich der Periodendauer aus a).",
               "$v = \\dfrac{s}{T}$"],
              ["$v = \\dfrac{0{,}50\\,m}{0{,}44\\,s} \\approx 1{,}1" + MS + "$"], tol=0.03),
         SELBST("Ein Vater meint: „Mit härteren Federn kommt das starke Schaukeln schon "
                "bei langsamerem Schieben.“ Bewerte die Aussage.", 1, "III",
                ["Falsch: Mit größerem D wird T kleiner und $f_0$ größer. Die Resonanz liegt "
                 "dann bei einer größeren Geschwindigkeit."],
                ["Wie ändert sich T, wenn D größer wird?"],
                ["falsch: größeres D, kleineres T, Resonanz bei größerer Geschwindigkeit"])])

diag("S3", "Bei Resonanz ist …",
     ["die Erregerfrequenz gleich der Eigenfrequenz", "die Amplitude null",
      "die Erregerfrequenz doppelt so groß wie die Eigenfrequenz",
      "die Dämpfung besonders groß"], 0)
diag("S3", "Die Masse an einer Feder wird vervierfacht. Die Periodendauer …",
     ["verdoppelt sich", "vervierfacht sich", "halbiert sich", "bleibt gleich"], 0)


# ========================================================================
#  Prüfung und Ausgabe
# ========================================================================
def statistik():
    be = {"I": 0, "II": 0, "III": 0}
    for a in AUFGABEN:
        for t in a["teile"]:
            be[t["afb"]] += t["be"]
    s = sum(be.values())
    return be, s


VERBOTEN = ("Takt", "innere Energie", "Energieverlust", ";", " – ", "ŷ", ", und ")

if __name__ == "__main__":
    ids = [a["id"] for a in AUFGABEN]
    assert len(ids) == len(set(ids))
    for a in AUFGABEN:
        assert a["thema"] in {t["id"] for t in THEMEN}
        for t in a["teile"]:
            p = t["pruefung"]
            assert t["hilfen"] and t["loesung"], a["id"]
            assert 1 <= len(t["hilfen"]) <= 3, a["id"]
            if p["typ"] == "auswahl":
                assert all(0 <= i < len(p["optionen"]) for i in p["richtig"])
            text = " ".join([a["kontext"], a["titel"], t["text"]] + t["hilfen"] + t["loesung"]
                            + p.get("kriterien", []) + p.get("optionen", []))
            for verboten in VERBOTEN:
                assert verboten not in text, (a["id"], verboten)
    rest = " ".join([str(x) for d in DIAGNOSE for x in [d["frage"]] + d["optionen"]]
                    + [c for t in THEMEN for c in t["checkliste"] + [t["titel"]]])
    for verboten in VERBOTEN:
        assert verboten not in rest, verboten
    for t in THEMEN:
        assert len([a for a in AUFGABEN if a["thema"] == t["id"]]) == 4, t["id"]
        assert len([d for d in DIAGNOSE if d["thema"] == t["id"]]) == 2, t["id"]
    be, s = statistik()
    print("Themen:", len(THEMEN), "Aufgaben:", len(AUFGABEN), "Teile:",
          sum(len(a["teile"]) for a in AUFGABEN), "BE:", s)
    print("AFB:", {k: "%d BE (%.0f %%)" % (v, 100 * v / s) for k, v in be.items()})
    print("Diagnosefragen:", len(DIAGNOSE))
    daten = {"meta": {"titel": "Lerntheke Test 2", "kurs": "Physik GK 12",
                      "untertitel": "Mechanische Schwingungen und Wellen",
                      "klausur": "Mi 25.11.2026, 45 min, Mechanische Schwingungen und Wellen",
                      "probe": "Probetest", "stand": "2026-11-17", "tempo_min_je_be": 2.2,
                      "bereiche": BEREICHE},
             "themen": THEMEN, "aufgaben": AUFGABEN, "diagnose": DIAGNOSE}
    with open("aufgaben.json", "w", encoding="utf8") as f:
        json.dump(daten, f, ensure_ascii=False, indent=1)
    print("aufgaben.json geschrieben")
