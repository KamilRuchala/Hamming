# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'lista.ui'
#
# Created: Mon Jun 23 22:50:04 2014
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
        okno_lista.setWindowTitle(QtGui.QApplication.translate("okno_lista", "Lista kodów", None, QtGui.QApplication.UnicodeUTF8))
        self.zamknijButton.setText(QtGui.QApplication.translate("okno_lista", "Zamknij", None, QtGui.QApplication.UnicodeUTF8))

