import sys
import qdarkstyle

from PySide6 import QtWidgets
from ui.main_window import MainWindow

app = QtWidgets.QApplication(sys.argv)
app.setStyleSheet(qdarkstyle.load_stylesheet())

window = MainWindow()
window.show()

app.exec()