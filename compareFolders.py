import os
import argparse



def list_files_with_sizes(root_path, output_file):
    entries = []
    root_path = os.path.normpath(os.path.abspath(root_path))
    for dirpath, _, filenames in os.walk(root_path):
        for filename in filenames:
            abs_file_path = os.path.normpath(os.path.abspath(os.path.join(dirpath, filename)))
            rel_file_path = os.path.relpath(abs_file_path, root_path).lower()
            try:
                size = os.path.getsize(abs_file_path)
                entries.append((rel_file_path, size))
            except Exception as e:
                entries.append((rel_file_path, f"ERROR: {e}"))
    entries.sort(key=lambda x: x[0])
    with open(output_file, 'w', encoding='utf-8') as f:
        for entry in entries:
            f.write("\t".join(str(e) for e in entry) + "\n")
    print (f" {len(entries)} Dateien und Verzeichnisse wurden erfasst")

def load_file_info(result_file):
    info = {}
    with open(result_file, 'r', encoding='utf-8') as f:
        for line in f:
            parts = line.strip().split('\t')
            if len(parts) >= 2 and not parts[1].startswith('ERROR'):
                rel_file_path = os.path.normpath(parts[0]).lower()
                size = int(parts[1])
                info[rel_file_path] = {'size': size}
    return info

def compare_with_result(root_path, result_file):
    old_info = load_file_info(result_file)
    new_info = {}
    root_path = os.path.normpath(os.path.abspath(root_path))
    for dirpath, _, filenames in os.walk(root_path):
        for filename in filenames:
            abs_file_path = os.path.normpath(os.path.abspath(os.path.join(dirpath, filename)))
            rel_file_path = os.path.relpath(abs_file_path, root_path).lower()
            try:
                size = os.path.getsize(abs_file_path)
                new_info[rel_file_path] = {'size': size}
            except Exception:
                continue

    all_files = set(old_info.keys()) | set(new_info.keys())
    print (f"{len(all_files)} Dateien und Verzeichnisse werden verglichen")

    # Verzeichnisse ermitteln, die komplett fehlen
    missing_files = [fp for fp in sorted(all_files) if old_info.get(fp) and not new_info.get(fp)]
    missing_dirs = set()
    for fp in missing_files:
        dir_part = os.path.dirname(fp)
        if dir_part:
            missing_dirs.add(dir_part)

    # Prüfe, ob ein ganzes Verzeichnis fehlt (ab 3 Dateien als ganzes Verzeichnis melden)
    already_reported = set()
    reported_dirs = set()
    for dir_part in sorted(missing_dirs):
        # Prüfe, ob dieses Verzeichnis ein Unterverzeichnis eines bereits gemeldeten ist
        if any(dir_part == d or dir_part.startswith(d + os.sep) for d in reported_dirs):
            continue
        files_in_dir = [fp for fp in missing_files if fp.startswith(dir_part + os.sep) or fp == dir_part]
        if len(files_in_dir) > 2:
            print(f"Verzeichnis fehlt in der Sicherung: {dir_part}/")
            already_reported.update(files_in_dir)
            reported_dirs.add(dir_part)

    for file_path in sorted(all_files):
        old = old_info.get(file_path)
        new = new_info.get(file_path)
        # Prüfe, ob file_path in einem bereits gemeldeten fehlenden Verzeichnis liegt
        if old is None:
            print(f"Nur in der Sicherung: {file_path}")
        elif new is None and not any(file_path == d or file_path.startswith(d + os.sep) for d in reported_dirs) and file_path not in already_reported:
            print(f"nicht gefunden in der Sicherung: {file_path}")
        elif new is not None and old['size'] != new['size']:
            print(f"Geändert: {file_path} -> Größe: alt={old['size']} neu={new['size']}")

def main():
    # Beispielaufrufe für die Bedienung:
    #
    # Scan eines Verzeichnisses und Speichern der Dateigrößen:
    #   python compareFolders.py scan /pfad/zum/verzeichnis ergebnis.txt
    #
    # Vergleich eines Verzeichnisses mit einer Ergebnisdatei:
    #   python compareFolders.py compare /pfad/zum/verzeichnis ergebnis.txt
    #
    # Die Ausgabe erfolgt auf der Konsole.
    #
    parser = argparse.ArgumentParser(
        description="""
Dateigrößenanalyse und Vergleich

Beispielaufrufe:
  Scan eines Verzeichnisses und Speichern der Dateigrößen:
    python compareFolders.py scan /pfad/zum/verzeichnis ergebnis.txt

  Vergleich eines Verzeichnisses mit einer Ergebnisdatei:
    python compareFolders.py compare /pfad/zum/verzeichnis ergebnis.txt

Die Ausgabe erfolgt auf der Konsole.
""",
        formatter_class=argparse.RawDescriptionHelpFormatter
    )
    subparsers = parser.add_subparsers(dest='command')

    parser_scan = subparsers.add_parser('scan', help='Dateien und Größen auflisten')
    parser_scan.add_argument('directory', help='Zu scannendes Verzeichnis')
    parser_scan.add_argument('output_file', help='Datei für die Ergebnisse')

    parser_cmp = subparsers.add_parser('compare', help='Vergleich mit Ergebnisdatei')
    parser_cmp.add_argument('directory', help='Zu vergleichendes Verzeichnis')
    parser_cmp.add_argument('result_file', help='Vorherige Ergebnisdatei')

    args = parser.parse_args()

    if args.command == 'scan':
            list_files_with_sizes(args.directory, args.output_file)
            print ("Verzeichnis erfasst")
    elif args.command == 'compare':
            compare_with_result(args.directory, args.result_file)
            print ("vergleich abgeschlossen")
    else:
        parser.print_help()

if __name__ == "__main__":
    main()
