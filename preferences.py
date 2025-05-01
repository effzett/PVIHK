# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'preferences.ui'
##
## Created by: Qt User Interface Compiler version 6.7.3
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide6.QtCore import (QCoreApplication, QDate, QDateTime, QLocale,
    QMetaObject, QObject, QPoint, QRect,
    QSize, QTime, QUrl, Qt)
from PySide6.QtGui import (QBrush, QColor, QConicalGradient, QCursor,
    QFont, QFontDatabase, QGradient, QIcon,
    QImage, QKeySequence, QLinearGradient, QPainter,
    QPalette, QPixmap, QRadialGradient, QTransform)
from PySide6.QtWidgets import (QAbstractButton, QApplication, QCheckBox, QDialog,
    QDialogButtonBox, QFormLayout, QGridLayout, QGroupBox,
    QHeaderView, QLabel, QLineEdit, QSizePolicy,
    QSpacerItem, QSpinBox, QTableWidget, QTableWidgetItem,
    QTimeEdit, QVBoxLayout, QWidget)

class Ui_Preferences(object):
    def setupUi(self, Preferences):
        if not Preferences.objectName():
            Preferences.setObjectName(u"Preferences")
        Preferences.resize(687, 481)
        self.verticalLayout = QVBoxLayout(Preferences)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.groupBox_2 = QGroupBox(Preferences)
        self.groupBox_2.setObjectName(u"groupBox_2")
        sizePolicy = QSizePolicy(QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.groupBox_2.sizePolicy().hasHeightForWidth())
        self.groupBox_2.setSizePolicy(sizePolicy)
        self.groupBox_2.setMinimumSize(QSize(0, 120))
        self.groupBox_2.setMaximumSize(QSize(16777215, 120))
        self.verticalLayout_3 = QVBoxLayout(self.groupBox_2)
        self.verticalLayout_3.setObjectName(u"verticalLayout_3")
        self.gridLayout = QGridLayout()
        self.gridLayout.setObjectName(u"gridLayout")
        self.gridLayout.setHorizontalSpacing(22)
        self.checkBox = QCheckBox(self.groupBox_2)
        self.checkBox.setObjectName(u"checkBox")
        self.checkBox.setEnabled(False)

        self.gridLayout.addWidget(self.checkBox, 0, 0, 1, 1)

        self.formLayout_5 = QFormLayout()
        self.formLayout_5.setObjectName(u"formLayout_5")
        self.label_8 = QLabel(self.groupBox_2)
        self.label_8.setObjectName(u"label_8")
        self.label_8.setEnabled(False)

        self.formLayout_5.setWidget(0, QFormLayout.LabelRole, self.label_8)

        self.spinBox = QSpinBox(self.groupBox_2)
        self.spinBox.setObjectName(u"spinBox")
        self.spinBox.setEnabled(False)
        self.spinBox.setValue(16)

        self.formLayout_5.setWidget(0, QFormLayout.FieldRole, self.spinBox)


        self.gridLayout.addLayout(self.formLayout_5, 0, 1, 1, 1)

        self.formLayout_7 = QFormLayout()
        self.formLayout_7.setObjectName(u"formLayout_7")
        self.label_10 = QLabel(self.groupBox_2)
        self.label_10.setObjectName(u"label_10")
        self.label_10.setEnabled(False)

        self.formLayout_7.setWidget(0, QFormLayout.LabelRole, self.label_10)

        self.lineEdit = QLineEdit(self.groupBox_2)
        self.lineEdit.setObjectName(u"lineEdit")
        self.lineEdit.setEnabled(False)

        self.formLayout_7.setWidget(0, QFormLayout.FieldRole, self.lineEdit)


        self.gridLayout.addLayout(self.formLayout_7, 0, 2, 1, 1)

        self.checkBox_2 = QCheckBox(self.groupBox_2)
        self.checkBox_2.setObjectName(u"checkBox_2")
        self.checkBox_2.setEnabled(False)

        self.gridLayout.addWidget(self.checkBox_2, 1, 0, 1, 1)

        self.formLayout_6 = QFormLayout()
        self.formLayout_6.setObjectName(u"formLayout_6")
        self.label_9 = QLabel(self.groupBox_2)
        self.label_9.setObjectName(u"label_9")
        self.label_9.setEnabled(False)

        self.formLayout_6.setWidget(0, QFormLayout.LabelRole, self.label_9)

        self.spinBox_2 = QSpinBox(self.groupBox_2)
        self.spinBox_2.setObjectName(u"spinBox_2")
        self.spinBox_2.setEnabled(False)
        self.spinBox_2.setValue(6)

        self.formLayout_6.setWidget(0, QFormLayout.FieldRole, self.spinBox_2)


        self.gridLayout.addLayout(self.formLayout_6, 1, 1, 1, 1)

        self.formLayout_8 = QFormLayout()
        self.formLayout_8.setObjectName(u"formLayout_8")
        self.label_11 = QLabel(self.groupBox_2)
        self.label_11.setObjectName(u"label_11")
        self.label_11.setEnabled(False)

        self.formLayout_8.setWidget(0, QFormLayout.LabelRole, self.label_11)

        self.lineEdit_2 = QLineEdit(self.groupBox_2)
        self.lineEdit_2.setObjectName(u"lineEdit_2")
        self.lineEdit_2.setEnabled(False)

        self.formLayout_8.setWidget(0, QFormLayout.FieldRole, self.lineEdit_2)


        self.gridLayout.addLayout(self.formLayout_8, 1, 2, 1, 1)


        self.verticalLayout_3.addLayout(self.gridLayout)


        self.verticalLayout.addWidget(self.groupBox_2)

        self.groupBox = QGroupBox(Preferences)
        self.groupBox.setObjectName(u"groupBox")
        self.verticalLayout_2 = QVBoxLayout(self.groupBox)
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.gridLayout_3 = QGridLayout()
        self.gridLayout_3.setObjectName(u"gridLayout_3")
        self.label_3 = QLabel(self.groupBox)
        self.label_3.setObjectName(u"label_3")
        self.label_3.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)

        self.gridLayout_3.addWidget(self.label_3, 0, 0, 1, 1)

        self.formLayout_3 = QFormLayout()
        self.formLayout_3.setObjectName(u"formLayout_3")
        self.formLayout_3.setFormAlignment(Qt.AlignCenter)
        self.label_6 = QLabel(self.groupBox)
        self.label_6.setObjectName(u"label_6")

        self.formLayout_3.setWidget(0, QFormLayout.LabelRole, self.label_6)

        self.spinBoxDuration2 = QSpinBox(self.groupBox)
        self.spinBoxDuration2.setObjectName(u"spinBoxDuration2")
        self.spinBoxDuration2.setMinimum(10)
        self.spinBoxDuration2.setMaximum(180)
        self.spinBoxDuration2.setSingleStep(5)
        self.spinBoxDuration2.setValue(60)

        self.formLayout_3.setWidget(0, QFormLayout.FieldRole, self.spinBoxDuration2)


        self.gridLayout_3.addLayout(self.formLayout_3, 1, 2, 1, 1)

        self.label_4 = QLabel(self.groupBox)
        self.label_4.setObjectName(u"label_4")
        self.label_4.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)

        self.gridLayout_3.addWidget(self.label_4, 1, 0, 1, 1)

        self.formLayout_4 = QFormLayout()
        self.formLayout_4.setObjectName(u"formLayout_4")
        self.formLayout_4.setFormAlignment(Qt.AlignCenter)
        self.label_2 = QLabel(self.groupBox)
        self.label_2.setObjectName(u"label_2")

        self.formLayout_4.setWidget(0, QFormLayout.LabelRole, self.label_2)

        self.timeEditBegin2 = QTimeEdit(self.groupBox)
        self.timeEditBegin2.setObjectName(u"timeEditBegin2")
        self.timeEditBegin2.setTime(QTime(14, 0, 0))

        self.formLayout_4.setWidget(0, QFormLayout.FieldRole, self.timeEditBegin2)


        self.gridLayout_3.addLayout(self.formLayout_4, 1, 1, 1, 1)

        self.formLayout = QFormLayout()
        self.formLayout.setObjectName(u"formLayout")
        self.formLayout.setFormAlignment(Qt.AlignCenter)
        self.formLayout.setVerticalSpacing(-1)
        self.label = QLabel(self.groupBox)
        self.label.setObjectName(u"label")

        self.formLayout.setWidget(0, QFormLayout.LabelRole, self.label)

        self.timeEditBegin1 = QTimeEdit(self.groupBox)
        self.timeEditBegin1.setObjectName(u"timeEditBegin1")
        self.timeEditBegin1.setProperty(u"showGroupSeparator", False)
        self.timeEditBegin1.setDateTime(QDateTime(QDate(1999, 12, 31), QTime(9, 0, 0)))
        self.timeEditBegin1.setTime(QTime(9, 0, 0))

        self.formLayout.setWidget(0, QFormLayout.FieldRole, self.timeEditBegin1)


        self.gridLayout_3.addLayout(self.formLayout, 0, 1, 1, 1)

        self.formLayout_2 = QFormLayout()
        self.formLayout_2.setObjectName(u"formLayout_2")
        self.formLayout_2.setFormAlignment(Qt.AlignCenter)
        self.label_5 = QLabel(self.groupBox)
        self.label_5.setObjectName(u"label_5")

        self.formLayout_2.setWidget(0, QFormLayout.LabelRole, self.label_5)

        self.spinBoxDuration1 = QSpinBox(self.groupBox)
        self.spinBoxDuration1.setObjectName(u"spinBoxDuration1")
        self.spinBoxDuration1.setMinimum(10)
        self.spinBoxDuration1.setMaximum(180)
        self.spinBoxDuration1.setSingleStep(5)
        self.spinBoxDuration1.setValue(60)

        self.formLayout_2.setWidget(0, QFormLayout.FieldRole, self.spinBoxDuration1)


        self.gridLayout_3.addLayout(self.formLayout_2, 0, 2, 1, 1)

        self.labelLunch = QLabel(self.groupBox)
        self.labelLunch.setObjectName(u"labelLunch")
        self.labelLunch.setMinimumSize(QSize(0, 40))
        self.labelLunch.setMaximumSize(QSize(16777215, 50))
        self.labelLunch.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)

        self.gridLayout_3.addWidget(self.labelLunch, 2, 0, 1, 1)


        self.verticalLayout_2.addLayout(self.gridLayout_3)

        self.verticalSpacer = QSpacerItem(20, 40, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Expanding)

        self.verticalLayout_2.addItem(self.verticalSpacer)

        self.tableWidgetTimes = QTableWidget(self.groupBox)
        if (self.tableWidgetTimes.columnCount() < 12):
            self.tableWidgetTimes.setColumnCount(12)
        if (self.tableWidgetTimes.rowCount() < 2):
            self.tableWidgetTimes.setRowCount(2)
        __qtablewidgetitem = QTableWidgetItem()
        self.tableWidgetTimes.setVerticalHeaderItem(0, __qtablewidgetitem)
        __qtablewidgetitem1 = QTableWidgetItem()
        self.tableWidgetTimes.setVerticalHeaderItem(1, __qtablewidgetitem1)
        self.tableWidgetTimes.setObjectName(u"tableWidgetTimes")
        self.tableWidgetTimes.setMaximumSize(QSize(16777215, 90))

        self.verticalLayout_2.addWidget(self.tableWidgetTimes)


        self.verticalLayout.addWidget(self.groupBox)

        self.buttonBox = QDialogButtonBox(Preferences)
        self.buttonBox.setObjectName(u"buttonBox")
        self.buttonBox.setOrientation(Qt.Horizontal)
        self.buttonBox.setStandardButtons(QDialogButtonBox.Cancel|QDialogButtonBox.Ok)

        self.verticalLayout.addWidget(self.buttonBox, 0, Qt.AlignHCenter)


        self.retranslateUi(Preferences)
        self.buttonBox.accepted.connect(Preferences.accept)
        self.buttonBox.rejected.connect(Preferences.reject)

        QMetaObject.connectSlotsByName(Preferences)
    # setupUi

    def retranslateUi(self, Preferences):
        Preferences.setWindowTitle(QCoreApplication.translate("Preferences", u"Einstellungen", None))
        self.groupBox_2.setTitle(QCoreApplication.translate("Preferences", u"Konfiguration der Pr\u00fcflinge und Korrektoren", None))
        self.checkBox.setText(QCoreApplication.translate("Preferences", u"Anonyme Pr\u00fcflinge", None))
        self.label_8.setText(QCoreApplication.translate("Preferences", u"Anzahl", None))
        self.label_10.setText(QCoreApplication.translate("Preferences", u"Muster", None))
        self.lineEdit.setText(QCoreApplication.translate("Preferences", u"Pr\u00fcfling #", None))
        self.checkBox_2.setText(QCoreApplication.translate("Preferences", u"Anonyme Korrektoren", None))
        self.label_9.setText(QCoreApplication.translate("Preferences", u"Anzahl", None))
        self.label_11.setText(QCoreApplication.translate("Preferences", u"Muster", None))
        self.lineEdit_2.setText(QCoreApplication.translate("Preferences", u"Korrektor #", None))
        self.groupBox.setTitle(QCoreApplication.translate("Preferences", u"Einstellung der Pr\u00fcfungszeiten (gilt f\u00fcr beide Tage gleicherma\u00dfen)", None))
        self.label_3.setText(QCoreApplication.translate("Preferences", u"Vormittags", None))
        self.label_6.setText(QCoreApplication.translate("Preferences", u"Pr\u00fcfungsdauer", None))
        self.spinBoxDuration2.setSuffix(QCoreApplication.translate("Preferences", u" Minuten", None))
        self.label_4.setText(QCoreApplication.translate("Preferences", u"Nachmittags", None))
        self.label_2.setText(QCoreApplication.translate("Preferences", u"2. Beginn", None))
        self.label.setText(QCoreApplication.translate("Preferences", u"1. Beginn", None))
        self.label_5.setText(QCoreApplication.translate("Preferences", u"Pr\u00fcfungsdauer", None))
        self.spinBoxDuration1.setSuffix(QCoreApplication.translate("Preferences", u" Minuten", None))
        self.labelLunch.setText(QCoreApplication.translate("Preferences", u"Mittagspause:", None))
        ___qtablewidgetitem = self.tableWidgetTimes.verticalHeaderItem(0)
        ___qtablewidgetitem.setText(QCoreApplication.translate("Preferences", u"Tag 1", None));
        ___qtablewidgetitem1 = self.tableWidgetTimes.verticalHeaderItem(1)
        ___qtablewidgetitem1.setText(QCoreApplication.translate("Preferences", u"Tag 2", None));
    # retranslateUi

