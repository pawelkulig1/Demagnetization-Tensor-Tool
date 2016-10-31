# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'helpWindow.ui'
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

class Ui_helpWindow(object):
    def setupUi(self, helpWindow):
        helpWindow.setObjectName(_fromUtf8("helpWindow"))
        helpWindow.resize(400, 300)
        self.textBrowser = QtGui.QTextBrowser(helpWindow)
        self.textBrowser.setGeometry(QtCore.QRect(70, 40, 256, 192))
        self.textBrowser.setObjectName(_fromUtf8("textBrowser"))
        self.closePushButton = QtGui.QPushButton(helpWindow)
        self.closePushButton.setGeometry(QtCore.QRect(300, 260, 89, 27))
        self.closePushButton.setObjectName(_fromUtf8("closePushButton"))

        self.retranslateUi(helpWindow)
        QtCore.QMetaObject.connectSlotsByName(helpWindow)

    def retranslateUi(self, helpWindow):
        helpWindow.setWindowTitle(_translate("helpWindow", "Help", None))
        self.textBrowser.setHtml(_translate("helpWindow", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'Sans Serif\'; font-size:10pt; font-weight:400; font-style:normal;\">\n"
"<p align=\"center\" style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">Here will be help.</p>\n"
"<p align=\"center\" style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><br /></p>\n"
"<p align=\"center\" style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><br /></p>\n"
"<p align=\"center\" style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">Paweł Kulig.</p>\n"
"<p align=\"center\" style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">pawelkulig1@gmail.com</p>\n"
"<p align=\"center\" style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">AGH University of Science and Technology</p></body></html>", None))
        self.closePushButton.setText(_translate("helpWindow", "Close", None))


if __name__ == "__main__":
    import sys
    app = QtGui.QApplication(sys.argv)
    helpWindow = QtGui.QWidget()
    ui = Ui_helpWindow()
    ui.setupUi(helpWindow)
    helpWindow.show()
    sys.exit(app.exec_())

