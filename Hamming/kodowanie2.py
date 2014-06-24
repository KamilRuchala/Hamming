
import numpy
from macierze import defaultMatrix
from macierze import jednostkowa
from operacje import *
from det_kor import *


sizeinf=0
sizepar=0

def encoder(inf):
	global sizeinf
	sizeinf=len(inf)
	

	(G,H)=defaultMatrix(inf)
	global sizepar
	sizepar=len(H)
	c=mnozenie(G,inf)
	kod=[]
	tmp=[]
	for x in xrange(len(H[1])):
		tmp=c[:,x]
		kod.append(suma(tmp))
	return (stringer(kod),G,H)	

def dekoder(kod):
	syndrom=""
	nr=None
	licznik=0
	potegi=1
	info="" # string po wyrzuceniu bitow parzystosci
	for i in xrange(len(kod)): # licze liczbe bitow parzystosci
		if i==potegi-1:
			licznik = licznik +1
			potegi=potegi*2
	info=kod[licznik:]
	(G,H)=defaultMatrix(info) # generuje macierze dla swojego kodu, szczegolnie interesuje mnie macierz 
	(nr,syndrom)=detekcja(kod,G,H)
	return (nr,syndrom,G,H)
	
	
def generuj_wszystkie(dlg): # funkcja generujaca wszystkie mozliwe kody dla okreslonej dlugosci informacji, zwraca gotowy string do gui, dzialam nastepujaco: licze jaka maksymalnie mozna zapisac binarna liczbe na tylu bitach ile mam dane, potem puszczam petelke do tej liczby i zamieniam na binarke. zostanie wtedy wykorzystany kazdy ciag 
	li=[] # lista pomocnicza zawierajace wszystkie ciagi danej dlugosci
	l_kombinacji= 2**dlg  # liczba kombinacji, inaczej mowiac jaka maks liczba moze byc zapisana na dlg bitach
	string="" # wyjsciowy string ktory trafi do gui
	for i in xrange(l_kombinacji):
		tmp= bin(i)
		tmp=tmp[2:]
		if len(tmp) < dlg: # uzupelnianie zerami zeby kazdy element mial taka sama dlugosc
			tmp1="" # korzystam z tmp1 zeby insertowac na poczatku zera
			for x in xrange(dlg-len(tmp)):
				tmp1=tmp1 +"0"
			tmp=tmp1+tmp
		li.append(tmp) # od 2 bo forma binarnej zmiennej to '0bxxxxx'
	for x in xrange(len(li)):
		tmp=str(li[x])
		(tmp1,a,b)=encoder(tmp)
		string=string+tmp+" -> "+tmp1+"\n"	
	return string

def generuj_syndromy(H):
	wyjscie="pozycja w kodzie -> odpowiadajacy syndrom\n\n"
	(m,n)=H.shape
	Ht=numpy.zeros(shape=(n,m))	# H transponowana
	for x in xrange(n):
		Ht[x,:]=H[:,x]	
	for i in xrange(n):
		if i<9:
			wyjscie=wyjscie+"             "+str(i+1)+"           ->        "+str(Ht[i,:])+"\n"
		else:
			wyjscie=wyjscie+"             "+str(i+1)+"         ->        "+str(Ht[i,:])+"\n"
	return wyjscie

