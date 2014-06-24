import numpy # trzeba doinstalowac 

def suma(wiersz):
	suma=0
	for i in xrange(len(wiersz)):
		suma=suma+wiersz[i]
	if suma %2 == 0:
		return 0
	else:
		return 1

def mnozenie(m1,inf): 
	inf2=[]
	for x in inf:
		tmp=int(x)
		inf2.append(tmp)
	l_k=len(m1[0]) # liczba kolumn
	l_w=len(m1) # liczba wierszy
	wynikowa=numpy.zeros(shape=(l_w,l_k)) #macierz wynikowa
	for x in xrange(l_w):
		for i in xrange(l_k):
			wynikowa[x,i]=m1[x,i]*inf2[x]
	return wynikowa

def mnozenie2(m1,inf): 
	inf2=[]
	for x in inf:
		tmp=int(x)
		inf2.append(tmp)
	l_k=len(m1[0]) # liczba kolumn
	l_w=len(m1) # liczba wierszy
	wynikowa=numpy.zeros(shape=(l_w,l_k)) #macierz wynikowa
	for x in xrange(l_w):
		for i in xrange(l_k):
			wynikowa[x,i]=m1[x,i]*inf2[i]
	return wynikowa

def stringer(tablica): # zmieniam tablice na string
	string=''.join(str(x) for x in tablica)
	return string

def inter(string):
	tab=[]
	for i in string:
		tab.append(int(i))
	return tab
	
def losuj(dlg):
	from random import randint
	ciag=""
	for i in xrange(dlg):
		ciag=ciag+str(randint(0,1))
	return ciag

def losujd(dlg):
	from random import randint
	ciag=""
	for i in xrange(dlg):
		ciag=ciag+str(randint(0,9))
	return ciag



	
