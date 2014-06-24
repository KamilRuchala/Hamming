# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'wprowadz_dzielnik.ui'
#
# Created: Mon Jun 23 23:31:33 2014
#      by: PyQt4 UI code generator 4.9.3
#
# WARNING! All changes made in this file will be lost!

from PyQt4 import QtCore, QtGui

try:
    _fromUtf8 = QtCore.QString.fromUtf8
except AttributeError:
    _fromUtf8 = lambda s: s

class Ui_oknoDzielnik(object):
    def setupUi(self, oknoDzielnik):
        oknoDzielnik.setObjectName(_fromUtf8("oknoDzielnik"))
        oknoDzielnik.resize(400, 101)
        self.okButton = QtGui.QPushButton(oknoDzielnik)
        self.okButton.setGeometry(QtCore.QRect(310, 70, 81, 23))
        self.okButton.setObjectName(_fromUtf8("okButton"))
        self.dzielnikInput = QtGui.QLineEdit(oknoDzielnik)
        self.dzielnikInput.setGeometry(QtCore.QRect(20, 30, 361, 20))
        self.dzielnikInput.setObjectName(_fromUtf8("dzielnikInput"))
        self.label = QtGui.QLabel(oknoDzielnik)
        self.label.setGeometry(QtCore.QRect(20, 10, 221, 16))
        self.label.setObjectName(_fromUtf8("label"))

        self.retranslateUi(oknoDzielnik)
        QtCore.QMetaObject.connectSlotsByName(oknoDzielnik)

    def retranslateUi(self, oknoDzielnik):
        oknoDzielnik.setWindowTitle(QtGui.QApplication.translate("oknoDzielnik", "Własny dzielnik", None, QtGui.QApplication.UnicodeUTF8))
        self.okButton.setText(QtGui.QApplication.translate("oknoDzielnik", "OK", None, QtGui.QApplication.UnicodeUTF8))
        self.label.setText(QtGui.QApplication.translate("oknoDzielnik", "Wprowadz wektor błedu:", None, QtGui.QApplication.UnicodeUTF8))

