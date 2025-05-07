from version import __version_major_minor__
import os
import sys

def resource_path(relative_path):
    """Ermittle Pfad relativ zur Datei selbst (auch PyInstaller-kompatibel)."""
    try:
        base_path = sys._MEIPASS
    except AttributeError:
        base_path = os.path.dirname(os.path.abspath(__file__))
    return os.path.join(base_path, relative_path)

BUILD_FILE = resource_path("build_number.txt")

def read_build():
    if not os.path.exists(BUILD_FILE):
        return "0"
    with open(BUILD_FILE, "r") as f:
        return f.read().strip()

def get_and_increment_build():
    build = int(read_build())
    new_build = build + 1
    with open(BUILD_FILE, "w") as f:
        f.write(str(new_build))
    return str(new_build)

def get_version(increment=False):
    build = get_and_increment_build() if increment else read_build()
    return f"{__version_major_minor__}.{build}"
