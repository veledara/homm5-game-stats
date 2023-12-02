import json
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


class HeroVsTable(QMainWindow):
    def __init__(self):
        super().__init__()

        self.game_data = GameData("src\config\hrta.json")

        # Настройка окна
        self.setWindowTitle("Герои HoMM5")
        self.resize(800, 600)
        # Создание таблицы
        self.table_widget = QTableWidget()

        # Установка количества колонок
        self.table_widget.setColumnCount(
            6
        )  # два изображения, два имени героя, один 'VS'

        # Установка заголовков колонок
        self.table_widget.setHorizontalHeaderLabels(
            ["Дата", "Герой", "Имя игрока 1", "VS", "Герой 2", "Имя игрока 1"]
        )

        # Добавление строк (пример с одной строкой)
        self.add_hero_row(
            "Имя героя 1",
            r"src\resources\races\dungeon\heroes\Eruina.png",
            "Имя игрока 1",
            "Имя героя 2",
            r"src\resources\races\dungeon\heroes\Lethos.png",
            "Имя игрока 2",
            True,
        )
        self.add_hero_row(
            "Имя героя 1",
            r"src\resources\races\dungeon\heroes\Eruina.png",
            "Имя игрока 1",
            "Имя героя 2",
            r"src\resources\races\dungeon\heroes\Lethos.png",
            "Имя игрока 2",
            False,
        )

        # Размещение таблицы в окне
        layout = QVBoxLayout()
        layout.addWidget(self.table_widget)
        container = QWidget()
        container.setLayout(layout)
        self.setCentralWidget(container)

    def add_hero_row(
        self,
        hero_name_1,
        hero_image_1,
        player_name_1,
        hero_name_2,
        hero_image_2,
        player_name_2,
        win_state,
    ):
        row_position = self.table_widget.rowCount()
        self.table_widget.insertRow(row_position)

        # Загрузка изображений героев
        hero_pixmap_1 = QPixmap(hero_image_1).scaled(128, 128, Qt.KeepAspectRatio, Qt.SmoothTransformation)  # Задайте нужные размеры
        hero_pixmap_2 = QPixmap(hero_image_2).scaled(128, 128, Qt.KeepAspectRatio, Qt.SmoothTransformation)  # Задайте нужные размеры

        row_height = max(hero_pixmap_1.height(), hero_pixmap_2.height())
        self.table_widget.setRowHeight(row_position, row_height)
        self.table_widget.setColumnWidth(1, row_height)
        self.table_widget.setColumnWidth(5, row_height)

        # Создание виджетов для отображения информации
        date: str = datetime.datetime.now()
        date_label = QLabel(f"{date.strftime('%d')}.{date.strftime('%m')}.{date.strftime('%y')}")
        date_label.setAlignment(Qt.AlignCenter)

        hero_label_1 = QLabel()
        hero_label_1.setPixmap(hero_pixmap_1)

        hero_label_2 = QLabel()
        hero_label_2.setPixmap(hero_pixmap_2)

        vs_label = QLabel("VS")
        vs_label.setAlignment(Qt.AlignCenter)

        # Добавление виджетов в таблицу
        self.table_widget.setCellWidget(row_position, 0, date_label)
        self.table_widget.setCellWidget(row_position, 1, hero_label_1)
        self.table_widget.setItem(row_position, 2, QTableWidgetItem(player_name_1))
        self.table_widget.setCellWidget(row_position, 3, vs_label)
        self.table_widget.setItem(row_position, 4, QTableWidgetItem(player_name_2))
        self.table_widget.setCellWidget(row_position, 5, hero_label_2)


# Создание и запуск приложения
app = QApplication([])
window = HeroVsTable()
window.show()
app.exec()
