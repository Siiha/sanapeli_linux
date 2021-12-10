import kysymykset as ksms
import tkinter,random,webbrowser
from functools import partial
def pohja():
	return tkinter.Tk()
def callback():
	webbrowser.open_new("https://www.paypal.com/paypalme/Siiha")
def seuraava():
	base = pohja()
	viesti = tkinter.Label(base,text="Valitse haluamasi kysymys tyyppi.")
	viesti.pack()
	ekaVika = tkinter.Button(base,text="eka tai vika kirjain",command=eka_vika )
	ekaVika.pack()
	pituus1 = tkinter.Button(base,text="Tietyn pituinen sana",command=pituus)
	pituus1.pack()
def tarkistus(x,y):
	base = pohja()
	x = x.get()
	if x in y[0]:
		viesti = tkinter.Label(base,text="Oikein!")
	else:
		viesti = tkinter.Label(base,text="Väärin!")
	viesti.pack()
def eka_vika():
	base = pohja()
	k1 = ksms.ekavika(ksms.k[random.randint(0,len(ksms.k)-1)],random.randint(0,1))
	viesti = tkinter.Label(base,text=k1[1])
	viesti.pack()
	syote = tkinter.Entry(base)
	syote.pack()
	valmis=tkinter.Button(base,text="valmis",command=partial(tarkistus,syote,k1))
	valmis.pack()
	
	
 
def pituus():
	base = pohja()
	k1 = ksms.pitka(random.randint(3,30))
	viesti = tkinter.Label(base,text=k1[1])
	viesti.pack()
	syote = tkinter.Entry(base)
	syote.pack()
	valmis=tkinter.Button(base,text="valmis",command=partial(tarkistus,syote,k1))
	valmis.pack()
	
