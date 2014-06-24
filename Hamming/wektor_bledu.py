def zmieniacz(kodzik,blad):
	kodzik2=""
	for i in xrange(len(kodzik)):
		if blad[i] == '1' and kodzik[i]=='0': 
			kodzik2=kodzik2+"1"	
		elif blad[i] == '1' and kodzik[i]=='1': 
			kodzik2=kodzik2+"0"
		else:
			kodzik2=kodzik2+kodzik[i]	
	return kodzik2
def wektorBlad(kod,wektorb):
	sizeK=len(kod)
	sizeW=len(wektorb)
	sizeWp=len(wektorb) # rozmiar wyjsciowy bledu
	if sizeW >sizeK:
		return "blad"
	elif sizeW < sizeK:
		while sizeW < sizeK: # takie combo bo wyjsciowy wektorb traktowany jest caly jako jeden element(np "101"traktowane jak jedno)
			arr = wektorb.split() # bo insert nie dziala w string
			arr.insert(sizeW,'0')
			wektorb="".join(arr)
			sizeW=len(wektorb)
	
	kod=zmieniacz(kod,wektorb)
	return (wektorb,kod)
