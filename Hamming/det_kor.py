import numpy # trzeba doinstalowac 
from operacje import *

def detekcja(kod,G,H):
	kod2=kod
	size=len(kod)
	Ht=numpy.zeros(shape=(size,len(H)))	# H transponowana
	for x in xrange(len(H)):
		Ht[:,x]=H[x,:]
	a=mnozenie2(H,kod2)
	syndrom=[] # syndrom
	for x in xrange(len(H)):
		tmp=a[x,:]
		syndrom.append(suma(tmp)) 
	syndrom1=numpy.zeros(shape=(1,len(H))) # zmieniam na numpy do porownywania z kolumnami macierzy H 
	for i in xrange(len(H)):
		syndrom1[0,i]=syndrom[i]
	for x in xrange(size):
		if (syndrom1[0,:]==Ht[x,:]).all():
			return (x,syndrom) # zwraca numer przeklamanego indeksu i syndrom
	return ("brak",syndrom)
	

def korekcja(kod,syndrom):
	kodzik=inter(kod)
	if kodzik[syndrom]==1:
		kodzik[syndrom]=0
	else:
		kodzik[syndrom]=1
	return stringer(kodzik)

def zliczacz(strin):
	licznik=0
	for i in strin:
		if i=="1":
			licznik=licznik+1
			if licznik > 1:
				return "blad"
	
