# Form implementation generated from reading ui file 'D:\llf\code\export-ui\ui\convert.ui'
#
# Created by: PyQt6 UI code generator 6.4.2
#
# WARNING: Any manual changes made to this file will be lost when pyuic6 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_Convert(object):
    def setupUi(self, Convert):
        Convert.setObjectName("Convert")
        Convert.resize(226, 111)
        self.centralwidget = QtWidgets.QWidget(parent=Convert)
        self.centralwidget.setObjectName("centralwidget")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.centralwidget)
        self.verticalLayout.setObjectName("verticalLayout")
        self.progressBar_convert = QtWidgets.QProgressBar(parent=self.centralwidget)
        self.progressBar_convert.setMaximum(0)
        self.progressBar_convert.setProperty("value", -1)
        self.progressBar_convert.setTextVisible(False)
        self.progressBar_convert.setOrientation(QtCore.Qt.Orientation.Horizontal)
        self.progressBar_convert.setTextDirection(QtWidgets.QProgressBar.Direction.BottomToTop)
        self.progressBar_convert.setObjectName("progressBar_convert")
        self.verticalLayout.addWidget(self.progressBar_convert)
        self.pushButton_stop = QtWidgets.QPushButton(parent=self.centralwidget)
        self.pushButton_stop.setObjectName("pushButton_stop")
        self.verticalLayout.addWidget(self.pushButton_stop)
        Convert.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(parent=Convert)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 226, 21))
        self.menubar.setObjectName("menubar")
        Convert.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(parent=Convert)
        self.statusbar.setObjectName("statusbar")
        Convert.setStatusBar(self.statusbar)

        self.retranslateUi(Convert)
        QtCore.QMetaObject.connectSlotsByName(Convert)

    def retranslateUi(self, Convert):
        _translate = QtCore.QCoreApplication.translate
        Convert.setWindowTitle(_translate("Convert", "Convert"))
        self.pushButton_stop.setText(_translate("Convert", "STOP"))
