from datetime import date
from build import get_and_increment_build

TITLE = "Prüfungs- und Korrektorenverteilung"
APP_NAME = "PVIHK"
AUTHOR = "fz@zenmeister.de"
COPYRIGHT = "© 2025 " + AUTHOR

BUILD = get_and_increment_build()
VERSION = f"2.0.{BUILD}"
DATE = str(date.today())

TITLEVERSION = TITLE + " (V" + VERSION + ")"
WINDOWTITLE = f"{APP_NAME}: Prüfungs- und Korrektorenverteilung, {VERSION}, {DATE}"
