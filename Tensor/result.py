# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'result.ui'
#
# Created by: PyQt4 UI code generator 4.11.4
#
# WARNING! All changes made in this file will be lost!

from PyQt4 import QtCore, QtGui

try:
    _fromUtf8 = QtCore.QString.fromUtf8
except AttributeError:
    def _fromUtf8(s):
        return s

try:
    _encoding = QtGui.QApplication.UnicodeUTF8
    def _translate(context, text, disambig):
        return QtGui.QApplication.translate(context, text, disambig, _encoding)
except AttributeError:
    def _translate(context, text, disambig):
        return QtGui.QApplication.translate(context, text, disambig)

class Ui_result(object):
    def setupUi(self, result):
        result.setObjectName(_fromUtf8("result"))
        result.resize(723, 166)
        self.a11_lineEdit = QtGui.QLineEdit(result)
        self.a11_lineEdit.setGeometry(QtCore.QRect(110, 20, 191, 31))
        self.a11_lineEdit.setObjectName(_fromUtf8("a11_lineEdit"))
        self.a12_lineEdit = QtGui.QLineEdit(result)
        self.a12_lineEdit.setGeometry(QtCore.QRect(300, 20, 191, 31))
        self.a12_lineEdit.setObjectName(_fromUtf8("a12_lineEdit"))
        self.a13_lineEdit = QtGui.QLineEdit(result)
        self.a13_lineEdit.setGeometry(QtCore.QRect(490, 20, 191, 31))
        self.a13_lineEdit.setObjectName(_fromUtf8("a13_lineEdit"))
        self.a21_lineEdit = QtGui.QLineEdit(result)
        self.a21_lineEdit.setGeometry(QtCore.QRect(110, 50, 191, 31))
        self.a21_lineEdit.setObjectName(_fromUtf8("a21_lineEdit"))
        self.a22_lineEdit = QtGui.QLineEdit(result)
        self.a22_lineEdit.setGeometry(QtCore.QRect(300, 50, 191, 31))
        self.a22_lineEdit.setObjectName(_fromUtf8("a22_lineEdit"))
        self.a23_lineEdit = QtGui.QLineEdit(result)
        self.a23_lineEdit.setGeometry(QtCore.QRect(490, 50, 191, 31))
        self.a23_lineEdit.setObjectName(_fromUtf8("a23_lineEdit"))
        self.a31_lineEdit = QtGui.QLineEdit(result)
        self.a31_lineEdit.setGeometry(QtCore.QRect(110, 80, 191, 31))
        self.a31_lineEdit.setObjectName(_fromUtf8("a31_lineEdit"))
        self.a32_lineEdit = QtGui.QLineEdit(result)
        self.a32_lineEdit.setGeometry(QtCore.QRect(300, 80, 191, 31))
        self.a32_lineEdit.setObjectName(_fromUtf8("a32_lineEdit"))
        self.a33_lineEdit = QtGui.QLineEdit(result)
        self.a33_lineEdit.setGeometry(QtCore.QRect(490, 80, 191, 31))
        self.a33_lineEdit.setObjectName(_fromUtf8("a33_lineEdit"))
        self.label = QtGui.QLabel(result)
        self.label.setGeometry(QtCore.QRect(70, 3, 51, 121))
        font = QtGui.QFont()
        font.setFamily(_fromUtf8("Abyssinica SIL"))
        font.setPointSize(90)
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(50)
        self.label.setFont(font)
        self.label.setObjectName(_fromUtf8("label"))
        self.label_2 = QtGui.QLabel(result)
        self.label_2.setGeometry(QtCore.QRect(680, 3, 51, 121))
        font = QtGui.QFont()
        font.setFamily(_fromUtf8("Abyssinica SIL"))
        font.setPointSize(90)
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(50)
        self.label_2.setFont(font)
        self.label_2.setObjectName(_fromUtf8("label_2"))
        self.label_3 = QtGui.QLabel(result)
        self.label_3.setGeometry(QtCore.QRect(3, 45, 91, 31))
        font = QtGui.QFont()
        font.setPointSize(21)
        self.label_3.setFont(font)
        self.label_3.setObjectName(_fromUtf8("label_3"))
        self.closePushButton = QtGui.QPushButton(result)
        self.closePushButton.setGeometry(QtCore.QRect(580, 130, 99, 27))
        self.closePushButton.setObjectName(_fromUtf8("closePushButton"))

        self.retranslateUi(result)
        QtCore.QMetaObject.connectSlotsByName(result)

    def retranslateUi(self, result):
        result.setWindowTitle(_translate("result", "Dialog", None))
        self.label.setText(_translate("result", "[", None))
        self.label_2.setText(_translate("result", "]", None))
        self.label_3.setText(_translate("result", "Nxx = ", None))
        self.closePushButton.setText(_translate("result", "Close", None))

