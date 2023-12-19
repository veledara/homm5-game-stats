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
    QTextEdit
)
from PySide6.QtGui import QPixmap
from PySide6.QtCore import Qt
import datetime

from core.mode import Mode
from core.user import User
from core.game import Game
from ui.ui_main_window import Ui_MainWindow


class MainWindow(QMainWindow, Ui_MainWindow):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.addRecordWidget.hide()
        self.confirmNameButton.clicked.connect(self.enter_player_name)

    def enter_player_name(self) -> None:
        player_nickname = self.playerNameLineEdit.text().strip()
        if player_nickname:
            self.user = User(player_nickname)
            self.modes = {
                "HRTA": Mode(
                    "HRTA", "src\\config\\hrta_config.json", self.hrta_table_widget
                ),
                "RTA": Mode(
                    "RTA", "src\\config\\rta_config.json", self.rta_table_widget
                ),
                "RW": Mode("RW", "src\\config\\rw_config.json", self.rw_table_widget),
                "XRTA": Mode(
                    "XRTA", "src\\config\\xrta_config.json", self.xrta_table_widget
                ),
                "FRFB": Mode(
                    "FRFB", "src\\config\\frfb_config.json", self.frfb_table_widget
                ),
            }
            for mod in self.modes.values():
                mod.tab_widget.setColumnCount(6)
                mod.tab_widget.setHorizontalHeaderLabels(
                    ["Дата", "Вы", "VS", "Противник", "", "Заметки"]
                )

            self.enterYourNameWidget.hide()
            self.addRecordWidget.show()
            self.addRecordButton.clicked.connect(self.add_record)
            self.tabWidget.currentChanged.connect(self.fill_combo_boxes)
            self.winRadioButton.click()
            self.fill_combo_boxes()
        else:
            pass

    def get_current_mode(self) -> Mode:
        current_tab_name = self.tabWidget.tabText(self.tabWidget.currentIndex())
        return self.modes.get(current_tab_name)

    def fill_combo_boxes(self) -> None:
        current_mode = self.get_current_mode()
        if current_mode:
            for race in current_mode.get_races():
                self.playerRaceComboBox.addItem(race)
                self.enemyRaceComboBox.addItem(race)

            self.update_heroes_combobox(
                self.playerRaceComboBox, self.playerHeroComboBox
            )
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
        selected_race_name = raceComboBox.currentText()

        current_mode = self.get_current_mode()
        if current_mode:
            heroes = current_mode.get_heroes_by_race(selected_race_name)
            if heroes:
                for hero in heroes:
                    heroComboBox.addItem(hero.name)

    def add_record(self):
        player_hero_name = self.playerHeroComboBox.currentText()
        enemy_hero_name = self.enemyHeroComboBox.currentText()
        enemy_name = (
            self.enemyPlayerNameLineEdit.text().strip()
            if self.enemyPlayerNameLineEdit.text().strip() != ""
            else "Оппонент"
        )
        win_state = self.winRadioButton.isChecked()
        date = datetime.datetime.now()

        current_mode = self.get_current_mode()
        if current_mode:
            player_hero = current_mode.get_hero_by_name(player_hero_name)
            enemy_hero = current_mode.get_hero_by_name(enemy_hero_name)

            if player_hero and enemy_hero:
                new_game = Game(
                    current_mode.name,
                    player_hero,
                    enemy_hero,
                    win_state,
                    date,
                    self.user.name,
                    enemy_name,
                    notes="",
                )
                self.user.add_game(new_game)
                self.add_game_on_table(new_game)

    def add_game_on_table(self, game):
        table_widget = self.get_current_mode().get_tab_widget()
        row_position = table_widget.rowCount()
        table_widget.insertRow(row_position)

        player_hero_pixmap = QPixmap(game.player_hero.image_path).scaled(
            128, 128, Qt.KeepAspectRatio, Qt.SmoothTransformation
        )
        enemy_hero_pixmap = QPixmap(game.enemy_hero.image_path).scaled(
            128, 128, Qt.KeepAspectRatio, Qt.SmoothTransformation
        )

        player_hero_widget = QWidget()
        player_hero_layout = QVBoxLayout(player_hero_widget)
        player_hero_image = QLabel()
        player_hero_image.setPixmap(player_hero_pixmap)
        player_name = QLabel(game.player_name)
        player_name.setAlignment(Qt.AlignCenter)
        player_hero_layout.addWidget(player_hero_image)
        player_hero_layout.addWidget(player_name)

        enemy_hero_widget = QWidget()
        enemy_hero_layout = QVBoxLayout(enemy_hero_widget)
        enemy_hero_image = QLabel()
        enemy_hero_image.setPixmap(enemy_hero_pixmap)
        enemy_name = QLabel(game.enemy_name)
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

        date_label = QLabel(game.date.strftime("%d.%m.%y"))
        date_label.setAlignment(Qt.AlignCenter)
        table_widget.setColumnWidth(0, date_label.sizeHint().width() * 1.2)

        vs_label = QLabel("VS")
        vs_label.setAlignment(Qt.AlignCenter)

        win_indicator = QLabel()
        win_indicator.setStyleSheet(
            "QLabel { background-color: %s; }"
            % ("#008000" if game.win_state else "#9b111e")
        )
        table_widget.setColumnWidth(4, vs_label.sizeHint().width())

        notes_edit = QTextEdit()
        notes_edit.setPlaceholderText("Заметки по игре...")

        table_widget.setCellWidget(row_position, 5, notes_edit)

        table_widget.setCellWidget(row_position, 4, win_indicator)

        table_widget.setColumnWidth(2, vs_label.sizeHint().width())

        table_widget.setCellWidget(row_position, 0, date_label)

        table_widget.setCellWidget(row_position, 2, vs_label)

        table_widget.setRowHeight(
            row_position,
            player_hero_pixmap.height() + player_name.sizeHint().height(),
        )
