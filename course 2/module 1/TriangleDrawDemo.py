from PyQt6.QtGui import QPainter, QPainterPath, QPen, QBrush
from PyQt6.QtCore import Qt
from PyQt6.QtWidgets import QApplication, QMainWindow
from PyQt6.QtGui import QColor
import sys

class TriangleDemo(QMainWindow):


    def __init__(self):
        QMainWindow.__init__(self)

        self.setWindowTitle("Triangle Drawing Application")
        self.setGeometry(150,15,500,500)
        self.show()

    def paintEvent(self, event):
        painter = QPainter(self)
        path = QPainterPath()
        painter.setPen(QPen(QColor("red"),5,Qt.PenStyle.DashLine))
        painter.setBrush(QBrush(QColor("blue")))
        path.lineTo(160, 400)
        path.lineTo(350, 100)
        path.lineTo(10, 25)

        painter.drawPath(path)


if __name__ == '__main__':
    app = QApplication(sys.argv)

    widget = TriangleDemo()

    sys.exit(app.exec())