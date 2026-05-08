import sys

from PyQt6.QtWidgets import QApplication, QComboBox, QWidget, QLabel

class Price(QWidget):

    def __init__(self):
        QWidget.__init__(self)

        price = QComboBox(self)
        price.addItem("0-100")
        price.addItem("100-200")
        price.addItem("200-300")
        price.addItem("300-400")
        price.addItem("400-500")
        price.addItem("500+")
        price.move(50, 50)
        price.show()

        self.label = QLabel(self)
        self.label.move(50, 20)
        self.label.show()

        price.textActivated.connect(self.OnChanged)

        self.setWindowTitle("ComboBox")
        self.resize(400, 600)
        self.show()

    def OnChanged(self, text):
        print(text)
        self.label.adjustSize()
        self.label.setText(text)

if __name__ == '__main__':
    app = QApplication(sys.argv)
    widget = Price()

    sys.exit(app.exec())