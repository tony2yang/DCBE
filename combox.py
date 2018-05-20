# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'combox.ui'
#
# Created by: PyQt5 UI code generator 5.10.1
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_Form(object):
    def setupUi(self, Form):
        Form.setObjectName("Form")
        Form.resize(370, 335)
        Form.setMinimumSize(QtCore.QSize(370, 335))
        Form.setMaximumSize(QtCore.QSize(370, 335))
        Form.setCursor(QtGui.QCursor(QtCore.Qt.ArrowCursor))
        Form.setMouseTracking(True)
        Form.setFocusPolicy(QtCore.Qt.ClickFocus)
        self.pushButton_3 = QtWidgets.QPushButton(Form)
        self.pushButton_3.setGeometry(QtCore.QRect(30, 300, 75, 23))
        self.pushButton_3.setObjectName("pushButton_3")
        self.widget = QtWidgets.QWidget(Form)
        self.widget.setGeometry(QtCore.QRect(32, 32, 299, 259))
        self.widget.setObjectName("widget")
        self.verticalLayout_2 = QtWidgets.QVBoxLayout(self.widget)
        self.verticalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.textBrowser = QtWidgets.QTextBrowser(self.widget)
        self.textBrowser.viewport().setProperty("cursor", QtGui.QCursor(QtCore.Qt.OpenHandCursor))
        self.textBrowser.setMouseTracking(True)
        self.textBrowser.setOpenExternalLinks(True)
        self.textBrowser.setOpenLinks(True)
        self.textBrowser.setObjectName("textBrowser")
        self.verticalLayout_2.addWidget(self.textBrowser)
        spacerItem = QtWidgets.QSpacerItem(20, 28, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.verticalLayout_2.addItem(spacerItem)
        self.horizontalLayout = QtWidgets.QHBoxLayout()
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.lineEdit = QtWidgets.QLineEdit(self.widget)
        self.lineEdit.setObjectName("lineEdit")
        self.horizontalLayout.addWidget(self.lineEdit)
        self.browserFile_btn = QtWidgets.QPushButton(self.widget)
        self.browserFile_btn.setObjectName("browserFile_btn")
        self.horizontalLayout.addWidget(self.browserFile_btn)
        self.addLink_btn = QtWidgets.QPushButton(self.widget)
        self.addLink_btn.setObjectName("addLink_btn")
        self.horizontalLayout.addWidget(self.addLink_btn)
        self.verticalLayout_2.addLayout(self.horizontalLayout)
        self.widget1 = QtWidgets.QWidget(Form)
        self.widget1.setGeometry(QtCore.QRect(172, 300, 158, 25))
        self.widget1.setObjectName("widget1")
        self.formLayout = QtWidgets.QFormLayout(self.widget1)
        self.formLayout.setContentsMargins(0, 0, 0, 0)
        self.formLayout.setObjectName("formLayout")
        self.pushButton_2 = QtWidgets.QPushButton(self.widget1)
        self.pushButton_2.setObjectName("pushButton_2")
        self.formLayout.setWidget(0, QtWidgets.QFormLayout.LabelRole, self.pushButton_2)
        self.pushButton = QtWidgets.QPushButton(self.widget1)
        self.pushButton.setObjectName("pushButton")
        self.formLayout.setWidget(0, QtWidgets.QFormLayout.FieldRole, self.pushButton)

        self.retranslateUi(Form)
        self.addLink_btn.clicked.connect(Form.add)
        self.browserFile_btn.clicked.connect(Form.file_path)
        self.pushButton_2.clicked.connect(Form.saveRecords)
        self.textBrowser.anchorClicked['QUrl'].connect(Form.setFocus)
        self.pushButton.clicked.connect(Form.close)
        self.pushButton_3.clicked.connect(Form.reset)
        QtCore.QMetaObject.connectSlotsByName(Form)

    def retranslateUi(self, Form):
        _translate = QtCore.QCoreApplication.translate
        Form.setWindowTitle(_translate("Form", "Form"))
        self.pushButton_3.setText(_translate("Form", "Reset"))
        self.browserFile_btn.setText(_translate("Form", "Browser"))
        self.addLink_btn.setText(_translate("Form", "Add"))
        self.pushButton_2.setText(_translate("Form", "Save"))
        self.pushButton.setText(_translate("Form", "Exit"))

