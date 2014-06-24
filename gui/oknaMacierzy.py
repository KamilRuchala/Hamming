import sys
from PyQt4 import QtGui, QtCore
from oknoG import Ui_Dialog

class oknoM(QtGui.QWidget):
	typ=""
       	text=""
	newtext=""
	macierz=None	
   	def __init__(self,iden,mac):
        	super(oknoM, self).__init__()
        	self.macierz=mac
		if iden=="G":
       			self.typ="G"
		else:
			self.typ="H"
		(m,n)=self.macierz.shape # rozmiar macierzy: m-liczba wierszy
		for i in xrange(m):
			for x in xrange(n): # sprowadzam macierz do formy teksowej
				tmp=int(self.macierz[i,x]) # jak tego nie bedzie to zestringuje floata
				self.text = self.text + str(tmp) +" "
			self.text=self.text+"\n"
		self.initUI(m,n)
    	def initUI(self,a,b):
		#rozmiary, szer znaku + spacja=14px, wysokosc wraz z enterem=18px      
		#wzor na rozmiar: l.wier*14 + 2*40 x l.kolumn * 18 +2*40 // 2*40 odleglosci od kazdej z krawedzi
		dlg=b*20+40
		wys= a*14 +40
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
		qp.setPen(QtGui.QColor(0, 0, 0))
		qp.setFont(QtGui.QFont('Decorative', 10))
		qp.drawText(event.rect(), QtCore.Qt.AlignCenter, self.text) 
		qp.setFont(QtGui.QFont('Decorative', 16))
		qp.drawText(event.rect(), QtCore.Qt.AlignVCenter, self.typ+"=") 
