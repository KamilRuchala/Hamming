# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'listaSyndrom.ui'
#
# Created: Tue Jun 24 01:30:05 2014
#      by: PyQt4 UI code generator 4.9.3
#
# WARNING! All changes made in this file will be lost!

from PyQt4 import QtCore, QtGui

try:
    _fromUtf8 = QtCore.QString.fromUtf8
except AttributeError:
    _fromUtf8 = lambda s: s

class Ui_okno_lista(object):
    def setupUi(self, okno_lista):
        okno_lista.setObjectName(_fromUtf8("okno_lista"))
        okno_lista.resize(399, 300)
        okno_lista.setMaximumSize(QtCore.QSize(399, 300))
        self.zamknijButton = QtGui.QPushButton(okno_lista)
        self.zamknijButton.setGeometry(QtCore.QRect(310, 260, 81, 23))
        self.zamknijButton.setObjectName(_fromUtf8("zamknijButton"))
        self.textBrowser = QtGui.QTextBrowser(okno_lista)
        self.textBrowser.setGeometry(QtCore.QRect(10, 20, 381, 221))
        self.textBrowser.setObjectName(_fromUtf8("textBrowser"))

        self.retranslateUi(okno_lista)
        QtCore.QMetaObject.connectSlotsByName(okno_lista)

    def retranslateUi(self, okno_lista):
        okno_lista.setWindowTitle(QtGui.QApplication.translate("okno_lista", "Lista Syndromów", None, QtGui.QApplication.UnicodeUTF8))
        self.zamknijButton.setText(QtGui.QApplication.translate("okno_lista", "Zamknij", None, QtGui.QApplication.UnicodeUTF8))
        self.textBrowser.setHtml(QtGui.QApplication.translate("okno_lista", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'DejaVu Sans\'; font-size:9pt; font-weight:400; font-style:normal;\">\n"
"<p style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><br /></p></body></html>", None, QtGui.QApplication.UnicodeUTF8))

