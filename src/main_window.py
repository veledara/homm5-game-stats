from typing import Optional
from PySide6.QtCore import Qt
from PySide6.QtWidgets import (
    QApplication,
    QMainWindow,
    QTableWidget,
    QTableWidgetItem,
    QLabel,
    QVBoxLayout,
    QWidget,
)
from PySide6.QtGui import QPixmap
from PySide6.QtCore import Qt
import datetime

from core.game_data import GameData
from ui_main_window import Ui_MainWindow


class MainWindow(QMainWindow, Ui_MainWindow):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.gamedata = GameData("src\config\hrta.json")
        self.fill_combo_boxes()
        self.hrta_table_widget.setColumnCount(4)
        self.rta_table_widget.setColumnCount(4)
        self.rw_table_widget.setColumnCount(4)
        self.xrta_table_widget.setColumnCount(4)
        self.hrta_table_widget.setHorizontalHeaderLabels(
            ["Дата", "Герой", "VS", "Герой Противника"]
        )
        self.rta_table_widget.setHorizontalHeaderLabels(
            ["Дата", "Герой", "VS", "Герой Противника"]
        )
        self.rw_table_widget.setHorizontalHeaderLabels(
            ["Дата", "Герой", "VS", "Герой Противника"]
        )
        self.xrta_table_widget.setHorizontalHeaderLabels(
            ["Дата", "Герой", "VS", "Герой Противника"]
        )
        self.addRecordButton.clicked.connect(self.add_record)

    def fill_combo_boxes(self):
        for race in self.gamedata.races:
            self.playerRaceComboBox.addItem(race.name)
            self.enemyRaceComboBox.addItem(race.name)

        self.update_heroes_combobox(self.playerRaceComboBox, self.playerHeroComboBox)
        self.update_heroes_combobox(self.enemyRaceComboBox, self.enemyHeroComboBox)

        self.playerRaceComboBox.currentIndexChanged.connect(
            lambda index: self.update_heroes_combobox(
                self.playerRaceComboBox, self.playerHeroComboBox
            )
        )
        self.enemyRaceComboBox.currentIndexChanged.connect(
            lambda index: self.update_heroes_combobox(
                self.enemyRaceComboBox, self.enemyHeroComboBox
            )
        )

    def update_heroes_combobox(self, raceComboBox, heroComboBox):
        heroComboBox.clear()
        selected_player_race_name = raceComboBox.currentText()
        heroes = self.gamedata.get_heroes_by_race(selected_player_race_name)
        if heroes is not None:
            for hero in heroes:
                heroComboBox.addItem(hero.name)

    def add_record(self):
        player_hero_name = self.playerHeroComboBox.currentText()
        enemy_hero_name = self.enemyHeroComboBox.currentText()

        hero_1 = self.gamedata.get_hero_by_name(player_hero_name)
        hero_2 = self.gamedata.get_hero_by_name(enemy_hero_name)

        win_state = self.winRadioButton.isChecked()

        if hero_1 and hero_2:
            current_tab = self.get_current_table()
            self.add_hero_row(
                current_tab,
                hero_1.image_path,
                hero_2.image_path,
                win_state,
            )

    def get_current_table(self):
        current_tab_index = self.tabWidget.currentIndex()
        current_tab_name = self.tabWidget.tabText(current_tab_index)
        if current_tab_name == "RTA":
            return self.rta_table_widget
        elif current_tab_name == "RW":
            return self.rw_table_widget
        elif current_tab_name == "HRTA":
            return self.hrta_table_widget
        elif current_tab_name == "XRTA":
            return self.xrta_table_widget
        else:
            return None

    def add_hero_row(self, table_widget, hero_image_1, hero_image_2, win_state):
        row_position = table_widget.rowCount()
        table_widget.insertRow(row_position)

        hero_pixmap_1 = QPixmap(hero_image_1).scaled(
            128, 128, Qt.KeepAspectRatio, Qt.SmoothTransformation
        )
        hero_pixmap_2 = QPixmap(hero_image_2).scaled(
            128, 128, Qt.KeepAspectRatio, Qt.SmoothTransformation
        )

        row_height = max(hero_pixmap_1.height(), hero_pixmap_2.height())
        table_widget.setRowHeight(row_position, row_height)
        table_widget.setColumnWidth(1, row_height)
        table_widget.setColumnWidth(3, row_height)

        date: str = datetime.datetime.now()
        date_label = QLabel(
            f"{date.strftime('%d')}.{date.strftime('%m')}.{date.strftime('%y')}"
        )
        date_label.setAlignment(Qt.AlignCenter)

        hero_label_1 = QLabel()
        hero_label_1.setPixmap(hero_pixmap_1)

        hero_label_2 = QLabel()
        hero_label_2.setPixmap(hero_pixmap_2)

        vs_label = QLabel("VS")
        vs_label.setAlignment(Qt.AlignCenter)

        table_widget.setCellWidget(row_position, 0, date_label)
        table_widget.setCellWidget(row_position, 1, hero_label_1)
        table_widget.setCellWidget(row_position, 2, vs_label)
        table_widget.setCellWidget(row_position, 3, hero_label_2)
