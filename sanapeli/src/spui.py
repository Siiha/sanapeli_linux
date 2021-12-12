import kysymykset as ksms
import tkinter,random,webbrowser
from functools import partial
pisteet=[]
def pohja():
	return tkinter.Tk()
def callback():
	webbrowser.open_new("https://www.paypal.com/paypalme/Siiha")
def seuraava():
	f = tkinter.Frame()
	f.pack()
	viesti = tkinter.Label(f,text="Valitse haluamasi kysymys tyyppi.")
	viesti.pack()
	ekaVika = tkinter.Button(f,text="eka tai vika kirjain",command=eka_vika )
	ekaVika.pack()
	pituus1 = tkinter.Button(f,text="Tietyn pituinen sana",command=pituus)
	pituus1.pack()
	tilanne = tkinter.Button(f,text="Pisteeni", command=pisteetf)
	tilanne.pack()
def tarkistus(x,y):
	f = tkinter.Frame()
	f.pack()
	x = x.get()
	sulje=tkinter.Button(f,text="Sulje osio" , command=f.destroy)
	sulje.pack()
	if x in y[0]:
		v = True
		viesti = tkinter.Label(f,text=v)
	else:
		v = False
		viesti = tkinter.Label(f,text=v)
	pisteet.append(v)
	viesti.pack()
def eka_vika():
	f = tkinter.Frame()
	f.pack()
	k1 = ksms.ekavika(ksms.k[random.randint(0,len(ksms.k)-1)],random.randint(0,1))
	viesti = tkinter.Label(f,text=k1[1])
	viesti.pack()
	syote = tkinter.Entry(f)
	syote.pack()
	valmis=tkinter.Button(f,text="valmis",command=partial(tarkistus,syote,k1))
	sulje=tkinter.Button(f,text="Sulje osio" , command=f.destroy)
	valmis.pack()
	sulje.pack()
	
def pituus():
	f = tkinter.Frame()
	f.pack()
	k1 = ksms.pitka(random.randint(3,30))
	viesti = tkinter.Label(f,text=k1[1])
	viesti.pack()
	syote = tkinter.Entry(f,)
	syote.pack()
	valmis=tkinter.Button(f,text="valmis",command=partial(tarkistus,syote,k1))
	valmis.pack()
	sulje=tkinter.Button(f,text="Sulje osio" , command=f.destroy)
	sulje.pack()
def pisteetf():
	f = tkinter.Frame()
	f.pack()
	viesti = tkinter.Label(f,text=sum(pisteet))
	viesti.pack()
	nahty=tkinter.Button(f,text="nähty",command=f.destroy)
	nahty.pack()
