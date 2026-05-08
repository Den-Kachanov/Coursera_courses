import sys
from PyQt6.QtCore import Qt
from PyQt6.QtWidgets import QApplication, QLabel, QGridLayout,QWidget
from PyQt6.QtGui import QPixmap

class ImageDisp(QWidget):

    def __init__(self):
        QWidget.__init__(self)

        self.image = QPixmap("/home/den/Pictures/2082226.jpg").scaled(200, 200, Qt.AspectRatioMode.KeepAspectRatio)
        self.label = QLabel()
        self.label.setPixmap(self.image)

        self.grid = QGridLayout()
        self.grid.addWidget(self.label, 1, 1)
        self.setLayout(self.grid)


        self.setGeometry(50,50,500,500)
        self.setWindowTitle("Image Disp Application")
        self.show()

if __name__ == '__main__':
    app = QApplication(sys.argv)
    widget = ImageDisp()
    sys.exit(app.exec())