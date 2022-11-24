import sys
from PyQt5.QtCore import *
from PyQt5.QtWidgets import *
from PyQt5.QtGui import *

from PyQt5 import QtCore, QtGui, QtWidgets


class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()

        self.centralwidget = QWidget()
        self.setCentralWidget(self.centralwidget)

        self.tabWidget = QtWidgets.QTabWidget(self.centralwidget)
        #self.tabWidget.setGeometry(QtCore.QRect(-10, 0, 1074, 621))
        #self.lcdNumber.setGeometry(QRect(0, 0, 551, 211))
        self.tabWidget.setGeometry(QRect(0, 0, 551, 211))

        self.tabWidget.setObjectName("tabWidget")
        self.tab = QtWidgets.QWidget()
        self.tab.setObjectName("tab")
        self.tabWidget.addTab(self.tab, "")
        self.tab_2 = QtWidgets.QWidget()
        self.tab_2.setObjectName("tab_2")
        self.tabWidget.addTab(self.tab_2, "")


        self.lcdNumber = QLCDNumber()
        self.lcdNumber.setGeometry(QRect(0, 0, 551, 211))
        self.lcdNumber.setProperty("intValue", 999)

        self.grid = QGridLayout(self.centralwidget)
        #self.grid.addWidget(self.lcdNumber)
        self.grid.addWidget(self.tabWidget)

if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = MainWindow()
    ex.resize(550, 246)
    ex.show()
    sys.exit(app.exec_()) 