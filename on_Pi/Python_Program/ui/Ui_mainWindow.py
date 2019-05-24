# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file '/home/pi/myProject/myProject/ui/mainWindow.ui'
#
# Created by: PyQt5 UI code generator 5.7
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(427, 319)
        self.centralWidget = QtWidgets.QWidget(MainWindow)
        self.centralWidget.setObjectName("centralWidget")
        self.btnExit = QtWidgets.QPushButton(self.centralWidget)
        self.btnExit.setGeometry(QtCore.QRect(260, 240, 141, 61))
        self.btnExit.setObjectName("btnExit")
        self.slRed = QtWidgets.QSlider(self.centralWidget)
        self.slRed.setGeometry(QtCore.QRect(80, 20, 321, 20))
        self.slRed.setMaximum(255)
        self.slRed.setOrientation(QtCore.Qt.Horizontal)
        self.slRed.setObjectName("slRed")
        self.slGreen = QtWidgets.QSlider(self.centralWidget)
        self.slGreen.setGeometry(QtCore.QRect(80, 60, 321, 16))
        self.slGreen.setMaximum(255)
        self.slGreen.setOrientation(QtCore.Qt.Horizontal)
        self.slGreen.setObjectName("slGreen")
        self.slBlue = QtWidgets.QSlider(self.centralWidget)
        self.slBlue.setGeometry(QtCore.QRect(80, 100, 321, 16))
        self.slBlue.setMaximum(255)
        self.slBlue.setOrientation(QtCore.Qt.Horizontal)
        self.slBlue.setObjectName("slBlue")
        self.label = QtWidgets.QLabel(self.centralWidget)
        self.label.setGeometry(QtCore.QRect(10, 20, 59, 14))
        self.label.setObjectName("label")
        self.label_2 = QtWidgets.QLabel(self.centralWidget)
        self.label_2.setGeometry(QtCore.QRect(10, 60, 59, 14))
        self.label_2.setObjectName("label_2")
        self.label_3 = QtWidgets.QLabel(self.centralWidget)
        self.label_3.setGeometry(QtCore.QRect(10, 100, 59, 14))
        self.label_3.setObjectName("label_3")
        MainWindow.setCentralWidget(self.centralWidget)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.btnExit.setText(_translate("MainWindow", "Exit"))
        self.label.setText(_translate("MainWindow", "red"))
        self.label_2.setText(_translate("MainWindow", "green"))
        self.label_3.setText(_translate("MainWindow", "blue"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())

