import kysymykset as ksms
import tkinter,random
from functools import partial
def seuraava():
	viesti = tkinter.Label(text="Valitse haluamasi kysymys tyyppi.")
	viesti.pack()
	ekaVika = tkinter.Button(text="eka tai vika kirjain",command=eka_vika )
	ekaVika.pack()
	pituus1 = tkinter.Button(text="Tietyn pituinen sana",command=pituus)
	pituus1.pack()
def tarkistus(x,y):
	x = x.get()
	if x in y[0]:
		viesti = tkinter.Label(text="Oikein!")
	else:
		viesti = tkinter.Label(text="Väärin!")
	viesti.pack()
def eka_vika():
	k1 = ksms.ekavika(ksms.k[random.randint(0,len(ksms.k)-1)],random.randint(0,1))
	viesti = tkinter.Label(text=k1[1])
	viesti.pack()
	syote = tkinter.Entry()
	syote.pack()
	valmis=tkinter.Button(text="valmis",command=partial(tarkistus,syote,k1))
	valmis.pack()
	
	
 
def pituus():
	k1 = ksms.pitka(random.randint(3,30))
	viesti = tkinter.Label(text=k1[1])
	viesti.pack()
	syote = tkinter.Entry()
	syote.pack()
	valmis=tkinter.Button(text="valmis",command=partial(tarkistus,syote,k1))
	valmis.pack()
	
