# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'mainwindow.ui'
##
## Created by: Qt User Interface Compiler version 6.7.3
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide6.QtCore import (QCoreApplication, QDate, QDateTime, QLocale,
    QMetaObject, QObject, QPoint, QRect,
    QSize, QTime, QUrl, Qt)
from PySide6.QtGui import (QAction, QBrush, QColor, QConicalGradient,
    QCursor, QFont, QFontDatabase, QGradient,
    QIcon, QImage, QKeySequence, QLinearGradient,
    QPainter, QPalette, QPixmap, QRadialGradient,
    QTransform)
from PySide6.QtWidgets import (QApplication, QDateEdit, QFrame, QHBoxLayout,
    QHeaderView, QLabel, QListWidget, QListWidgetItem,
    QMainWindow, QMenu, QMenuBar, QPushButton,
    QSizePolicy, QSpacerItem, QStatusBar, QTableWidget,
    QTableWidgetItem, QVBoxLayout, QWidget)

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(892, 676)
        MainWindow.setMinimumSize(QSize(500, 500))
        self.actionKandidaten_einlesen = QAction(MainWindow)
        self.actionKandidaten_einlesen.setObjectName(u"actionKandidaten_einlesen")
        self.actionKorrektoren_einlesen = QAction(MainWindow)
        self.actionKorrektoren_einlesen.setObjectName(u"actionKorrektoren_einlesen")
        self.actionKandidaten_speichern = QAction(MainWindow)
        self.actionKandidaten_speichern.setObjectName(u"actionKandidaten_speichern")
        self.actionKorrektoren_speichern = QAction(MainWindow)
        self.actionKorrektoren_speichern.setObjectName(u"actionKorrektoren_speichern")
        self.actionPDF_abspeichern = QAction(MainWindow)
        self.actionPDF_abspeichern.setObjectName(u"actionPDF_abspeichern")
        self.actionPDF_anzeigen = QAction(MainWindow)
        self.actionPDF_anzeigen.setObjectName(u"actionPDF_anzeigen")
        self.actionSession_save = QAction(MainWindow)
        self.actionSession_save.setObjectName(u"actionSession_save")
        self.actionSession_read = QAction(MainWindow)
        self.actionSession_read.setObjectName(u"actionSession_read")
        self.actionEinstellungen = QAction(MainWindow)
        self.actionEinstellungen.setObjectName(u"actionEinstellungen")
        self.actionAbout = QAction(MainWindow)
        self.actionAbout.setObjectName(u"actionAbout")
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.verticalLayout_3 = QVBoxLayout(self.centralwidget)
        self.verticalLayout_3.setSpacing(0)
        self.verticalLayout_3.setObjectName(u"verticalLayout_3")
        self.frame_top = QFrame(self.centralwidget)
        self.frame_top.setObjectName(u"frame_top")
        self.frame_top.setFrameShape(QFrame.NoFrame)
        self.frame_top.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_7 = QHBoxLayout(self.frame_top)
        self.horizontalLayout_7.setObjectName(u"horizontalLayout_7")
        self.horizontalLayout_6 = QHBoxLayout()
        self.horizontalLayout_6.setObjectName(u"horizontalLayout_6")
        self.verticalLayout_5 = QVBoxLayout()
        self.verticalLayout_5.setObjectName(u"verticalLayout_5")
        self.label = QLabel(self.frame_top)
        self.label.setObjectName(u"label")
        font = QFont()
        font.setBold(True)
        self.label.setFont(font)
        self.label.setAlignment(Qt.AlignCenter)

        self.verticalLayout_5.addWidget(self.label)

        self.date1Edit = QDateEdit(self.frame_top)
        self.date1Edit.setObjectName(u"date1Edit")
        self.date1Edit.setMinimumSize(QSize(0, 30))
        self.date1Edit.setFont(font)
        self.date1Edit.setAlignment(Qt.AlignCenter)
        self.date1Edit.setCalendarPopup(True)

        self.verticalLayout_5.addWidget(self.date1Edit)

        self.listWidget1 = QListWidget(self.frame_top)
        self.listWidget1.setObjectName(u"listWidget1")
        self.listWidget1.setSortingEnabled(False)

        self.verticalLayout_5.addWidget(self.listWidget1)


        self.horizontalLayout_6.addLayout(self.verticalLayout_5)

        self.verticalLayout_6 = QVBoxLayout()
        self.verticalLayout_6.setObjectName(u"verticalLayout_6")
        self.label_3 = QLabel(self.frame_top)
        self.label_3.setObjectName(u"label_3")
        self.label_3.setFont(font)
        self.label_3.setAlignment(Qt.AlignCenter)

        self.verticalLayout_6.addWidget(self.label_3)

        self.listWidgetList = QListWidget(self.frame_top)
        self.listWidgetList.setObjectName(u"listWidgetList")

        self.verticalLayout_6.addWidget(self.listWidgetList)


        self.horizontalLayout_6.addLayout(self.verticalLayout_6)

        self.verticalLayout_7 = QVBoxLayout()
        self.verticalLayout_7.setObjectName(u"verticalLayout_7")
        self.label_2 = QLabel(self.frame_top)
        self.label_2.setObjectName(u"label_2")
        self.label_2.setFont(font)
        self.label_2.setAlignment(Qt.AlignCenter)

        self.verticalLayout_7.addWidget(self.label_2)

        self.date2Edit = QDateEdit(self.frame_top)
        self.date2Edit.setObjectName(u"date2Edit")
        self.date2Edit.setMinimumSize(QSize(0, 30))
        self.date2Edit.setFont(font)
        self.date2Edit.setAlignment(Qt.AlignCenter)
        self.date2Edit.setCalendarPopup(True)

        self.verticalLayout_7.addWidget(self.date2Edit)

        self.listWidget2 = QListWidget(self.frame_top)
        self.listWidget2.setObjectName(u"listWidget2")
        self.listWidget2.setSortingEnabled(False)

        self.verticalLayout_7.addWidget(self.listWidget2)


        self.horizontalLayout_6.addLayout(self.verticalLayout_7)


        self.horizontalLayout_7.addLayout(self.horizontalLayout_6)


        self.verticalLayout_3.addWidget(self.frame_top)

        self.frame_bottom = QFrame(self.centralwidget)
        self.frame_bottom.setObjectName(u"frame_bottom")
        self.frame_bottom.setFrameShape(QFrame.NoFrame)
        self.frame_bottom.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_8 = QHBoxLayout(self.frame_bottom)
        self.horizontalLayout_8.setObjectName(u"horizontalLayout_8")
        self.verticalLayout_10 = QVBoxLayout()
        self.verticalLayout_10.setObjectName(u"verticalLayout_10")
        self.labelDate1 = QLabel(self.frame_bottom)
        self.labelDate1.setObjectName(u"labelDate1")
        font1 = QFont()
        font1.setPointSize(15)
        font1.setBold(True)
        self.labelDate1.setFont(font1)
        self.labelDate1.setAlignment(Qt.AlignCenter)

        self.verticalLayout_10.addWidget(self.labelDate1)

        self.table1Widget = QTableWidget(self.frame_bottom)
        if (self.table1Widget.columnCount() < 3):
            self.table1Widget.setColumnCount(3)
        __qtablewidgetitem = QTableWidgetItem()
        self.table1Widget.setHorizontalHeaderItem(0, __qtablewidgetitem)
        __qtablewidgetitem1 = QTableWidgetItem()
        self.table1Widget.setHorizontalHeaderItem(1, __qtablewidgetitem1)
        __qtablewidgetitem2 = QTableWidgetItem()
        self.table1Widget.setHorizontalHeaderItem(2, __qtablewidgetitem2)
        if (self.table1Widget.rowCount() < 9):
            self.table1Widget.setRowCount(9)
        __qtablewidgetitem3 = QTableWidgetItem()
        self.table1Widget.setItem(0, 0, __qtablewidgetitem3)
        __qtablewidgetitem4 = QTableWidgetItem()
        self.table1Widget.setItem(0, 1, __qtablewidgetitem4)
        __qtablewidgetitem5 = QTableWidgetItem()
        self.table1Widget.setItem(0, 2, __qtablewidgetitem5)
        __qtablewidgetitem6 = QTableWidgetItem()
        self.table1Widget.setItem(1, 0, __qtablewidgetitem6)
        __qtablewidgetitem7 = QTableWidgetItem()
        self.table1Widget.setItem(1, 1, __qtablewidgetitem7)
        __qtablewidgetitem8 = QTableWidgetItem()
        self.table1Widget.setItem(1, 2, __qtablewidgetitem8)
        self.table1Widget.setObjectName(u"table1Widget")
        self.table1Widget.setEnabled(True)
        self.table1Widget.setShowGrid(False)
        self.table1Widget.setRowCount(9)

        self.verticalLayout_10.addWidget(self.table1Widget)


        self.horizontalLayout_8.addLayout(self.verticalLayout_10)

        self.verticalLayout_9 = QVBoxLayout()
        self.verticalLayout_9.setObjectName(u"verticalLayout_9")
        self.labelDate2 = QLabel(self.frame_bottom)
        self.labelDate2.setObjectName(u"labelDate2")
        self.labelDate2.setFont(font1)
        self.labelDate2.setAlignment(Qt.AlignCenter)

        self.verticalLayout_9.addWidget(self.labelDate2)

        self.table2Widget = QTableWidget(self.frame_bottom)
        if (self.table2Widget.columnCount() < 3):
            self.table2Widget.setColumnCount(3)
        __qtablewidgetitem9 = QTableWidgetItem()
        self.table2Widget.setHorizontalHeaderItem(0, __qtablewidgetitem9)
        __qtablewidgetitem10 = QTableWidgetItem()
        self.table2Widget.setHorizontalHeaderItem(1, __qtablewidgetitem10)
        __qtablewidgetitem11 = QTableWidgetItem()
        self.table2Widget.setHorizontalHeaderItem(2, __qtablewidgetitem11)
        if (self.table2Widget.rowCount() < 9):
            self.table2Widget.setRowCount(9)
        __qtablewidgetitem12 = QTableWidgetItem()
        self.table2Widget.setItem(0, 0, __qtablewidgetitem12)
        __qtablewidgetitem13 = QTableWidgetItem()
        self.table2Widget.setItem(0, 1, __qtablewidgetitem13)
        __qtablewidgetitem14 = QTableWidgetItem()
        self.table2Widget.setItem(0, 2, __qtablewidgetitem14)
        __qtablewidgetitem15 = QTableWidgetItem()
        self.table2Widget.setItem(1, 0, __qtablewidgetitem15)
        __qtablewidgetitem16 = QTableWidgetItem()
        self.table2Widget.setItem(1, 1, __qtablewidgetitem16)
        __qtablewidgetitem17 = QTableWidgetItem()
        self.table2Widget.setItem(1, 2, __qtablewidgetitem17)
        self.table2Widget.setObjectName(u"table2Widget")
        self.table2Widget.setEnabled(True)
        self.table2Widget.setShowGrid(False)

        self.verticalLayout_9.addWidget(self.table2Widget)


        self.horizontalLayout_8.addLayout(self.verticalLayout_9)


        self.verticalLayout_3.addWidget(self.frame_bottom)

        self.frame = QFrame(self.centralwidget)
        self.frame.setObjectName(u"frame")
        self.frame.setMinimumSize(QSize(0, 45))
        self.frame.setMaximumSize(QSize(16777215, 55))
        self.frame.setFrameShape(QFrame.NoFrame)
        self.frame.setFrameShadow(QFrame.Raised)
        self.verticalLayout_2 = QVBoxLayout(self.frame)
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.horizontalLayout_5 = QHBoxLayout()
        self.horizontalLayout_5.setObjectName(u"horizontalLayout_5")
        self.horizontalLayout_4 = QHBoxLayout()
        self.horizontalLayout_4.setObjectName(u"horizontalLayout_4")
        self.pushButtonCancelOptimize = QPushButton(self.frame)
        self.pushButtonCancelOptimize.setObjectName(u"pushButtonCancelOptimize")

        self.horizontalLayout_4.addWidget(self.pushButtonCancelOptimize)

        self.horizontalSpacer = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.horizontalLayout_4.addItem(self.horizontalSpacer)

        self.pushButtonCancel = QPushButton(self.frame)
        self.pushButtonCancel.setObjectName(u"pushButtonCancel")
        sizePolicy = QSizePolicy(QSizePolicy.Policy.Fixed, QSizePolicy.Policy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.pushButtonCancel.sizePolicy().hasHeightForWidth())
        self.pushButtonCancel.setSizePolicy(sizePolicy)
        self.pushButtonCancel.setMinimumSize(QSize(0, 29))

        self.horizontalLayout_4.addWidget(self.pushButtonCancel)

        self.pushButtonOptimize = QPushButton(self.frame)
        self.pushButtonOptimize.setObjectName(u"pushButtonOptimize")
        sizePolicy.setHeightForWidth(self.pushButtonOptimize.sizePolicy().hasHeightForWidth())
        self.pushButtonOptimize.setSizePolicy(sizePolicy)
        self.pushButtonOptimize.setMinimumSize(QSize(0, 29))
        self.pushButtonOptimize.setAutoDefault(True)

        self.horizontalLayout_4.addWidget(self.pushButtonOptimize)

        self.horizontalSpacer_2 = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.horizontalLayout_4.addItem(self.horizontalSpacer_2)


        self.horizontalLayout_5.addLayout(self.horizontalLayout_4)


        self.verticalLayout_2.addLayout(self.horizontalLayout_5)


        self.verticalLayout_3.addWidget(self.frame)

        MainWindow.setCentralWidget(self.centralwidget)
        self.statusbar = QStatusBar(MainWindow)
        self.statusbar.setObjectName(u"statusbar")
        MainWindow.setStatusBar(self.statusbar)
        self.menuBar = QMenuBar(MainWindow)
        self.menuBar.setObjectName(u"menuBar")
        self.menuBar.setGeometry(QRect(0, 0, 892, 24))
        self.menuDatei = QMenu(self.menuBar)
        self.menuDatei.setObjectName(u"menuDatei")
        self.menuPr_flinge = QMenu(self.menuDatei)
        self.menuPr_flinge.setObjectName(u"menuPr_flinge")
        self.menuKorrektoren = QMenu(self.menuDatei)
        self.menuKorrektoren.setObjectName(u"menuKorrektoren")
        self.menuSession = QMenu(self.menuDatei)
        self.menuSession.setObjectName(u"menuSession")
        self.menuAnsicht = QMenu(self.menuBar)
        self.menuAnsicht.setObjectName(u"menuAnsicht")
        self.menuInfo = QMenu(self.menuBar)
        self.menuInfo.setObjectName(u"menuInfo")
        MainWindow.setMenuBar(self.menuBar)
        QWidget.setTabOrder(self.date1Edit, self.date2Edit)
        QWidget.setTabOrder(self.date2Edit, self.listWidget1)
        QWidget.setTabOrder(self.listWidget1, self.listWidget2)
        QWidget.setTabOrder(self.listWidget2, self.listWidgetList)
        QWidget.setTabOrder(self.listWidgetList, self.pushButtonCancel)
        QWidget.setTabOrder(self.pushButtonCancel, self.pushButtonOptimize)
        QWidget.setTabOrder(self.pushButtonOptimize, self.table1Widget)
        QWidget.setTabOrder(self.table1Widget, self.table2Widget)
        QWidget.setTabOrder(self.table2Widget, self.pushButtonCancelOptimize)

        self.menuBar.addAction(self.menuDatei.menuAction())
        self.menuBar.addAction(self.menuAnsicht.menuAction())
        self.menuBar.addAction(self.menuInfo.menuAction())
        self.menuDatei.addAction(self.menuPr_flinge.menuAction())
        self.menuDatei.addSeparator()
        self.menuDatei.addAction(self.menuKorrektoren.menuAction())
        self.menuDatei.addSeparator()
        self.menuDatei.addAction(self.menuSession.menuAction())
        self.menuDatei.addSeparator()
        self.menuDatei.addAction(self.actionEinstellungen)
        self.menuPr_flinge.addAction(self.actionKandidaten_einlesen)
        self.menuPr_flinge.addAction(self.actionKandidaten_speichern)
        self.menuKorrektoren.addAction(self.actionKorrektoren_einlesen)
        self.menuKorrektoren.addAction(self.actionKorrektoren_speichern)
        self.menuSession.addAction(self.actionSession_save)
        self.menuSession.addAction(self.actionSession_read)
        self.menuAnsicht.addAction(self.actionPDF_anzeigen)
        self.menuAnsicht.addAction(self.actionPDF_abspeichern)
        self.menuInfo.addAction(self.actionAbout)

        self.retranslateUi(MainWindow)

        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"Pr\u00fcfungsaufteilung (IHK) (fz,V1.0.0)", None))
        self.actionKandidaten_einlesen.setText(QCoreApplication.translate("MainWindow", u"Pr\u00fcflinge einlesen...", None))
        self.actionKorrektoren_einlesen.setText(QCoreApplication.translate("MainWindow", u"Korrektoren einlesen...", None))
        self.actionKandidaten_speichern.setText(QCoreApplication.translate("MainWindow", u"Pr\u00fcflinge speichern...", None))
        self.actionKorrektoren_speichern.setText(QCoreApplication.translate("MainWindow", u"Korrektoren speichern...", None))
        self.actionPDF_abspeichern.setText(QCoreApplication.translate("MainWindow", u"PDF abspeichern...", None))
        self.actionPDF_anzeigen.setText(QCoreApplication.translate("MainWindow", u"PDF anzeigen", None))
        self.actionSession_save.setText(QCoreApplication.translate("MainWindow", u"Session speichern", None))
        self.actionSession_read.setText(QCoreApplication.translate("MainWindow", u"Session einlesen", None))
        self.actionEinstellungen.setText(QCoreApplication.translate("MainWindow", u"Einstellungen", None))
        self.actionAbout.setText(QCoreApplication.translate("MainWindow", u"\u00dcber PVIHK", None))
        self.label.setText(QCoreApplication.translate("MainWindow", u"1. Pr\u00fcfungstag", None))
