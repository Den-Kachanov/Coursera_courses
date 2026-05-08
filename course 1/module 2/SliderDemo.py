import sys

from PyQt6 import QtGui
from PyQt6.QtWidgets import QApplication, QWidget, QHBoxLayout, QLabel, QSlider
from PyQt6.QtCore import Qt

class SliderDemo(QWidget):

    def __init__(self):
        QWidget.__init__(self)

        self.setWindowTitle("Slider Demo")
        self.resize(400, 600)

        hbox = QHBoxLayout()
        self.slider = QSlider()

        self.slider.setOrientation(Qt.Orientation.Horizontal)
        self.slider.setTickPosition(QSlider.TickPosition.TicksBelow)
        self.slider.setTickInterval(1)
        self.slider.setMinimum(0)
        self.slider.setMaximum(100)

        self.slider.valueChanged.connect(self.sliderdata)

        self.slidervalue = QLabel("0")
        self.slidervalue.setFont(QtGui.QFont("sans-serif", 18))

        hbox.addWidget(self.slider)
        hbox.addWidget(self.slidervalue)

        self.setLayout(hbox)

        self.show()

    def sliderdata(self):
        size = self.slider.value()
        self.slidervalue.setText(str(size))

if __name__ == '__main__':
    app = QApplication(sys.argv)
    widget = SliderDemo()

    sys.exit(app.exec())