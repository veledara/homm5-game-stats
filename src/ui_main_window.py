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
    QLabel, QMainWindow, QPushButton, QRadioButton,
    QSizePolicy, QTabWidget, QTableWidget, QTableWidgetItem,
    QWidget)

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
        self.widget.setGeometry(QRect(850, 70, 231, 152))
        self.addRecordGrid = QGridLayout(self.widget)
        self.addRecordGrid.setObjectName(u"addRecordGrid")
        self.addRecordGrid.setContentsMargins(0, 0, 0, 0)
        self.playerHeroComboBox = QComboBox(self.widget)
        self.playerHeroComboBox.setObjectName(u"playerHeroComboBox")

        self.addRecordGrid.addWidget(self.playerHeroComboBox, 2, 1, 1, 1)

        self.enemyHeroComboBox = QComboBox(self.widget)
        self.enemyHeroComboBox.setObjectName(u"enemyHeroComboBox")

        self.addRecordGrid.addWidget(self.enemyHeroComboBox, 4, 1, 1, 1)

        self.winRadioButton = QRadioButton(self.widget)
        self.winRadioButton.setObjectName(u"winRadioButton")
        sizePolicy = QSizePolicy(QSizePolicy.Minimum, QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.winRadioButton.sizePolicy().hasHeightForWidth())
        self.winRadioButton.setSizePolicy(sizePolicy)
        self.winRadioButton.setLayoutDirection(Qt.LeftToRight)

        self.addRecordGrid.addWidget(self.winRadioButton, 5, 0, 1, 1, Qt.AlignHCenter)

        self.playerRaceComboBox = QComboBox(self.widget)
        self.playerRaceComboBox.setObjectName(u"playerRaceComboBox")

        self.addRecordGrid.addWidget(self.playerRaceComboBox, 2, 0, 1, 1)

        self.loseRadioButton = QRadioButton(self.widget)
        self.loseRadioButton.setObjectName(u"loseRadioButton")

        self.addRecordGrid.addWidget(self.loseRadioButton, 5, 1, 1, 1, Qt.AlignHCenter)

        self.addRecordButton = QPushButton(self.widget)
        self.addRecordButton.setObjectName(u"addRecordButton")

        self.addRecordGrid.addWidget(self.addRecordButton, 6, 0, 1, 2)

        self.enemyRaceComboBox = QComboBox(self.widget)
        self.enemyRaceComboBox.setObjectName(u"enemyRaceComboBox")

        self.addRecordGrid.addWidget(self.enemyRaceComboBox, 4, 0, 1, 1)

        self.enemyHeroLabel = QLabel(self.widget)
        self.enemyHeroLabel.setObjectName(u"enemyHeroLabel")

        self.addRecordGrid.addWidget(self.enemyHeroLabel, 3, 0, 1, 2, Qt.AlignHCenter)

        self.playerHeroLabel = QLabel(self.widget)
        self.playerHeroLabel.setObjectName(u"playerHeroLabel")

        self.addRecordGrid.addWidget(self.playerHeroLabel, 1, 0, 1, 2, Qt.AlignHCenter)

        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)

        self.tabWidget.setCurrentIndex(2)


        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"HoMM5 Stats", None))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.rta_tab), QCoreApplication.translate("MainWindow", u"RTA", None))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.rw_tab), QCoreApplication.translate("MainWindow", u"RW", None))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.hrta_tab), QCoreApplication.translate("MainWindow", u"HRTA", None))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.xrta_tab), QCoreApplication.translate("MainWindow", u"XRTA", None))
        self.winRadioButton.setText(QCoreApplication.translate("MainWindow", u"\u041f\u043e\u0431\u0435\u0434\u0430", None))
        self.loseRadioButton.setText(QCoreApplication.translate("MainWindow", u"\u041f\u043e\u0440\u0430\u0436\u0435\u043d\u0438\u0435", None))
        self.addRecordButton.setText(QCoreApplication.translate("MainWindow", u"\u0414\u043e\u0431\u0430\u0432\u0438\u0442\u044c \u043f\u0430\u0440\u0442\u0438\u044e", None))
        self.enemyHeroLabel.setText(QCoreApplication.translate("MainWindow", u"\u0412\u044b\u0431\u0435\u0440\u0438 \u0433\u0435\u0440\u043e\u044f \u043e\u043f\u043f\u043e\u043d\u0435\u043d\u0442\u0430", None))
        self.playerHeroLabel.setText(QCoreApplication.translate("MainWindow", u"\u0412\u044b\u0431\u0435\u0440\u0438 \u0441\u0432\u043e\u0435\u0433\u043e \u0433\u0435\u0440\u043e\u044f", None))
    # retranslateUi

