import sys
sys.path.insert(0, '../Hamming')
from PyQt4 import QtCore, QtGui
from koderHamming import *
import numpy


from mainwindow import Ui_MainWindow
class StartQT4(QtGui.QMainWindow):
	info="" 
	kontrolka=None # zmienna jesli =1 to wykonano kodowanie jesli =0 to dekodowanie
	wektorb="" # potrzebny do zapamietania wb
	pozycjaBledu=None
	G=None
	H=None # macierze G i H 
	syndrom=None
	def __init__(self, parent=None):
		QtGui.QWidget.__init__(self, parent)
		# nazwa klasy
		self.ui = Ui_MainWindow()
		self.ui.setupUi(self)
		self.ui.hammingInput.setFocus()
	 	self.setFixedSize(self.size())

		QtCore.QObject.connect(self.ui.encodeButton,QtCore.SIGNAL("clicked()"), self.kodujHammingiem)
		QtCore.QObject.connect(self.ui.generateButton,QtCore.SIGNAL("clicked()"), self.generatorHam)
		QtCore.QObject.connect(self.ui.errorButton,QtCore.SIGNAL("clicked()"), self.errorHam)
		QtCore.QObject.connect(self.ui.clearOutHam,QtCore.SIGNAL("clicked()"), self.clearHam)
		QtCore.QObject.connect(self.ui.detekcjaButton,QtCore.SIGNAL("clicked()"), self.detekcjaHam)
		QtCore.QObject.connect(self.ui.korekcjaButton,QtCore.SIGNAL("clicked()"), self.korekcjaHam)
		QtCore.QObject.connect(self.ui.pokazG,QtCore.SIGNAL("clicked()"), self.pokazG)
		QtCore.QObject.connect(self.ui.pokazH,QtCore.SIGNAL("clicked()"), self.pokazH)
		QtCore.QObject.connect(self.ui.pokazSposob,QtCore.SIGNAL("clicked()"), self.pokazSposob)
		QtCore.QObject.connect(self.ui.buttonLista,QtCore.SIGNAL("clicked()"), self.pokazListe)
		QtCore.QObject.connect(self.ui.decodeButton,QtCore.SIGNAL("clicked()"), self.dekoduj)
		QtCore.QObject.connect(self.ui.buttonBledy,QtCore.SIGNAL("clicked()"), self.listaBledow)
			

