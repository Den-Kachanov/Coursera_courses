import sys
from PyQt6.QtWidgets import QApplication, QWidget, QPushButton, QMessageBox

class MessageBoxDemo(QWidget):

    def __init__(self):
        QWidget.__init__(self)

        self.setWindowTitle("MessageBox Application Demo")
        self.setGeometry(10,10,320,200)

        message = QMessageBox.warning(self,'Exit','Do You Want to Exit the Application', QMessageBox.StandardButton.Yes | QMessageBox.StandardButton.No)

        if message == QMessageBox.StandardButton.Yes:
            print("Yes Button Clicked. Closing Application")
            sys.exit()
        else:
            print("No Button Clicked. Returning to Application")

        self.show()


if __name__ == '__main__':
    app = QApplication(sys.argv)
    widget = MessageBoxDemo()
