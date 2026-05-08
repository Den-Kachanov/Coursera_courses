import sys

from PyQt6.QtGui import QAction
from PyQt6.QtWidgets import QApplication, QMainWindow, QMenuBar, QStatusBar, QWidget



class TextPad(QMainWindow):

    def __init__(self):
        QWidget.__init__(self)

        menubar = self.menuBar()
        filemenu = menubar.addMenu('File')
        editmenu = menubar.addMenu('Edit')
        fontmenu = menubar.addMenu('Font')
        viewmenu = menubar.addMenu('View')

        self.statusbar = self.statusBar()
        self.statusbar.showMessage('Status Shown')

        self.viewAction = QAction('View status bar', self, checkable=True)
        self.viewAction.setStatusTip('View status bar')
        self.viewAction.setChecked(True)

        self.viewAction.triggered.connect(self.show_hide)

        viewmenu.addAction(self.viewAction)

        self.resize(400, 600)
        self.setWindowTitle("Menu bar demo")
        self.show()

    def show_hide(self, status):
        if status:
            self.statusbar.show()
        else:
            self.statusbar.hide()



if __name__ == '__main__':
    app = QApplication(sys.argv)

    widget = TextPad()

    widget.resize(400, 600)
    widget.show()

    sys.exit(app.exec())