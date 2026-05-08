import sys

from PyQt6.QtWidgets import QApplication, QWidget

def main():

    app = QApplication(sys.argv)
    widget = QWidget()
    widget.resize(250, 280)

    widget.setWindowTitle("First PyQT6 application")
    widget.move(300, 300)
    widget.show()
    sys.exit(app.exec())


if __name__ == '__main__':
    main()