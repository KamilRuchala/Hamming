# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'generator.ui'
#
# Created: Thu May 29 17:27:53 2014
#      by: PyQt4 UI code generator 4.9.3
#
# WARNING! All changes made in this file will be lost!

from PyQt4 import QtCore, QtGui

try:
    _fromUtf8 = QtCore.QString.fromUtf8
except AttributeError:
    _fromUtf8 = lambda s: s

class Ui_Form(object):
    def setupUi(self, Form):
        Form.setObjectName(_fromUtf8("Form"))
        Form.resize(316, 98)
        Form.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.suwak = QtGui.QSlider(Form)
        self.suwak.setGeometry(QtCore.QRect(10, 40, 281, 20))
        self.suwak.setMaximum(30)
        self.suwak.setPageStep(5)
        self.suwak.setOrientation(QtCore.Qt.Horizontal)
        self.suwak.setObjectName(_fromUtf8("suwak"))
        self.pushOk = QtGui.QPushButton(Form)
        self.pushOk.setGeometry(QtCore.QRect(220, 70, 81, 23))
        self.pushOk.setObjectName(_fromUtf8("pushOk"))
        self.label = QtGui.QLabel(Form)
        self.label.setGeometry(QtCore.QRect(10, 10, 251, 16))
        self.label.setObjectName(_fromUtf8("label"))
        self.ile = QtGui.QLabel(Form)
        self.ile.setGeometry(QtCore.QRect(300, 40, 20, 20))
        self.ile.setObjectName(_fromUtf8("ile"))

        self.retranslateUi(Form)
        QtCore.QObject.connect(self.pushOk, QtCore.SIGNAL(_fromUtf8("clicked()")), Form.close)
        QtCore.QMetaObject.connectSlotsByName(Form)

    def retranslateUi(self, Form):
        Form.setWindowTitle(QtGui.QApplication.translate("Form", "Generator", None, QtGui.QApplication.UnicodeUTF8))
        self.pushOk.setText(QtGui.QApplication.translate("Form", "OK", None, QtGui.QApplication.UnicodeUTF8))
        self.label.setText(QtGui.QApplication.translate("Form", "Ustaw dlugosc losowego ciagu", None, QtGui.QApplication.UnicodeUTF8))
        self.ile.setText(QtGui.QApplication.translate("Form", "0", None, QtGui.QApplication.UnicodeUTF8))

