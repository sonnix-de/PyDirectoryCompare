# Python Directory Compare

Ein einfaches Python-Tool zum Vergleichen von Dateigrößen in Verzeichnissen – ideal zur Überprüfung von Backups, Synchronisationen oder Sicherungen.

## Features
- Listet alle Dateien eines Verzeichnisses mit ihrer Größe auf
- Speichert die Ergebnisse in einer Textdatei (relativer Pfad, Größe)
- Vergleicht ein Verzeichnis mit einer gespeicherten Ergebnisdatei
- Zeigt neue, gelöschte und geänderte Dateien an
- Plattformunabhängig (Linux/Windows)
- Groß-/Kleinschreibung der Dateinamen wird beim Vergleich ignoriert

## Beispielaufrufe

**Scan eines Verzeichnisses und Speichern der Dateigrößen:**

```bash
python filesizeanalyse.py scan /pfad/zum/verzeichnis ergebnis.txt
```

**Vergleich eines Verzeichnisses mit einer Ergebnisdatei:**

```bash
python filesizeanalyse.py compare /pfad/zum/verzeichnis ergebnis.txt
```

Die Ausgabe erfolgt auf der Konsole.

## Typische Anwendungsfälle
- Kontrolle, ob ein Backup/Sicherung vollständig und korrekt ist
- Vergleiche nach Synchronisationen (z.B. mit rsync, robocopy, etc.)
- Erkennen von versehentlich gelöschten oder veränderten Dateien

## Voraussetzungen
- Python 3.x
- Keine externen Abhängigkeiten

## Hinweise
- Die Ergebnisdatei enthält nur relative Pfade und Dateigrößen, keine Zeitstempel oder Metadaten.
- Für Windows und Linux geeignet.
- Die Vergleichsfunktion ist robust gegenüber unterschiedlichen Mountpunkten und Groß-/Kleinschreibung.

## Lizenz
MIT License
