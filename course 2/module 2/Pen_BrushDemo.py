from PyQt6.QtGui import QColor
from PyQt6.QtGui import *
from PyQt6 import QtCore
from PyQt6.QtCore import Qt

from PyQt6.QtWidgets import *
import sys

class ArrowDemo(QMainWindow):

    def __init__(self):
        QMainWindow.__init__(self)
        self.setWindowTitle("Arrow Draw Application")
        self.setGeometry(150,150,500,500)
        self.show()

    def paintEvent(self, event):
        painter = QPainter(self)

        painter.setPen(QPen(QColor("red"), 5, Qt.PenStyle.SolidLine))
        painter.drawLine(20, 40, 250, 40)

        painter.setPen(QPen(QColor("red"), 5, Qt.PenStyle.DashLine))
        painter.drawLine(20, 80, 250, 80)

        painter.setPen(QPen(QColor("red"), 5, Qt.PenStyle.DashDotLine))
        painter.drawLine(20, 120, 2560, 120)

        painter.setPen(QPen(QColor("red"), 5, Qt.PenStyle.DotLine))
        painter.drawLine(20, 160, 250, 160)

        painter.setPen(QPen(QColor("red"), 5, Qt.PenStyle.DashDotDotLine))
        painter.drawLine(20, 200, 250, 200)

        pen = QPen()
        pen.setStyle(Qt.PenStyle.CustomDashLine)

        pen.setDashPattern([1,4,5,4])
        painter.setPen(pen)
        painter.drawLine(20, 240, 250, 240)


if __name__ == '__main__':
    app = QApplication(sys.argv)
    window = ArrowDemo()
    sys.exit(app.exec())