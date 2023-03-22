# Aufgabe PVA-01
## Aufgabenstellung 
Datensatz aus Bildern der Zeichen 'x', 'o' und '+' erstellen. Anschliessend igitalisieren diese Bilder. Die digitalen Bilder werden mittels eines Python Skripts in einen Datensatz umgewandelt. 
## Vorgehen
Die Zeichen wurden mit einem Zeichenpad erstellt und in einer Datei im Format png gespeichert. Anschliessend wurde ein Pythons-Skript erstellt, welches die Bilder einzeln aus der Datei ausschneidet und in insgesamt 30 Einzelbilder abspeichert (`generate.py`). Das darauffolgend erstellte Skript `reformat.py` wandelt die Bilder in das gewünschte Format um und speichert deren Pixelwerte in einer Datei (`Datensatz-matthias.heimberg.csv`) ab (binäre Darstellung). Die Schritte können mit den in dem Repository enthaltenen Dateien reproduziert werden.
### Skript `generate.py`
- Programm extrahiert Symbole aus dem handgezeichnetem Bild und speichert diese in Ordner
- Bild wird geladen und in Graustufen umgewandelt
- Konturen der Symbole werden erkannt und jedes Symbol wird in eigenem File im Symbol-Ordner (`symbols`) gespeichert
- Symbole werden aus Symbol-Ordner geladen und in Quadrat mittig eingefügt
- Grösse des Quadrats ist vordefiniert auf 100x100 Pixel
- Symbole werden auf Quadratgrösse skaliert und in Quadrat eingefügt
- Neues Bild wird als PNG-Datei im Ordner `squares` gespeichert
- Dateiname besteht aus Präfix und ursprünglichem Dateinamen des Symbols

### Skript `reformat.py`
- Importiert os und Image von der Python Imaging Library (PIL)
- Definiert eine Funktion namens `process_image`, die ein Bild liest, es auf eine Grösse von 10x10 Pixel verkleinert, in ein binäres Schwarz-Weiss-Bild konvertiert, es speichert und die Pixelwerte in eine CSV-Datei schreibt
- Durchläuft jede Datei im Eingabe-Verzeichnis und ruft die `process_image` -Funktion auf, um jedes Bild zu verarbeiten.
- verarbeitete Bilder werden in `processed` gespeichert

## Requirements
Sind unter `requirements.txt` aufgelistet. Diese können mit dem Befehl `pip install -r requirements.txt` installiert werden.