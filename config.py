from datetime import date
from build import get_version

# App-Metadaten
TITLE = "Prüfungs- und Korrektorenverteilung"
APP_NAME = "PVIHK"
AUTHOR = "fz@zenmeister.de"
COPYRIGHT = "© 2025 " + AUTHOR

# Version (inkl. optionaler Inkrementierung)
VERSION = get_version(increment=True)
DATE = str(date.today())

# Titeltexte
TITLEVERSION = f"{TITLE} (V{VERSION})"
WINDOWTITLE = f"{APP_NAME}: Prüfungs- und Korrektorenverteilung, {VERSION}, {DATE}"
