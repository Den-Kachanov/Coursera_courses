import sys
from PyQt6.QtWidgets import QApplication
from PyQt6.QtCore import Qt
from PyQt6.QtWidgets import QWidget, QLCDNumber, QSlider, QVBoxLayout

class SignalsDemo(QWidget):

    def __init__(self):
        QWidget.__init__(self)

        lcd = QLCDNumber (self)
        slider = QSlider(Qt.Orientation.Horizontal, self)

        vbox = QVBoxLayout()
        vbox.addWidget (lcd)
        vbox.addWidget (slider)

        self.setLayout(vbox)
        slider.valueChanged.connect(lcd. display)

        self.setGeometry(300,300,250,250)
        self.setWindowTitle("Event & Signals Application Demo")
        self.show()

def main():
    app = QApplication(sys.argv)
    widget = SignalsDemo()
    sys.exit(app.exec())

if __name__ == '__main__':
    main()