import sys
from PyQt6.QtWidgets import QPushButton, QWidget, QLineEdit, QApplication

class DragButton(QPushButton):

    def __init__(self, Title, Parent):
        QPushButton.__init__(self, Title, Parent)
        self.setAcceptDrops(True)

    def dragEnterEvent(self, event):
        if event.mimeData().hasFormat("text/plain"):
            event.accept()
        else:
            event.ignore()

    def dropEvent(self, event):
        self.setText(event.mineData().text())

class DragAndDrop(QWidget):

    def __init__(self):
        QWidget.__init__(self)

        edit = QLineEdit('"',self)
        edit.setDragEnabled(True)

        edit.move (30,65)

        self.setWindowTitle("Drag & Drop Application")
        self.setGeometry(300,300,500,500)

        button = DragButton("Drag and Drop Button", self)
        button.move(190, 65)

def main():
    app = QApplication(sys.argv)
    widget = DragAndDrop()
    widget.show()
    sys.exit(app.exec())

if __name__ == '__main__':
    main()