######################################## Zakladka Hamminga ######################################
		
					
	def kodujHammingiem(self):
		self.kontrolka=1
		self.clearHam()
		self.info=str(self.ui.hammingInput.text())
		if self.blad(self.info)==0 or self.info=="": # jesli tego if'a nie bedzie to funkcja zakoduje mimo bledu
			return
		hamming=HammingEncoder(self.info)
		self.G=hamming.G
		self.H=hamming.H
		rozmiar=len(hamming.kod)-len(hamming.info)# liczba bitow parzystosci
		self.ui.kodHamminga.setText(hamming.kod)
		fonttemplate = QtCore.QString("<font color='#9999FF'><b>%1</b></font><font color='black'>%2</font>")
		self.ui.kodHamminga.setText(fonttemplate.arg(hamming.kod[0:rozmiar],hamming.kod[rozmiar:] ))
		
		
	def generatorHam(self):
		from gen_ui import Ui_Form
		oknogen = QtGui.QWidget()
		oknogen.ui = Ui_Form()
		oknogen.ui.setupUi(oknogen)
		oknogen.show()
		
		def hand(): #obrazuje zmiane wartosci na suwaku
			wartosc=oknogen.ui.suwak.value()
       			oknogen.ui.ile.setText(str(wartosc))
	        QtCore.QObject.connect(oknogen.ui.suwak,QtCore.SIGNAL("valueChanged(int)"), hand)
		
		def genera():
			a=oknogen.ui.suwak.value()
			from operacje import losuj
			losowy=losuj(a)
			self.ui.hammingInput.setText(losowy)
		QtCore.QObject.connect(oknogen.ui.pushOk,QtCore.SIGNAL("clicked()"), genera)

	def errorHam(self):
		from wprowadz_dzielnik import Ui_oknoDzielnik # to okno moze sluzyc rowniez do wektora bledu
		oknoWB = QtGui.QWidget() # okno wektora bledu
		oknoWB.ui = Ui_oknoDzielnik()
		oknoWB.ui.setupUi(oknoWB)
		oknoWB.setWindowTitle('Wektor bledu')
		oknoWB.show()
		oknoWB.ui.dzielnikInput.setFocus()
		oknoWB.ui.dzielnikInput.setText(self.wektorb)

		def ok():
			licznik = 0
			for i in oknoWB.ui.dzielnikInput.text():
				if i == "1":
					licznik=licznik+1
			if licznik == 0:
				message = QtGui.QMessageBox(self)
				message.setText('podano zerowy wektor bledu')
				message.setWindowTitle('Blad')
				message.exec_()
				
			from wektor_bledu import wektorBlad
			self.wektorb=str(oknoWB.ui.dzielnikInput.text())	
			if self.blad(self.wektorb)==0: 
				return
			else:
				kodzik=str(self.ui.kodHamminga.toPlainText())
				zmienony_kod=""
				if wektorBlad(kodzik,self.wektorb) == "blad" or kodzik=="":
					message = QtGui.QMessageBox(self)
					message.setText('Podano za dlugi wektor lub nie zakodowano informacji')
					message.setWindowTitle('Blad')
					message.exec_()
					return 0
				else:
					(self.wektorb,zmieniony_kod)=wektorBlad(kodzik,self.wektorb)
					self.ui.WektorBledu.setText(self.wektorb)
					self.ui.HammingWithError.setText(zmieniony_kod)
					oknoWB.close()
			
		QtCore.QObject.connect(oknoWB.ui.okButton,QtCore.SIGNAL("clicked()"), ok)
	
	def clearHam(self):
		self.ui.kodHamminga.setText("")
		self.ui.WektorBledu.setText("")
		self.ui.HammingWithError.setText("")
		self.ui.DetekcjaB.setText("")
		self.ui.Skorygowany.setText("")
		self.ui.syndrom.setText("")
		self.G=None
		self.H=None
	
	def detekcjaHam(self):
		"""licznik = 0
		for i in self.ui.WektorBledu.toPlainText():
			if i == "1":
				licznik=licznik+1
		if licznik == 0:
			message = QtGui.QMessageBox(self)
			message.setText('Podano zerowy wektor bledu.\nDetekcja nie ma sensu')
			message.setWindowTitle('Blad')
			message.exec_()
			return 0"""
		from det_kor import zliczacz
		if str(self.ui.WektorBledu.toPlainText())=="":
			message = QtGui.QMessageBox(self)
			message.setText('Nie podano bledu')
			message.setWindowTitle('Blad')
			message.exec_()
			return 0
		#if zliczacz(self.ui.WektorBledu.toPlainText())=="blad":
		#	mess = QtGui.QMessageBox(self)
		#	mess.setText('Detekcja niemozliwa(podano zbyt wiele bledow)')
		#	mess.setWindowTitle('Blad')
		#	mess.exec_()
		#	return 0
		from macierze import defaultMatrix
		(G,H)=defaultMatrix(str(self.ui.hammingInput.text()))
		from det_kor import detekcja
		(self.pozycjaBledu,self.syndrom)=detekcja(str(self.ui.HammingWithError.toPlainText()),G,H)
		self.syndrom=(stringer(self.syndrom))
		self.ui.syndrom.setText(self.syndrom)
		kod_blad=self.ui.HammingWithError.toPlainText()
		licznik=0
		for i in self.syndrom:
			if i=="1":
				licznik=licznik+1
		if licznik==0:
			self.ui.DetekcjaB.setText("brak bledu")
		else:
			#fonttemplate = QtCore.QString("<font color='black'>%1</font><font color='#FF9999'><b>%2</b></font><font color='black'>%3</font>")			
			self.ui.DetekcjaB.setText("blad wystapil, aby skorygowac kliknij przycisk 'korekcja'(jesli wiecej niz 1 blad korekcja bedzie bledna")
			
			#self.ui.DetekcjaB.setText(fonttemplate.arg(kod_blad[0:self.pozycjaBledu],kod_blad[self.pozycjaBledu],kod_blad[self.pozycjaBledu+1:] ))
		
	
	def korekcjaHam(self):
		if str(self.ui.DetekcjaB.toPlainText())=="" or str(self.ui.DetekcjaB.toPlainText())=="brak bledu" :
			message = QtGui.QMessageBox(self)
			message.setText('Nie wykonano detekcji lub blad nie wystapil')
			message.setWindowTitle('Blad')
			message.exec_()
			return 0
		from det_kor import korekcja
		self.ui.Skorygowany.setText(korekcja(str(self.ui.HammingWithError.toPlainText()),self.pozycjaBledu))
		tmp=self.ui.Skorygowany.toPlainText()
		fonttemplate = QtCore.QString("<font color='black'>%1</font><font color='#B2FF66'><b>%2</b></font><font color='black'>%3</font>")
		self.ui.Skorygowany.setText(fonttemplate.arg( tmp[0:self.pozycjaBledu],tmp[self.pozycjaBledu],tmp[self.pozycjaBledu+1:] ))
	
	def pokazG(self):
		if str(self.ui.kodHamminga.toPlainText())=="":
			message = QtGui.QMessageBox(self)
			message.setText('Nie zakodowano informacji')
			message.setWindowTitle('Blad')
			message.exec_()
			return 0
		from oknaMacierzy import oknoM
		ex = oknoM("G",self.G)
    		ex.show()
		def ok():
			ex.close()
		QtCore.QObject.connect(ex.zam,QtCore.SIGNAL("clicked()"), ok)

	def pokazH(self):
		#if str(self.ui.kodHamminga.toPlainText())=="":
		if self.H==None:
		
			message = QtGui.QMessageBox(self)
			message.setText('Nie zakodowano informacji')
			message.setWindowTitle('Blad')
			message.exec_()
			return 0
		from oknaMacierzy import oknoM
		ex = oknoM("H",self.H)
    		ex.show()
		def ok():
			ex.close()
		QtCore.QObject.connect(ex.zam,QtCore.SIGNAL("clicked()"), ok)
	
	def pokazSposob(self):
		if str(self.ui.DetekcjaB.toPlainText())=="" or self.kontrolka==0:
			message = QtGui.QMessageBox(self)
			message.setText('Nie wykonano detekcji dla funkcji kodowania')
			message.setWindowTitle('Blad')
			message.exec_()
			return 0
		from oknoSyndrom import oknoS
		ex = oknoS(self.H,self.syndrom,self.pozycjaBledu)
    		ex.show()
		def ok():
			ex.close()
		QtCore.QObject.connect(ex.zam,QtCore.SIGNAL("clicked()"), ok)

	def pokazListe(self):
		if str(self.ui.kodHamminga.toPlainText())=="":
			message = QtGui.QMessageBox(self)
			message.setText('Nie zakodowano informacji')
			message.setWindowTitle('Blad')
			message.exec_()
			return 0
		else:
			from lista import Ui_okno_lista
			oknoL = QtGui.QWidget() # okno wektora bledu
			oknoL.ui = Ui_okno_lista()
			oknoL.ui.setupUi(oknoL)
			oknoL.show()
			a=generuj_wszystkie(len(self.info))
			oknoL.ui.textBrowser.setText(a)
			def zamknij():
				oknoL.close()
			QtCore.QObject.connect(oknoL.ui.zamknijButton,QtCore.SIGNAL("clicked()"), zamknij)
			
	def dekoduj(self):
		self.kontrolka=0
		self.clearHam()
		kodzik=self.ui.dekodujInput.text()
		if self.blad(kodzik)==0 or kodzik=="": 
			return
		for i in xrange(10):
			if len(kodzik)==2**i:
				message = QtGui.QMessageBox(self)
				message.setText('Kod nie moze miec dlugosci 2^n')
				message.setWindowTitle('Blad')
				message.exec_()
				return 0
		(nr,syndrom,self.G,self.H)=dekoder(kodzik)
		syndrom=stringer(syndrom)
		self.ui.syndrom.setText(syndrom)
		licznik=0
		for i in syndrom: # licznik zer w syndromie
			if i=="1":
				licznik=licznik+1
		if nr=="brak" and licznik!=0:
			self.ui.DetekcjaB.setText("Wyliczony syndrom nie zawiera sie w macierzy H")
		elif licznik==0:
			self.ui.DetekcjaB.setText("Blad nie wystapil")
		else:
			fonttemplate = QtCore.QString("<font color='black'>%1</font><font color='#FF9999'><b>%2</b></font><font color='black'>%3</font>")
			self.ui.DetekcjaB.setText(fonttemplate.arg(kodzik[0:nr],kodzik[nr],kodzik[nr+1:] ))
			from det_kor import korekcja
			self.ui.Skorygowany.setText(korekcja(kodzik,nr))
			tmp=self.ui.Skorygowany.toPlainText()
			fonttemplate = QtCore.QString("<font color='black'>%1</font><font color='#B2FF66'><b>%2</b></font><font color='black'>%3</font>")
			self.ui.Skorygowany.setText(fonttemplate.arg(tmp[0:nr],tmp[nr],tmp[nr+1:] ))
		
	def listaBledow(self):
		if str(self.ui.kodHamminga.toPlainText())=="":
			message = QtGui.QMessageBox(self)
			message.setText('Nie zakodowano informacji')
			message.setWindowTitle('Blad')
			message.exec_()
			return 0
		from listaSyndrom import Ui_okno_lista
		oknoS = QtGui.QWidget() # okno wektora bledu
		oknoS.ui = Ui_okno_lista()
		oknoS.ui.setupUi(oknoS)
		oknoS.show()
		a=generuj_syndromy(self.H)
		oknoS.ui.textBrowser.setText(a)
		def zamknij():
			oknoS.close()
		QtCore.QObject.connect(oknoS.ui.zamknijButton,QtCore.SIGNAL("clicked()"), zamknij)
		

	def blad(self,st):
		for i in st: #poprawnosc wejscia
			if i !="1" and i !="0":
				message = QtGui.QMessageBox(self)
				message.setText('Zly format danych')
				message.setWindowTitle('Blad')
				message.exec_()
				return 0

#################################################################

if __name__ == "__main__":
	app = QtGui.QApplication(sys.argv)
   	myapp = StartQT4()
   	myapp.show()
   	sys.exit(app.exec_())





