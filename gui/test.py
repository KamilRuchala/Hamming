def dekoder(kod):
	licznik=0
	potegi=1
	info="" # string po wyrzuceniu bitow parzystosci
	for i in xrange(len(kod)):
		if i==potegi-1:
			licznik = licznik +1
			potegi=potegi*2
	print licznik

dekoder("11111111")
