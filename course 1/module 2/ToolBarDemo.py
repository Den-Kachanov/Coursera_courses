import sys
from PyQt6.QtWidgets import QMainWindow, QApplication
from PyQt6.QtGui import QAction, QIcon

class ToolbarDemo(QMainWindow) :
    def __init__(self):
        QMainWindow.__init__(self)

        exitaction = QAction(QIcon('exit.png'), 'Exit', self)
        exitaction.setShortcut('Ctrl+E')
        exitaction.triggered.connect(QApplication.quit)

        self.toolbar = self.addToolBar('Exit')
        self.toolbar.addAction(exitaction)
        self.resize(400, 600)
        self.setWindowTitle("Tool Bar Demo")
        self.show()


def main():

    app = QApplication(sys.argv)

    widget = ToolbarDemo()

    sys.exit(app.exec())

if __name__ == '__main__':

    main()