# Form implementation generated from reading ui file '.\design.ui'
#
# Created by: PyQt6 UI code generator 6.7.0
#
# WARNING: Any manual changes made to this file will be lost when pyuic6 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt6 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(503, 96)
        self.centralwidget = QtWidgets.QWidget(parent=MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.gridLayout = QtWidgets.QGridLayout(self.centralwidget)
        self.gridLayout.setObjectName("gridLayout")
        self.archiveLabel = QtWidgets.QLabel(parent=self.centralwidget)
        self.archiveLabel.setMinimumSize(QtCore.QSize(0, 25))
        self.archiveLabel.setWordWrap(True)
        self.archiveLabel.setObjectName("archiveLabel")
        self.gridLayout.addWidget(self.archiveLabel, 0, 0, 1, 1)
        self.statusLabel = QtWidgets.QLabel(parent=self.centralwidget)
        self.statusLabel.setAlignment(QtCore.Qt.AlignmentFlag.AlignRight|QtCore.Qt.AlignmentFlag.AlignTrailing|QtCore.Qt.AlignmentFlag.AlignVCenter)
        self.statusLabel.setObjectName("statusLabel")
        self.gridLayout.addWidget(self.statusLabel, 0, 1, 1, 1)
        self.extractProgressBar = QtWidgets.QProgressBar(parent=self.centralwidget)
        self.extractProgressBar.setMinimumSize(QtCore.QSize(0, 25))
        self.extractProgressBar.setProperty("value", 24)
        self.extractProgressBar.setObjectName("extractProgressBar")
        self.gridLayout.addWidget(self.extractProgressBar, 1, 0, 1, 2)
        self.currentFileLabel = QtWidgets.QLabel(parent=self.centralwidget)
        self.currentFileLabel.setObjectName("currentFileLabel")
        self.gridLayout.addWidget(self.currentFileLabel, 2, 0, 1, 2)
        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.archiveLabel.setText(_translate("MainWindow", "TextLabel"))
        self.statusLabel.setText(_translate("MainWindow", "TextLabel"))
        self.currentFileLabel.setText(_translate("MainWindow", "TextLabel"))