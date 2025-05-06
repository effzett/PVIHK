from PySide6.QtWidgets import QWidget, QHBoxLayout, QCheckBox, QLineEdit


class KorrektorItem(QWidget):
    def __init__(self, name="", checked=False, parent=None):
        super().__init__(parent)
        self.checkbox = QCheckBox()
        self.lineedit = QLineEdit()
        self.lineedit.setText(name)

        self.checkbox.setChecked(checked)

        layout = QHBoxLayout(self)
        layout.setContentsMargins(2, 0, 2, 0)
        layout.setSpacing(12)
        layout.addWidget(self.checkbox)
        layout.addWidget(self.lineedit)

    def get_name(self):
        return self.lineedit.text().strip()

    def is_checked(self):
        return self.checkbox.isChecked()

    def set_name(self, name):
        self.lineedit.setText(name)

    def set_checked(self, checked):
        self.checkbox.setChecked(checked)
