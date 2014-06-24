import sys
from PyQt4 import QtGui, QtCore
from oknoG import Ui_Dialog

class oknoS(QtGui.QWidget):
	typ="H"
       	text="" # tekstowa macierz
	text1="[ " # tekstowy syndrom
	textP=""
	syndrom=None
	pozycja=0 # pozycja bledu
	macierz=None	
   	def __init__(self,macH,syn,poz):
        	super(oknoS, self).__init__()
        	self.macierz=macH
		self.syndrom=syn
		self.pozycja=poz
		(m,n)=self.macierz.shape # rozmiar macierzy: m-liczba wierszy
		for i in xrange(m): # sprowadzam macierz do formy teksowej
			for x in xrange(n):
				tmp=int(self.macierz[i,x]) # jak tego nie bedzie to zestringuje floata
				self.text = self.text + str(tmp) +" "
			self.text=self.text+"\n"
		for a in xrange(len(self.syndrom)):
			self.text1=self.text1+str(self.syndrom[a])+" "
		self.text1=self.text1+"]"
		self.textP="Syndrom: "+self.text1+" jest rowny kolumnie nr "+str(self.pozycja+1)+". macierzy H,\nczyli blad wystepuje wlasnie na tej pozycji"
		self.initUI(m,n)
    	def initUI(self,a,b):
		dlg=b*25+300
		wys= a*14 +120
        	self.setGeometry(300, 300,dlg,wys)
        	self.setWindowTitle('Macierz '+self.typ)
		self.zam = QtGui.QPushButton('Zamknij', self)
		self.zam.move(dlg-57,wys-22)
		self.setFixedSize(self.size());
        	self.show()

	def paintEvent(self, event):
		qp = QtGui.QPainter()
		qp.begin(self)
		self.drawText(event, qp)
		qp.end()
		
	def drawText(self, event, qp):
		qp.setPen(QtGui.QColor(128, 0, 0))
		qp.setFont(QtGui.QFont('Decorative', 11))
		qp.drawText(event.rect(), QtCore.Qt.AlignHCenter, self.textP)
		qp.setPen(QtGui.QColor(0, 0, 0))
		qp.setFont(QtGui.QFont('Decorative', 10))
		qp.drawText(event.rect(), QtCore.Qt.AlignCenter, self.text) 
		qp.setFont(QtGui.QFont('Decorative', 16))
		qp.drawText(event.rect(), QtCore.Qt.AlignVCenter, self.typ+"=") 
