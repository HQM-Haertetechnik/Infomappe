# Projekt Infomappe HQM Härtetechnik

**Stand:** 15.10.2026 · **Verantwortlich:** Carsten Klinke · **Status:** Versandfassung erstellt, Übernahme in `main` offen

## 1. Ziel

Die alte Infomappe (`Ausgangsmaterial/HQM Infobroschüre.pdf`, 14 Seiten, Canva 2025) wird als **eine einzige HTML-Datei** neu aufgebaut:

- Versand als Mailanhang, Zielgröße höchstens 4 bis 6 MB
- Corporate Design nach `styleguide-hqm.pdf` (v1.0, 18.09.2025): Onyx #122436, Anthrazit #475F6A, Off-White #CFCFCF, Ember #A4302F, Schrift Open Sans
- hell, viel Weiß, sachlich im B2B-Stil
- funktioniert am Desktop, auf dem Handy und im A4-Druck (13 Seiten)
- keine erfundenen Inhalte; gefundene Fehler werden korrigiert und dokumentiert

## 2. Ergebnis

| Datei | Inhalt |
|---|---|
| `Infomappe_HTML/HQM_Haertetechnik_Infomappe.html` | Versandfassung, 2,7 MB, alle Bilder und die Schrift eingebettet, keine Internetverbindung nötig |
| `Infomappe_HTML/HQM_Haertetechnik_Infomappe_Druckkontrolle_A4.pdf` | Kontrollausdruck A4, 13 Seiten |
| `Infomappe_HTML/Aenderungen_Entwurf_v1.md` | Änderungstabelle gegenüber der alten Mappe (Stand Entwurf v1, siehe offene Punkte) |
| `Infomappe_HTML/quelle/` | Quelle zum Neubauen: `vorlage.html`, `build.py`, `assets/`, `font/`, `original/` |
| `Zertifikate/ISO50001_GUTcert_B-24-13897_2024.pdf` | Zertifikat DIN EN ISO 50001 mit Anlage (Geltungsbereich) |

## 3. Aufbau der neuen Mappe

| Seite | Inhalt | Wesentliche Änderung gegenüber alt |
|---|---|---|
| 01 | Titel | Logo, aktiver Link zur Homepage, Schachtofenbild, Feld in Onyx |
| 02 | Unternehmensvorstellung | Blocksatz |
| 03 | Wärmebehandlungsprozesse | Historienleiste durch Gebäudefoto Leipzig ersetzt |
| 04 | Beratung und Qualität | Historie und Foto ersetzt durch Grafik „Customer Journey“ (nach Folie 17 der Präsentation `PR_20260713_HQM Härtetechnik.pptx`), Hintergrund Onyx |
| 05 | Anlagenportfolio | Tabelle als Text statt Bild, auf dem Handy als Karten |
| 06 | Werkstoffprüfung und Labor | Icons in Anthrazit |
| 07 | Ansprechpartner | „Das sind wir“ entfallen; Arbeitsvorbereitung jetzt Adrian E. Ocampo |
| 08 | Neue Technologien | Kopfbild und Überschrift „E-Mobilität“ entfallen; Projektkasten zweispaltig; Text um ca. 100 Wörter aus der Website ergänzt |
| 09–11 | Anlagen im Detail | kleine Bilder einheitlich groß und mittig zum Text; S. 10 Ofenbild zugeschnitten, fünf Icons zu den Vorteilen |
| 12 | Zertifikate | IATF 16949 Leipzig und Wuppertal (DNV), DIN EN ISO 50001 (GUTcert) |
| 13 | Kontakt | Standortkasten in Onyx mit weißer Schrift; QR-Code auf www.hqm-haertetechnik.de |

## 4. Prüfungen (15.10.2026)

