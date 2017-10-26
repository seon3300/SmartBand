import sys

from PyQt5.QtWidgets import QApplication, QMainWindow, QPushButton, QWidget

class UIWindow(object):
    def setupUI(self, MainWindow):
        MainWindow.setGeometry(50, 50, 400, 450)
        MainWindow.setFixedSize(400, 450)
        self.centralwidget = QWidget(MainWindow)
        # mainwindow.setWindowIcon(QtGui.QIcon('PhotoIcon.png'))
        self.ToolsBTN = QPushButton('text', self.centralwidget)
        self.ToolsBTN.move(50, 350)
        MainWindow.setCentralWidget(self.centralwidget)


class UIwToolTab(object):
    def setupUI(self, MainaWindow):
        MainaWindow.setGeometry(50, 50, 400, 450)
        MainaWindow.setFixedSize(400, 450)
        self.centralwidget = QWidget(MainaWindow)
        self.sCPSBTN = QPushButton("text2", self.centralwidget)
        self.sCPSBTN.move(100, 350)
        MainaWindow.setCentralWidget(self.centralwidget)


class MainaWindow(QMainWindow):
    def __init__(self, parent=None):
        super(MainaWindow, self).__init__(parent)
        self.uiWindow = UIWindow()
        self.uiwToolTab = UIwToolTab()
        self.startUIWindow()

    def startUIwToolTab(self):
        self.uiwToolTab.setupUI(self)
        self.uiwToolTab.sCPSBTN.clicked.connect(self.startUIWindow)
        self.show()

    def startUIWindow(self):
        self.uiWindow.setupUI(self)
        self.uiWindow.ToolsBTN.clicked.connect(self.startUIwToolTab)
        self.show()


if __name__ == '__main__':
    app = QApplication(sys.argv)
    w = MainaWindow()
    sys.exit(app.exec_())