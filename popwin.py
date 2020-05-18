# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'popwin.ui'
#
# Created by: PyQt5 UI code generator 5.14.1
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_Pop(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(858, 613)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.centralwidget)
        self.verticalLayout.setObjectName("verticalLayout")
        self.gridLayout_3 = QtWidgets.QGridLayout()
        self.gridLayout_3.setObjectName("gridLayout_3")
        self.gridLayout_2 = QtWidgets.QGridLayout()
        self.gridLayout_2.setObjectName("gridLayout_2")
        self.popwindow = PlotWidget(self.centralwidget)
        self.popwindow.setObjectName("popwindow")
        self.gridLayout_2.addWidget(self.popwindow, 0, 0, 1, 1)
        self.popwindowF = PlotWidget(self.centralwidget)
        self.popwindowF.setObjectName("popwindowF")
        self.gridLayout_2.addWidget(self.popwindowF, 0, 1, 1, 1)
        self.gridLayout_3.addLayout(self.gridLayout_2, 0, 0, 1, 1)
        self.gridLayout = QtWidgets.QGridLayout()
        self.gridLayout.setObjectName("gridLayout")
        self.soundonbutton = QtWidgets.QPushButton(self.centralwidget)
        self.soundonbutton.setText("")
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap("sound.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.soundonbutton.setIcon(icon)
        self.soundonbutton.setIconSize(QtCore.QSize(50, 50))
        self.soundonbutton.setObjectName("soundonbutton")
        self.gridLayout.addWidget(self.soundonbutton, 0, 0, 1, 1)
        self.muteButton = QtWidgets.QPushButton(self.centralwidget)
        self.muteButton.setText("")
        icon1 = QtGui.QIcon()
        icon1.addPixmap(QtGui.QPixmap("stop.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.muteButton.setIcon(icon1)
        self.muteButton.setIconSize(QtCore.QSize(50, 50))
        self.muteButton.setObjectName("muteButton")
        self.gridLayout.addWidget(self.muteButton, 0, 1, 1, 1)
        self.gridLayout_3.addLayout(self.gridLayout, 1, 0, 1, 1)
        self.verticalLayout.addLayout(self.gridLayout_3)
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 858, 26))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "Difference of outputs"))
from pyqtgraph import PlotWidget


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_Pop()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())