- **Links:** Homepage-Links (Titel, Logos, Kontaktseite) führen auf https://www.hqm-haertetechnik.de/, die Seite war erreichbar. Der QR-Code liefert beim Auslesen dieselbe Adresse. Alle E-Mail- und Telefon-Links sind anklickbar, auch im PDF. Ob die Postfächer existieren, wurde nicht geprüft.
- **Darstellung:** Bei Breiten von 1440, 1280, 768, 390 und 360 Pixeln ragt kein Element über den Rand, alle Bilder laden, die Schrift ist eingebettet.
- **Druck:** A4, genau 13 Seiten, jede Seite beginnt mit dem richtigen Inhalt.
- **Reproduzierbarkeit:** `build.py` erzeugt aus `quelle/` eine Datei, die Byte für Byte der Versandfassung entspricht.
- **Texte:** Gesamttext (ca. 1.350 Wörter) mit LanguageTool 6.8 lokal geprüft. Die 63 Meldungen sind Fehlalarme: Fachbegriffe und Namen (z. B. Carbonitrieren, Bainitisieren, AICHELIN, GUTcert), Großschreibung nach Überschriften und gleichlautende Tabellenzellen. Kein Korrekturbedarf.

## 5. Bearbeitung und Neubau

1. Inhalte in `quelle/vorlage.html` ändern. Bearbeitbare Stellen sind mit `BEARBEITBAR` markiert, die Ansprechpartner stehen im gleichnamigen Block.
2. Neue Bilder in `quelle/assets/` ablegen und in der Vorlage als `{{dateiname_ohne_endung}}` einsetzen.
3. Bauen: `cd quelle && python3 build.py ../HQM_Haertetechnik_Infomappe.html`. Für sauberen Blocksatz wird das Python-Paket `pyphen` benötigt (setzt weiche Trennstriche); ohne `pyphen` baut die Datei trotzdem, nur ohne Silbentrennung.
4. Prüfen: Desktop, Handy, Druckvorschau A4 (13 Seiten).

Die Schrift Open Sans stammt aus dem npm-Paket `@fontsource/open-sans` 5.0.28 (SIL Open Font License).

## 6. Entscheidungen

- Versand als HTML-Mailanhang, 4 bis 6 MB sind in Ordnung.
- Normbezeichnung einheitlich „DIN EN ISO 50001“.
- Ansprechpartner werden nur im HTML-Code gepflegt.
- Jahreszahlen wurden nicht neu eingefügt, weil die Website („27 Jahre Erfahrung“) und die alte Mappe („seit 1993“) nicht übereinstimmen.
- Die Zertifikatsanlage zu ISO 50001 nennt die Standorte Leipzig (Fraunhoferstraße, Ludwig-Hupfeld-Straße) und Wuppertal. Die Aussage auf Seite 4, beide Standorte seien zertifiziert, ist damit belegt.

## 7. Offene Punkte

| Punkt | Wer |
|---|---|
| Übernahme in `main` per Pull Request | Freigabe Carsten |
| Schreibweise `Adrian.Ocampo@hqm-gruppe.de` (Großbuchstaben) bestätigen | Carsten |
| Rote Hervorhebung der Schritte 3, 6 und 8 in der Customer Journey beibehalten? | Carsten |
| Ergänzten Text auf Seite 8 freigeben | Carsten |
| Bild der Festigkeitsstrahlanlage (S. 11) nur in geringer Auflösung vorhanden, bessere Fassung liefern | Carsten |
| Änderungstabelle auf den Stand der Versandfassung fortschreiben | Claude |

## 8. Verlauf

| Version | Inhalt |
|---|---|
| v1–v2 | Grundaufbau im Corporate Design, Anlagentabelle als Text, Zertifikate |
| v3 | Ansprechpartner Arbeitsvorbereitung: Adrian E. Ocampo |
| v4 | Gebäudefoto Seite 3 |
| v5–v6 | Customer Journey Seite 4, Hintergrund Onyx |
| v7 | Seite 8 neu aufgebaut, Text aus der Website ergänzt |
| v8 | Blocksatz mit Silbentrennung auf S. 2, 4, 8–11 |
| v9–v10 | Bilder S. 9–11 vereinheitlicht, Icons S. 10 |
| v11 | Zertifikat DIN EN ISO 50001 eingesetzt |
| v12 | QR-Code auf hqm-haertetechnik.de, Standortkasten in Onyx |
| v13 | Links geprüft und verbessert, Versandfassung |
