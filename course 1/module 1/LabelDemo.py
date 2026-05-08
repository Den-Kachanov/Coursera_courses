import sys
from PyQt6.QtWidgets import QApplication, QWidget, QLabel

def main():

    app = QApplication(sys.argv)

    widget = QWidget()

    text = QLabel(widget)
    text.setText("PyQt6 applcation test")
    text.move(118, 85)

    widget.resize(400, 600)
    widget.setWindowTitle("Label demo")
    widget.show()
    sys.exit(app.exec())

if __name__ == '__main__':
    main()