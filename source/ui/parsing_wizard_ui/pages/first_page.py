# Form implementation generated from reading ui file 'parse_wizard_1.ui'
#
# Created by: PyQt6 UI code generator 6.2.1
#
# WARNING: Any manual changes made to this file will be lost when pyuic6 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt6 import QtCore, QtGui, QtWidgets


class WizardFirstPageUi:

    def setupUi(self, FirstPage):
        FirstPage.setObjectName("FirstPage")
        FirstPage.resize(346, 214)
        self.gridLayout = QtWidgets.QGridLayout(FirstPage)
        self.gridLayout.setObjectName("gridLayout")
        self.label = QtWidgets.QLabel(FirstPage)
        font = QtGui.QFont()
        font.setPointSize(10)
        self.label.setFont(font)
        self.label.setObjectName("label")
        self.gridLayout.addWidget(self.label, 0, 0, 1, 2)
        self.verticalLayout = QtWidgets.QVBoxLayout()
        self.verticalLayout.setObjectName("verticalLayout")
        self.OnlineTrade = QtWidgets.QCheckBox(FirstPage)
        font = QtGui.QFont()
        font.setPointSize(9)
        self.OnlineTrade.setFont(font)
        self.OnlineTrade.setObjectName("OnlineTrade")
        self.verticalLayout.addWidget(self.OnlineTrade)
        self.EKatalog = QtWidgets.QCheckBox(FirstPage)
        font = QtGui.QFont()
        font.setPointSize(9)
        self.EKatalog.setFont(font)
        self.EKatalog.setObjectName("EKatalog")
        self.verticalLayout.addWidget(self.EKatalog)
        self.Citilink = QtWidgets.QCheckBox(FirstPage)
        font = QtGui.QFont()
        font.setPointSize(9)
        self.Citilink.setFont(font)
        self.Citilink.setObjectName("Citilink")
        self.verticalLayout.addWidget(self.Citilink)
        self.Eldorado = QtWidgets.QCheckBox(FirstPage)
        font = QtGui.QFont()
        font.setPointSize(9)
        self.Eldorado.setFont(font)
        self.Eldorado.setObjectName("Eldorado")
        self.verticalLayout.addWidget(self.Eldorado)
        self.gridLayout.addLayout(self.verticalLayout, 1, 0, 1, 2)
        spacerItem = QtWidgets.QSpacerItem(119, 20, QtWidgets.QSizePolicy.Policy.Expanding, QtWidgets.QSizePolicy.Policy.Minimum)
        self.gridLayout.addItem(spacerItem, 2, 0, 1, 1)
        self.horizontalLayout = QtWidgets.QHBoxLayout()
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.CancelButton = QtWidgets.QPushButton(FirstPage)
        self.CancelButton.setObjectName("CancelButton")
        self.horizontalLayout.addWidget(self.CancelButton)
        self.OkButton = QtWidgets.QPushButton(FirstPage)
        self.OkButton.setObjectName("OkButton")
        self.horizontalLayout.addWidget(self.OkButton)
        self.gridLayout.addLayout(self.horizontalLayout, 2, 1, 1, 1)

        self.retranslateUi(FirstPage)
        QtCore.QMetaObject.connectSlotsByName(FirstPage)

    def retranslateUi(self, FirstPage):
        _translate = QtCore.QCoreApplication.translate
        FirstPage.setWindowTitle(_translate("FirstPage", "Parsing wizard"))
        self.label.setText(_translate("FirstPage", "Choose stores to get products:"))
        self.OnlineTrade.setText(_translate("FirstPage", "Online Trade"))
        self.EKatalog.setText(_translate("FirstPage", "E-Katalog"))
        self.Citilink.setText(_translate("FirstPage", "Citilink"))
        self.Eldorado.setText(_translate("FirstPage", "Eldorado"))
        self.CancelButton.setText(_translate("FirstPage", "Cancel"))
        self.OkButton.setText(_translate("FirstPage", "OK"))


# if __name__ == "__main__":
#     import sys
#     app = QtWidgets.QApplication(sys.argv)
#     FirstPage = QtWidgets.QWidget()
#     ui = WizardFirstPageUi()
#     ui.setupUi(FirstPage)
#     FirstPage.show()
#     sys.exit(app.exec())
