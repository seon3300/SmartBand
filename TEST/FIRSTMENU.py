from PyQt5 import QtCore, QtGui, QtWidgets
from SELECTSUBJECTC import Ui_SELECTSUBJECTC
from SELECTSUBJECTT import Ui_SELECTSUBJECTT
from CLOCK import DigitalClock

class Ui_FIRSTMENU(object):

    def openWindow(self):
        self.window = QtWidgets.QMainWindow()
        self.ui = DigitalClock()
        self.ui.setupUi(self.window)
        FIRSTMENU.hide()
        self.window.show()

    def openWindow1(self):
        self.window = QtWidgets.QMainWindow()
        self.ui = Ui_SELECTSUBJECTC()
        self.ui.setupUi(self.window)
        FIRSTMENU.hide()
        self.window.show()

    def openWindow2(self):
        self.window = QtWidgets.QMainWindow()
        self.ui = Ui_SELECTSUBJECTT()
        self.ui.setupUi(self.window)
        FIRSTMENU.hide()
        self.window.show()

    def openWindow3(self):
        self.window = QtWidgets.QMainWindow()
        self.ui = Ui_FIRSTMENU()
        self.ui.setupUi(self.window)
        FIRSTMENU.hide()
        self.window.show()

    def setupUi(self, FIRSTMENU):
        FIRSTMENU.setObjectName("FIRSTMENU")
        FIRSTMENU.resize(200, 96)
        self.centralwidget = QtWidgets.QWidget(FIRSTMENU)
        self.centralwidget.setObjectName("centralwidget")

        self.btn_open = QtWidgets.QPushButton(self.centralwidget)
        self.btn_open.setIcon(QtGui.QIcon('clock.png'))
        self.btn_open.setIconSize(QtCore.QSize(40, 40))
        self.btn_open.setGeometry(QtCore.QRect(10, 25, 40, 40))
        self.btn_open.setObjectName("btn_open")
        self.btn_open.clicked.connect(self.openWindow)

        self.btn_open1 = QtWidgets.QPushButton(self.centralwidget)
        self.btn_open1.setIcon(QtGui.QIcon('camera.png'))
        self.btn_open1.setIconSize(QtCore.QSize(40, 40))
        self.btn_open1.setGeometry(QtCore.QRect(55, 25, 40, 40))
        self.btn_open1.setObjectName("btn_open1")
        self.btn_open1.clicked.connect(self.openWindow1)

        self.btn_open2 = QtWidgets.QPushButton(self.centralwidget)
        self.btn_open2.setIcon(QtGui.QIcon('stopwatch.png'))
        self.btn_open2.setIconSize(QtCore.QSize(40, 40))
        self.btn_open2.setGeometry(QtCore.QRect(100, 25, 40, 40))
        self.btn_open2.setObjectName("btn_open2")
        self.btn_open2.clicked.connect(self.openWindow2)

        self.btn_open3 = QtWidgets.QPushButton(self.centralwidget)
        self.btn_open3.setIcon(QtGui.QIcon('bluetooth.png'))
        self.btn_open3.setIconSize(QtCore.QSize(40, 40))
        self.btn_open3.setGeometry(QtCore.QRect(145, 25, 40, 40))
        self.btn_open3.setObjectName("btn_open3")
        self.btn_open3.clicked.connect(self.openWindow3)

        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(70, 40, 211, 41))
        font = QtGui.QFont()
        font.setPointSize(16)
        self.label.setFont(font)
        self.label.setObjectName("label")
        FIRSTMENU.setCentralWidget(self.centralwidget)
        self.statusbar = QtWidgets.QStatusBar(FIRSTMENU)
        self.statusbar.setObjectName("statusbar")
        FIRSTMENU.setStatusBar(self.statusbar)

if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    FIRSTMENU = QtWidgets.QMainWindow()
    ui = Ui_FIRSTMENU()
    ui.setupUi(FIRSTMENU)
    FIRSTMENU.show()
    sys.exit(app.exec_())