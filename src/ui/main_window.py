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
from ui.ui_main_window import Ui_MainWindow


class MainWindow(QMainWindow, Ui_MainWindow):
    def __init__(self):
        super().__init__()
        self.setupUi(self)

        self.mods_dict = {
            "HRTA": self.hrta_table_widget,
            "RTA": self.rta_table_widget,
            "RW": self.rw_table_widget,
            "XRTA": self.xrta_table_widget,
        }
        for mod in self.mods_dict.values():
            mod.setColumnCount(4)
            mod.setHorizontalHeaderLabels(["Дата", "Герой", "VS", "Герой Противника"])

        self.gamedata = GameData("src\config\hrta.json")
        self.fill_combo_boxes()
        self.addRecordButton.clicked.connect(self.add_record)
        self.winRadioButton.click()

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
        return self.mods_dict.get(current_tab_name)

    def add_hero_row(
        self, table_widget, player_hero_image_path, enemy_player_image_path, win_state
    ):
        row_position = table_widget.rowCount()
        table_widget.insertRow(row_position)

        player_hero_pixmap = QPixmap(player_hero_image_path).scaled(
            128, 128, Qt.KeepAspectRatio, Qt.SmoothTransformation
        )
        enemy_hero_pixmap = QPixmap(enemy_player_image_path).scaled(
            128, 128, Qt.KeepAspectRatio, Qt.SmoothTransformation
        )

        player_hero_widget = QWidget()
        player_hero_layout = QVBoxLayout(player_hero_widget)
        player_hero_image = QLabel()
        player_hero_image.setPixmap(player_hero_pixmap)
        player_name = QLabel("Игрок 1")
        player_name.setAlignment(Qt.AlignCenter)
        player_hero_layout.addWidget(player_hero_image)
        player_hero_layout.addWidget(player_name)

        enemy_hero_widget = QWidget()
        enemy_hero_layout = QVBoxLayout(enemy_hero_widget)
        enemy_hero_image = QLabel()
        enemy_hero_image.setPixmap(enemy_hero_pixmap)
        enemy_name = QLabel("Игрок 2")
        enemy_name.setAlignment(Qt.AlignCenter)
        enemy_hero_layout.addWidget(enemy_hero_image)
        enemy_hero_layout.addWidget(enemy_name)

        player_hero_widget.setLayout(player_hero_layout)
        enemy_hero_widget.setLayout(enemy_hero_layout)

        row_height = max(
            player_hero_pixmap.height() + player_name.sizeHint().height(),
            enemy_hero_pixmap.height() + enemy_name.sizeHint().height(),
        )
        table_widget.setColumnWidth(1, row_height)
        table_widget.setColumnWidth(3, row_height)

        table_widget.setCellWidget(row_position, 1, player_hero_widget)
        table_widget.setCellWidget(row_position, 3, enemy_hero_widget)

        date = datetime.datetime.now().strftime("%d.%m.%y")
        date_label = QLabel(date)
        date_label.setAlignment(Qt.AlignCenter)
        table_widget.setColumnWidth(0, date_label.sizeHint().width() * 1.2)

        vs_label = QLabel("VS")
        vs_label.setAlignment(Qt.AlignCenter)
        table_widget.setColumnWidth(2, vs_label.sizeHint().width())

        table_widget.setItem(row_position, 0, QTableWidgetItem(date))
        table_widget.setCellWidget(row_position, 2, vs_label)

        table_widget.setRowHeight(
            row_position,
            player_hero_pixmap.height() + player_name.sizeHint().height(),
        )
