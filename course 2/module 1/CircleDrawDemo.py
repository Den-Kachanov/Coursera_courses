from PyQt6.QtGui import QPainter, QPen, QBrush
from PyQt6.QtCore import Qt
from PyQt6.QtWidgets import QApplication, QMainWindow
from PyQt6.QtGui import QColor
import sys

class CircleDemo(QMainWindow):


    def __init__(self):
        QMainWindow.__init__(self)

        self.setWindowTitle("Circle Drawing Application")
        self.setGeometry(150,15,500,500)
        self.show()

    def paintEvent(self, event):
        painter = QPainter(self)
        painter.setPen(QPen(QColor("red"),5,Qt.PenStyle.DashLine))
        painter.setBrush(QBrush(QColor("yellow"), Qt.BrushStyle.CrossPattern))
        painter.drawEllipse(40, 40,400,400)


if __name__ == '__main__':
    app = QApplication(sys.argv)

    widget = CircleDemo()

    sys.exit(app.exec())