from PyQt6.QtWidgets import *
from PyQt6.QtGui import *
from PyQt6.QtCore import *
import sys

class BrushStyles(QMainWindow):

    def __init__(self):
        QMainWindow.__init__(self)

        self.setWindowTitle("Brush Style Demo")
        self.setGeometry(150, 150, 500, 500)
        self.show()

    def paintEvent(self, event):
        painter = QPainter(self)

        brush = QBrush(Qt.BrushStyle.SolidPattern)
        painter.setBrush(brush)
        painter.drawRect(10,15, 90,60)

        brush = QBrush(Qt.BrushStyle.Dense1Pattern)
        painter.setBrush(brush)
        painter.drawRect(130, 15, 90, 60)

        brush = QBrush(Qt.BrushStyle.Dense2Pattern)
        painter.setBrush(brush)
        painter.drawRect(250, 15, 90, 60)

        brush = QBrush(Qt.BrushStyle.Dense3Pattern)
        painter.setBrush(brush)
        painter.drawRect(370, 15, 90, 60)


        brush = QBrush(Qt.BrushStyle.Dense4Pattern)
        painter.setBrush(brush)
        painter.drawRect(10, 105, 90, 60)


        brush = QBrush(Qt.BrushStyle.Dense5Pattern)
        painter.setBrush(brush)
        painter.drawRect(130, 105, 90, 60)


        brush = QBrush(Qt.BrushStyle.Dense6Pattern)
        painter.setBrush(brush)
        painter.drawRect(250, 105, 90, 60)

        brush = QBrush(Qt.BrushStyle.DiagCrossPattern)
        painter.setBrush(brush)
        painter.drawRect(370, 105, 90, 60)

        brush = QBrush(Qt.BrushStyle.HorPattern)
        painter.setBrush(brush)
        painter.drawRect(10, 190, 90, 60)

        brush = QBrush(Qt.BrushStyle.VerPattern)
        painter.setBrush(brush)
        painter.drawRect(130, 190, 90, 60)

        brush = QBrush(Qt.BrushStyle.BDiagPattern)
        painter.setBrush(brush)
        painter.drawRect(250, 190, 90, 60)

if __name__ == '__main__':
    
    app = QApplication(sys.argv)
    window = BrushStyles()

    sys.exit(app.exec())