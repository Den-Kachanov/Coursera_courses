import sys

from PyQt6.QtCore import qChecksum
from PyQt6.QtWidgets import QApplication, QWidget, QCheckBox, QLabel

class Hobbies(QWidget):

    def __init__(self):
        QWidget.__init__(self)

        label = QLabel()
        label.setText("Hobbies")
        label.move(65, 20)

        hobby_1 = QCheckBox('Dancing', self)
        hobby_1.move(65, 40)
        hobby_1.toggle()

        hobby_2 = QCheckBox('Signing', self)
        hobby_2.move(65, 60)

        hobby_3 = QCheckBox('Reading', self)
        hobby_3.move(65, 80)

        self.resize(400, 600)
        self.setWindowTitle("CheckBox")
        self.show()

if __name__ == '__main__':
    app = QApplication(sys.argv)

    widget = Hobbies()
    sys.exit(app.exec())