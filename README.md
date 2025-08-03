# Python Directory Compare

Ein einfaches Python-Tool zum Vergleichen von Dateigrößen in Verzeichnissen – z.B. für die Überprüfung von Backups und Synchronisationen.

## Features
- Listet alle Dateien eines Verzeichnisses mit ihrer Größe auf
- Speichert die Ergebnisse in einer Textdatei (relativer Pfad, Größe)
- Vergleicht ein Verzeichnis mit einer gespeicherten Ergebnisdatei
- Zeigt neue, gelöschte und geänderte Dateien an
- Groß-/Kleinschreibung der Dateinamen wird beim Vergleich ignoriert

## Beispielaufrufe

**Scan eines Verzeichnisses und Speichern der Dateigrößen:**

```bash
python compareFolders.py scan /pfad/zum/verzeichnis ergebnis.txt
```
**Vergleich eines Verzeichnisses mit einer Ergebnisdatei:**

```bash
python compareFolders.py compare /pfad/zum/verzeichnis ergebnis.txt
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
- Ist derzeit nur auf Linux getestet

## Lizenz
MIT License
