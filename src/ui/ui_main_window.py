# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'main_window.ui'
##
## Created by: Qt User Interface Compiler version 6.6.0
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
from PySide6.QtWidgets import (QApplication, QComboBox, QGridLayout, QHeaderView,
    QLabel, QLineEdit, QMainWindow, QPushButton,
    QRadioButton, QSizePolicy, QTabWidget, QTableWidget,
    QTableWidgetItem, QVBoxLayout, QWidget)

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.setEnabled(True)
        MainWindow.resize(1280, 720)
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.centralwidget.setEnabled(True)
        self.tabWidget = QTabWidget(self.centralwidget)
        self.tabWidget.setObjectName(u"tabWidget")
        self.tabWidget.setGeometry(QRect(40, 40, 800, 640))
        self.tabWidget.setTabPosition(QTabWidget.North)
        self.tabWidget.setTabShape(QTabWidget.Rounded)
        self.tabWidget.setElideMode(Qt.ElideNone)
        self.tabWidget.setUsesScrollButtons(True)
        self.tabWidget.setMovable(True)
        self.tabWidget.setTabBarAutoHide(False)
        self.rta_tab = QWidget()
        self.rta_tab.setObjectName(u"rta_tab")
        self.rta_table_widget = QTableWidget(self.rta_tab)
        self.rta_table_widget.setObjectName(u"rta_table_widget")
        self.rta_table_widget.setGeometry(QRect(0, 0, 800, 640))
        self.tabWidget.addTab(self.rta_tab, "")
        self.rw_tab = QWidget()
        self.rw_tab.setObjectName(u"rw_tab")
        self.rw_table_widget = QTableWidget(self.rw_tab)
        self.rw_table_widget.setObjectName(u"rw_table_widget")
        self.rw_table_widget.setGeometry(QRect(0, 0, 800, 640))
        self.tabWidget.addTab(self.rw_tab, "")
        self.hrta_tab = QWidget()
        self.hrta_tab.setObjectName(u"hrta_tab")
        self.hrta_tab.setAutoFillBackground(False)
        self.hrta_table_widget = QTableWidget(self.hrta_tab)
        self.hrta_table_widget.setObjectName(u"hrta_table_widget")
        self.hrta_table_widget.setGeometry(QRect(0, 0, 800, 640))
        self.tabWidget.addTab(self.hrta_tab, "")
        self.xrta_tab = QWidget()
        self.xrta_tab.setObjectName(u"xrta_tab")
        self.xrta_table_widget = QTableWidget(self.xrta_tab)
        self.xrta_table_widget.setObjectName(u"xrta_table_widget")
        self.xrta_table_widget.setGeometry(QRect(0, 0, 800, 640))
        self.tabWidget.addTab(self.xrta_tab, "")
        self.widget = QWidget(self.centralwidget)
        self.widget.setObjectName(u"widget")
        self.widget.setGeometry(QRect(870, 190, 361, 195))
        self.addRecordLayout = QGridLayout(self.widget)
        self.addRecordLayout.setObjectName(u"addRecordLayout")
        self.addRecordLayout.setContentsMargins(0, 0, 0, 0)
        self.enemyHeroComboBox = QComboBox(self.widget)
        self.enemyHeroComboBox.setObjectName(u"enemyHeroComboBox")

        self.addRecordLayout.addWidget(self.enemyHeroComboBox, 3, 2, 1, 2)

        self.addRecordButton = QPushButton(self.widget)
        self.addRecordButton.setObjectName(u"addRecordButton")

        self.addRecordLayout.addWidget(self.addRecordButton, 6, 0, 1, 4)

        self.playerHeroComboBox = QComboBox(self.widget)
        self.playerHeroComboBox.setObjectName(u"playerHeroComboBox")

        self.addRecordLayout.addWidget(self.playerHeroComboBox, 1, 2, 1, 2)

        self.enemyRaceComboBox = QComboBox(self.widget)
        self.enemyRaceComboBox.setObjectName(u"enemyRaceComboBox")

        self.addRecordLayout.addWidget(self.enemyRaceComboBox, 3, 0, 1, 2)

        self.winRadioButton = QRadioButton(self.widget)
        self.winRadioButton.setObjectName(u"winRadioButton")
        sizePolicy = QSizePolicy(QSizePolicy.Minimum, QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.winRadioButton.sizePolicy().hasHeightForWidth())
        self.winRadioButton.setSizePolicy(sizePolicy)
        self.winRadioButton.setLayoutDirection(Qt.LeftToRight)

        self.addRecordLayout.addWidget(self.winRadioButton, 4, 0, 1, 2, Qt.AlignHCenter)

        self.playerHeroLabel = QLabel(self.widget)
        self.playerHeroLabel.setObjectName(u"playerHeroLabel")

        self.addRecordLayout.addWidget(self.playerHeroLabel, 0, 0, 1, 4, Qt.AlignHCenter)

        self.loseRadioButton = QRadioButton(self.widget)
        self.loseRadioButton.setObjectName(u"loseRadioButton")

        self.addRecordLayout.addWidget(self.loseRadioButton, 4, 2, 1, 2, Qt.AlignHCenter)

        self.enemyPlayerNameLineEdit = QLineEdit(self.widget)
        self.enemyPlayerNameLineEdit.setObjectName(u"enemyPlayerNameLineEdit")

        self.addRecordLayout.addWidget(self.enemyPlayerNameLineEdit, 5, 2, 1, 2)

        self.enemyHeroLabel = QLabel(self.widget)
        self.enemyHeroLabel.setObjectName(u"enemyHeroLabel")

        self.addRecordLayout.addWidget(self.enemyHeroLabel, 2, 0, 1, 4, Qt.AlignHCenter)

        self.playerRaceComboBox = QComboBox(self.widget)
        self.playerRaceComboBox.setObjectName(u"playerRaceComboBox")

        self.addRecordLayout.addWidget(self.playerRaceComboBox, 1, 0, 1, 2)

        self.enemyPlayerNameLabel = QLabel(self.widget)
        self.enemyPlayerNameLabel.setObjectName(u"enemyPlayerNameLabel")

        self.addRecordLayout.addWidget(self.enemyPlayerNameLabel, 5, 0, 1, 2, Qt.AlignHCenter)

        self.widget1 = QWidget(self.centralwidget)
        self.widget1.setObjectName(u"widget1")
        self.widget1.setGeometry(QRect(870, 70, 361, 101))
        self.playerNameLayout = QVBoxLayout(self.widget1)
        self.playerNameLayout.setObjectName(u"playerNameLayout")
        self.playerNameLayout.setContentsMargins(0, 0, 0, 0)
        self.enterYourNameLabel = QLabel(self.widget1)
        self.enterYourNameLabel.setObjectName(u"enterYourNameLabel")

        self.playerNameLayout.addWidget(self.enterYourNameLabel)

        self.playerNameLineEdit = QLineEdit(self.widget1)
        self.playerNameLineEdit.setObjectName(u"playerNameLineEdit")

        self.playerNameLayout.addWidget(self.playerNameLineEdit)

        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)

        self.tabWidget.setCurrentIndex(3)


        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"HoMM5 Stats", None))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.rta_tab), QCoreApplication.translate("MainWindow", u"RTA", None))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.rw_tab), QCoreApplication.translate("MainWindow", u"RW", None))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.hrta_tab), QCoreApplication.translate("MainWindow", u"HRTA", None))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.xrta_tab), QCoreApplication.translate("MainWindow", u"XRTA", None))
        self.addRecordButton.setText(QCoreApplication.translate("MainWindow", u"\u0414\u043e\u0431\u0430\u0432\u0438\u0442\u044c \u043f\u0430\u0440\u0442\u0438\u044e", None))
        self.winRadioButton.setText(QCoreApplication.translate("MainWindow", u"\u041f\u043e\u0431\u0435\u0434\u0430", None))
        self.playerHeroLabel.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><p><span style=\" font-size:12pt; font-weight:700;\">\u0412\u044b\u0431\u0435\u0440\u0438 \u0441\u0432\u043e\u0435\u0433\u043e \u0433\u0435\u0440\u043e\u044f</span></p></body></html>", None))
        self.loseRadioButton.setText(QCoreApplication.translate("MainWindow", u"\u041f\u043e\u0440\u0430\u0436\u0435\u043d\u0438\u0435", None))
        self.enemyPlayerNameLineEdit.setText("")
        self.enemyHeroLabel.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><p><span style=\" font-size:12pt; font-weight:700;\">\u0412\u044b\u0431\u0435\u0440\u0438 \u0433\u0435\u0440\u043e\u044f \u043e\u043f\u043f\u043e\u043d\u0435\u043d\u0442\u0430</span></p></body></html>", None))
        self.enemyPlayerNameLabel.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><p>\u0412\u0432\u0435\u0434\u0438\u0442\u0435 \u043d\u0438\u043a\u043d\u0435\u0439\u043c \u043e\u043f\u043f\u043e\u043d\u0435\u043d\u0442\u0430:</p></body></html>", None))
        self.enterYourNameLabel.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><p align=\"center\"><span style=\" font-size:12pt; font-weight:700;\">\u041f\u0440\u0438\u0432\u0435\u0442! \u0414\u043b\u044f \u043d\u0430\u0447\u0430\u043b\u0430, \u0432\u0432\u0435\u0434\u0438 \u0441\u0432\u043e\u0439 \u0438\u0433\u0440\u043e\u0432\u043e\u0439 \u043d\u0438\u043a.</span></p><p align=\"center\"><span style=\" font-size:12pt; font-weight:700;\">\u041e\u043d \u0431\u0443\u0434\u0435\u0442 \u043e\u0442\u043e\u0431\u0440\u0430\u0436\u0430\u0442\u044c\u0441\u044f \u0432 \u0442\u0430\u0431\u043b\u0438\u0446\u0435 \u0438\u0433\u0440.</span></p></body></html>", None))
        self.playerNameLineEdit.setText("")
    # retranslateUi

