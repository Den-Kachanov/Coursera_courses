import sys
from PyQt6.QtWidgets import QApplication, QWidget, QLabel, QLineEdit, QPushButton

class App(QWidget):

    def __init__(self):
        QWidget.__init__(self)
        self.namelabel = QLabel(self)
        self.namelabel.move(30, 50)
        self.namelabel.setText("Enter your name:")

        self.name = QLineEdit(self)
        self.name.move(140, 45)

        self.submit = QPushButton(self)
        self.submit.setText("Submit")
        self.submit.move(280, 45)

        self.resize(400, 600)
        self.setWindowTitle("Text Box Demo")
        self.submit.clicked.connect(self.showname)

    def showname(self):
        a = self.name.text()
        print(a)



if __name__ == '__main__':
    app = QApplication(sys.argv)

    widget = App()

    widget.resize(400, 600)
    widget.show()

    sys.exit(app.exec())
