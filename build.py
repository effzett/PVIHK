def get_and_increment_build():
    import sys
    import os

    if getattr(sys, 'frozen', False):
        # Gebündelte App (z. B. EXE via PyInstaller)
        BASIS_DIR = sys._MEIPASS  # Ressourcenverzeichnis
        frozen = True
    else:
        # Entwicklungsmodus
        BASIS_DIR = os.path.dirname(os.path.abspath(__file__))
        frozen = False

    filename = os.path.join(BASIS_DIR, "build_number.txt")

    try:
        with open(filename, "r") as f:
            build = int(f.read().strip())
    except (FileNotFoundError, ValueError):
        build = 0

    # Nur im Entwicklungsmodus inkrementieren
    if not frozen:
        build += 1
        with open(filename, "w") as f:
            f.write(str(build))

    return build
