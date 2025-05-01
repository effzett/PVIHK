from PySide6.QtWidgets import QDialog, QHeaderView, QTableWidgetItem
from PySide6.QtCore import Qt, QTime
from datetime import datetime, timedelta
import json
from pathlib import Path
from preferences import Ui_Preferences

from contextlib import contextmanager

@contextmanager
def block_signals(widgets):
    for w in widgets:
        w.blockSignals(True)
    try:
        yield
    finally:
        for w in widgets:
            w.blockSignals(False)

class PreferencesDialog(QDialog, Ui_Preferences):
    def __init__(self, parent=None, preferences_path=None):
        super().__init__(parent)
        self.setupUi(self)

        self.preferences_file = preferences_path or Path.home() / ".pvihk_preferences.json"

        # Events
        self.timeEditBegin1.timeChanged.connect(self.update_zeittabelle)
        self.timeEditBegin2.timeChanged.connect(self.update_zeittabelle)
        self.spinBoxDuration1.valueChanged.connect(self.update_zeittabelle)
        self.spinBoxDuration2.valueChanged.connect(self.update_zeittabelle)

        # Initial laden
        self.load_preferences()

    def load_preferences(self):
        if not self.preferences_file.exists():
            # Defaults setzen – alles konsistent
            with block_signals([
                self.timeEditBegin1,
                self.timeEditBegin2,
                self.spinBoxDuration1,
                self.spinBoxDuration2
            ]):
                self.timeEditBegin1.setTime(QTime(9, 0))
                self.timeEditBegin2.setTime(QTime(14, 0))
                self.spinBoxDuration1.setValue(60)
                self.spinBoxDuration2.setValue(60)

            default_slots = [
                ["09:00", "10:00", "11:00", "12:00"],
                ["14:00", "15:00", "16:00", "17:00"]
            ]
            self.set_zeitslots(default_slots)
            self.geladene_zeitslots = default_slots
            return

        try:
            with open(self.preferences_file, "r", encoding="utf-8") as f:
                data = json.load(f)

            with block_signals([
                self.timeEditBegin1,
                self.timeEditBegin2,
                self.spinBoxDuration1,
                self.spinBoxDuration2
            ]):
                if "begin1" in data:
                    h, m = map(int, data["begin1"].split(":"))
                    self.timeEditBegin1.setTime(QTime(h, m))

                if "begin2" in data:
                    h, m = map(int, data["begin2"].split(":"))
                    self.timeEditBegin2.setTime(QTime(h, m))

                if "dauer1" in data:
                    self.spinBoxDuration1.setValue(int(data["dauer1"]))

                if "dauer2" in data:
                    self.spinBoxDuration2.setValue(int(data["dauer2"]))

            if "zeitslots" in data:
                self.set_zeitslots(data["zeitslots"])
                self.geladene_zeitslots = data["zeitslots"]

        except Exception as e:
            print(f"Fehler beim Laden der Einstellungen: {e}")

    def save_preferences(self):
        daten = {
            "begin1": self.timeEditBegin1.time().toString("HH:mm"),
            "begin2": self.timeEditBegin2.time().toString("HH:mm"),
            "dauer1": self.spinBoxDuration1.value(),
            "dauer2": self.spinBoxDuration2.value(),
            "zeitslots": self.get_pruefungszeiten()
        }
        try:
            with open(self.preferences_file, "w", encoding="utf-8") as f:
                json.dump(daten, f, indent=2)
            print("Einstellungen gespeichert in", self.preferences_file)
        except Exception as e:
            print(f"Fehler beim Speichern der Einstellungen: {e}")

    def update_zeittabelle(self):
        try:
            fmt = "%H:%M"
            dauer1 = self.spinBoxDuration1.value()
            dauer2 = self.spinBoxDuration2.value()

            start1_dt = datetime.combine(datetime.today(), self.timeEditBegin1.time().toPython())
            start2_dt = datetime.combine(datetime.today(), self.timeEditBegin2.time().toPython())

            min_pause = timedelta(minutes=15)
            max_end_time = datetime.combine(datetime.today(), datetime.strptime("18:00", fmt).time())

            # Slot-Berechnung
            zeiten = []

            aktuelle = start1_dt
            while aktuelle + timedelta(minutes=dauer1) <= start2_dt - min_pause:
                zeiten.append(aktuelle.strftime(fmt))
                aktuelle += timedelta(minutes=dauer1)

            pause_start = aktuelle
            pause_dauer = start2_dt - pause_start
            pause_min = int(pause_dauer.total_seconds() // 60)
            if pause_min >= 60:
                pause_str = f"Mittagspause: {pause_min // 60}:{pause_min % 60:02d} Stunden"
            else:
                pause_str = f"Mittagspause: {pause_min} Minuten"
            self.labelLunch.setText(pause_str)

            aktuelle = start2_dt
            while aktuelle + timedelta(minutes=dauer2) <= max_end_time:
                zeiten.append(aktuelle.strftime(fmt))
                aktuelle += timedelta(minutes=dauer2)

            # Tabelle füllen
            self.tableWidgetTimes.clearContents()
            self.tableWidgetTimes.setRowCount(2)
            self.tableWidgetTimes.setColumnCount(len(zeiten))
            self.tableWidgetTimes.setHorizontalHeaderLabels([f"P{i+1}" for i in range(len(zeiten))])
            self.tableWidgetTimes.setVerticalHeaderLabels(["Tag 1", "Tag 2"])

            for row in range(2):
                for col, zeit in enumerate(zeiten):
                    item = QTableWidgetItem(zeit)
                    item.setFlags(item.flags() | Qt.ItemIsEditable)
                    self.tableWidgetTimes.setItem(row, col, item)

            # Spalten strecken
            header = self.tableWidgetTimes.horizontalHeader()
            for i in range(self.tableWidgetTimes.columnCount()):
                header.setSectionResizeMode(i, QHeaderView.Stretch)

        except Exception as e:
            print(f"Fehler beim Aktualisieren der Zeittabelle: {e}")

    def set_zeitslots(self, slots: list[list[str]]):
        if not (isinstance(slots, list) and len(slots) == 2):
            print("⚠️ Ungültige Zeitslots-Struktur – erwartet 2 Listen")
            return

        max_spalten = max(len(slots[0]), len(slots[1]))
        self.tableWidgetTimes.clearContents()
        self.tableWidgetTimes.setRowCount(2)
        self.tableWidgetTimes.setColumnCount(max_spalten)
        self.tableWidgetTimes.setHorizontalHeaderLabels([f"P{i+1}" for i in range(max_spalten)])
        self.tableWidgetTimes.setVerticalHeaderLabels(["Tag 1", "Tag 2"])

        for row in range(2):
            for col, zeit in enumerate(slots[row]):
                item = QTableWidgetItem(zeit)
                item.setFlags(item.flags() | Qt.ItemIsEditable)
                self.tableWidgetTimes.setItem(row, col, item)

        header = self.tableWidgetTimes.horizontalHeader()
        for i in range(self.tableWidgetTimes.columnCount()):
            header.setSectionResizeMode(i, QHeaderView.Stretch)

    def get_pruefungszeiten(self):
        zeiten = [[], []]
        for row in range(2):
            for col in range(self.tableWidgetTimes.columnCount()):
                item = self.tableWidgetTimes.item(row, col)
                zeiten[row].append(item.text() if item else "")
        return zeiten