#if QT_CONFIG(tooltip)
        self.date1Edit.setToolTip("")
#endif // QT_CONFIG(tooltip)
        self.label_3.setText(QCoreApplication.translate("MainWindow", u"Pr\u00fcflinge", None))
        self.label_2.setText(QCoreApplication.translate("MainWindow", u"2. Pr\u00fcfungstag", None))
#if QT_CONFIG(tooltip)
        self.date2Edit.setToolTip("")
#endif // QT_CONFIG(tooltip)
        self.labelDate1.setText(QCoreApplication.translate("MainWindow", u"TextLabel", None))
        ___qtablewidgetitem = self.table1Widget.horizontalHeaderItem(0)
        ___qtablewidgetitem.setText(QCoreApplication.translate("MainWindow", u"Zeit", None));
        ___qtablewidgetitem1 = self.table1Widget.horizontalHeaderItem(1)
        ___qtablewidgetitem1.setText(QCoreApplication.translate("MainWindow", u"Pr\u00fcfling", None));
        ___qtablewidgetitem2 = self.table1Widget.horizontalHeaderItem(2)
        ___qtablewidgetitem2.setText(QCoreApplication.translate("MainWindow", u"Korrektoren", None));

        __sortingEnabled = self.table1Widget.isSortingEnabled()
        self.table1Widget.setSortingEnabled(False)
        self.table1Widget.setSortingEnabled(__sortingEnabled)

        self.labelDate2.setText(QCoreApplication.translate("MainWindow", u"TextLabel", None))
        ___qtablewidgetitem3 = self.table2Widget.horizontalHeaderItem(0)
        ___qtablewidgetitem3.setText(QCoreApplication.translate("MainWindow", u"Zeit", None));
        ___qtablewidgetitem4 = self.table2Widget.horizontalHeaderItem(1)
        ___qtablewidgetitem4.setText(QCoreApplication.translate("MainWindow", u"Pr\u00fcfling", None));
        ___qtablewidgetitem5 = self.table2Widget.horizontalHeaderItem(2)
        ___qtablewidgetitem5.setText(QCoreApplication.translate("MainWindow", u"Korrektoren", None));

        __sortingEnabled1 = self.table2Widget.isSortingEnabled()
        self.table2Widget.setSortingEnabled(False)
        self.table2Widget.setSortingEnabled(__sortingEnabled1)

        self.pushButtonCancelOptimize.setText(QCoreApplication.translate("MainWindow", u"Optimierung abbrechen", None))
        self.pushButtonCancel.setText(QCoreApplication.translate("MainWindow", u"Beenden", None))
        self.pushButtonOptimize.setText(QCoreApplication.translate("MainWindow", u"Aufteilen", None))
        self.menuDatei.setTitle(QCoreApplication.translate("MainWindow", u"Datei", None))
        self.menuPr_flinge.setTitle(QCoreApplication.translate("MainWindow", u"Pr\u00fcflinge", None))
        self.menuKorrektoren.setTitle(QCoreApplication.translate("MainWindow", u"Korrektoren", None))
        self.menuSession.setTitle(QCoreApplication.translate("MainWindow", u"Session", None))
        self.menuAnsicht.setTitle(QCoreApplication.translate("MainWindow", u"Ansicht", None))
        self.menuInfo.setTitle(QCoreApplication.translate("MainWindow", u"Info", None))
    # retranslateUi

