from PySide6.QtCore import QTimer
from PySide6.QtGui import Qt
from PySide6.QtWidgets import QListWidget, QListWidgetItem, QMessageBox


class CustomListWidget(QListWidget):
    def __init__(self, parent=None, max_items=30):
        super().__init__(parent)
        self.max_items = max_items
        self._limit_warning_shown = False

        self.return_pressed = False
        self.itemDelegate().commitData.connect(self.handle_commit)

    def addItem(self, item):
        if self.count() >= self.max_items:
            self._warn_limit()
            return
        super().addItem(item if isinstance(item, QListWidgetItem) else str(item))

    def addItems(self, items):
        space_left = self.max_items - self.count()
        if space_left <= 0:
            self._warn_limit()
            return
        super().addItems(items[:space_left])
        if len(items) > space_left:
            self._warn_limit()

    def insertItem(self, row, item):
        if self.count() >= self.max_items:
            self._warn_limit()
            return
        super().insertItem(row, item if isinstance(item, QListWidgetItem) else str(item))

    def _warn_limit(self):
        if not self._limit_warning_shown:
            self._limit_warning_shown = True
            QTimer.singleShot(0, self._show_limit_warning)

    def _show_limit_warning(self):
        QMessageBox.warning(self, "Listenlimit erreicht",
                            f"Es dürfen maximal {self.max_items} Einträge hinzugefügt werden.")

    def mouseDoubleClickEvent(self, event):
        item = self.itemAt(event.position().toPoint())

        if item:
            self.editItem(item)
        else:
            self.fuege_und_editiere_neues_item_ein()
        event.accept() # keine weiteren Aktionen

    def keyPressEvent(self, event):
        if event.key() in (Qt.Key_Return, Qt.Key_Enter):
            self.return_pressed = True
        else:
            super().keyPressEvent(event)

    def handle_commit(self, editor):
        if not self.return_pressed:
            return
        self.return_pressed = False

        current = self.currentItem()
        if current:
            text = current.text().strip()
            if text == "":
                row = self.row(current)
                self.takeItem(row)  # löscht das leere Item
                return

            row = self.row(current)
            if row + 1 < self.count():
                self.setCurrentRow(row + 1)
                QTimer.singleShot(0, lambda: self.editItem(self.item(row + 1)))
            else:
                self.fuege_und_editiere_neues_item_ein()

    def fuege_und_editiere_neues_item_ein(self):
        neues_item = QListWidgetItem("")
        neues_item.setFlags(neues_item.flags() | Qt.ItemIsEditable)
        self.addItem(neues_item)
        self.setCurrentItem(neues_item)
        QTimer.singleShot(0, lambda: self.editItem(neues_item))

