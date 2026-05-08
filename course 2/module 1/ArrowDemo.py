from PyQt6.QtGui import *
from PyQt6 import QtCore

from PyQt6.QtWidgets import *
from PyQt6.QtGui import QColor
import sys

class ArrowDemo(QMainWindow):

    def __init__(self):
        QMainWindow.__init__(self)

        self.setWindowTitle ("Arrow Draw Application")
        self.setGeometry(150,150,500,500)
        self.show()

    def paintEvent(self, event):
        painter = QPainter(self)
        painter.setRenderHint(QPainter.RenderHint.Antialiasing)
        painter.setPen(QColor("red"))
        painter.setBrush(QColor("green"))
        painter.drawLine(480,150,100,100)
        painter.drawLine(156,150,100,100)
        painter.drawLine(150,50,100,100)

if __name__ == '__main__':
    app = QApplication(sys.argv)
    window = ArrowDemo()
    sys.exit(app.exec())