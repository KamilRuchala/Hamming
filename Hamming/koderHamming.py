import sys
sys.path.insert(0, '../')

from koder import koder
from kodowanie2 import *

class HammingEncoder(koder):
	G=None
	H=None
	def __init__(self,informacja):
		self.info=informacja
		self.kod="None"
		self.opis="zastosowano koder Hamminga"
		self.koduj()
	def koduj(self):
		(self.kod,self.G,self.H)=encoder(self.info)


