import sys
from PyQt6.QtWidgets import QMainWindow, QWidget, QPlainTextEdit, QApplication
from PyQt6.QtCore import QSize

class ClipBoardDemo(QMainWindow):

    def __init__(self):
        QMainWindow.__init__(self)

        self.setMinimumSize(QSize (440,240))
        self.setWindowTitle("ClipBoard Application Demo")

        self.textarea = QPlainTextEdit(self)

        self.textarea.setPlainText("You can perform editing on text, by right click of your mouse")
        self.textarea.move(10,10)

        self.textarea.resize (400,200)

        QApplication.clipboard().dataChanged.connect(self.textChanged)
    def textChanged(self):

        text = QApplication.clipboard().text() + "\n"
        print(text)
        self.textarea.insertPlainText(text)

if __name__ == '__main__':
    app = QApplication(sys.argv)
    widget = ClipBoardDemo()
    widget.show()
    sys.exit(app.exec())