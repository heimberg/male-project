# PVA-02
## Vorgehen CSV Dateien
1. Erste Zeile aus Dateien '\PVA-02\Datensatz\CSVs\Datensatz-CorneliaIsenschmid.csv' und '\PVA-02\Datensatz\CSVs\Datensatz_VivianeRogenmoser.csv' manuell entfernt, da diese Zeilen keine Daten enthalten.
2. Erste Spalte aus Datei '\PVA-02\Datensatz\CSVs\Datensatz_VivianeRogenmoser.csv' manuell entfernt, da diese keine Daten enthält
3. Python Skript erstellt in welchem die folgenden Schritte nacheinander durchgeführt werden:
   1. Leere Zeilen aus allen CSV Dateien entfernen (dies betrifft nur die Datei '\PVA-02\Datensatz\CSVs\Datensatz_OlgaEngelmann.csv' aber wäre manuell zu aufwändig)
   2. Eine Datei enthält 'kreuz', 'kreis', 'plus', 'minus' und 'gartenhag' an Stelle von 'x', 'o', '+', '-' und '#'. Diese werden durch die entsprechenden Zeichen ersetzt.
   3. Eine Datei enthält 'True' und 'False' an Stelle von '1' und '0'. Diese werden durch die entsprechenden Zeichen ersetzt, zugleich werden die Pixelwerte auf 1 normiert. So enthalten alle Spalten mit Pixelwerten ausschliesslich 0 und 1.
   4. Sämtliche Zahlenwerte werden in Integer umgewandelt.

Das dazu verwendete Skript ist unter '\PVA-02\cleanup-csv.py' zu finden. Die korrigierten CSV Dateien sind unter '\PVA-02\Datensatz\CSVs\corrected' zu finden.

## Vorgehen Bilddateien
1. Prüfung ob das Bild eine Grösse von 10x10 Pixeln hat. Falls nicht, wird das Bild auf 10x10 Pixel skaliert.
2. Anpassen der Dateinamen gemäss der Vorgaben in der Aufgabenstellung.

## Resultate
Die Dateien werden durch die beiden Skripte so umgewandelt, dass diese sowohl in Dateinamen wie auch im Inhalt mit der Aufgabenstellung aus PVA-01 übereinstimmen. Folgende Punkte wurden dabei angepasst:
- Dateinamen gemäss Konvention
- Bildgrösse skaliert auf 10x10 Pixel 
- Pixelwerte auf 0 und 1 normiert
- Pixelwerte in positive Bilddateien umgewandelt (mehr '0' als '1')
