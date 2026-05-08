import sys
from PyQt6.QtWidgets import QApplication, QGridLayout, QWidget, QRadioButton

class RadioDemo(QWidget):

    def __init__(self):
        QWidget.__init__(self)
        self.resize(100, 200)
        layout = QGridLayout()
        self.setLayout(layout)

        radio_button = QRadioButton("Male")
        radio_button.setChecked(True)
        radio_button.gender = "Male"
        radio_button.toggled.connect(self.onClicked)
        layout.addWidget(radio_button, 0, 0)

        radio_button_2 = QRadioButton("Female")
        radio_button_2.gender = "Female"
        radio_button_2.toggled.connect(self.onClicked)
        layout.addWidget(radio_button_2, 0, 1)

        radio_button_3 = QRadioButton("Other")
        radio_button_3.gender = "Other"
        radio_button_3.toggled.connect(self.onClicked)
        layout.addWidget(radio_button_3)

    def onClicked(self):
        RadioButton = self.sender()
        if RadioButton.isChecked():
            print(f"Gender is {RadioButton.gender}")


if __name__ == '__main__':
    app = QApplication(sys.argv)

    widget = RadioDemo()
    widget.setWindowTitle("Radio button demo")
    widget.show()
    sys.exit(app.exec())