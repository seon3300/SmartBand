from PyQt5.QtCore import QTime, QTimer
from PyQt5.QtWidgets import QApplication, QLCDNumber
from PyQt5 import QtWidgets

class DigitalClock(QLCDNumber):



    # def __init__(self, parent=None):
    def setupUi(self, parent=None):
        super(DigitalClock, self).__init__(parent)
        self.setSegmentStyle(QLCDNumber.Filled)
        # clockUI.setObjectName("clcok")
        # clockUI.resize(200, 96)
        timer = QTimer(self)
        timer.timeout.connect(self.showTime)
        timer.start(1000)
        self.showTime()
        self.resize(200, 96)

    def showTime(self):
        time = QTime.currentTime()
        text = time.toString('hh:mm')
        if (time.second() % 2) == 0:
            text = text[:2] + ' ' + text[3:]

        self.display(text)


if __name__ == '__main__':
    import sys

    app = QApplication(sys.argv)
    clockUI = QtWidgets.QMainWindow()
    clock = DigitalClock()
    clock.setupUi(clockUI)
    clockUI.show()
    # clock.show()
    sys.exit(app.exec_())