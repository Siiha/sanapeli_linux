import kysymykset as ksms
import tkinter,random,webbrowser
from functools import partial
pisteet=[]
color1 = "#AADAFF"
color2 = "#AADDFF"
def kehys():
	return tkinter.Frame(bg=color1)
def pohja():
	return tkinter.Tk()
def callback():
	webbrowser.open_new("https://www.paypal.com/paypalme/Siiha")
def seuraava():
	f = kehys()
	f.pack()
	viesti = tkinter.Label(f,text="Valitse haluamasi kysymys tyyppi.",bg=color2)
	viesti.pack()
	ekaVika = tkinter.Button(f,text="eka tai vika kirjain",command=eka_vika ,bg=color2)
	ekaVika.pack()
	pituus1 = tkinter.Button(f,text="Tietyn pituinen sana",command=pituus,bg=color2)
	pituus1.pack()
	tilanne = tkinter.Button(f,text="Pisteeni", command=pisteetf,bg=color2)
	tilanne.pack()
def tarkistus(x,y):
	f = kehys()
	f.pack()
	x = x.get()
	sulje=tkinter.Button(f,text="Sulje osio" , command=f.destroy,bg=color2)
	sulje.pack()
	if x in y[0]:
		v = True
		viesti = tkinter.Label(f,text=v,bg=color2)
	else:
		v = False
		viesti = tkinter.Label(f,text=v,bg=color2)
	pisteet.append(v)
	viesti.pack()
def eka_vika():
	f = kehys()
	f.pack()
	k1 = ksms.ekavika(ksms.k[random.randint(0,len(ksms.k)-1)],random.randint(0,1))
	viesti = tkinter.Label(f,text=k1[1],bg=color2)
	viesti.pack()
	syote = tkinter.Entry(f)
	syote.pack()
	valmis=tkinter.Button(f,text="valmis",command=partial(tarkistus,syote,k1),bg=color2)
	sulje=tkinter.Button(f,text="Sulje osio" , command=f.destroy,bg=color2)
	valmis.pack()
	sulje.pack()
	
def pituus():
	f = kehys()
	f.pack()
	k1 = ksms.pitka(random.randint(3,30))
	viesti = tkinter.Label(f,text=k1[1],bg=color2)
	viesti.pack()
	syote = tkinter.Entry(f,bg=color2)
	syote.pack()
	valmis=tkinter.Button(f,text="valmis",command=partial(tarkistus,syote,k1),bg=color2)
	valmis.pack()
	sulje=tkinter.Button(f,text="Sulje osio" , command=f.destroy,bg=color2)
	sulje.pack()
def pisteetf():
	f = kehys()
	f.pack()
	viesti = tkinter.Label(f,text=sum(pisteet),bg=color2)
	viesti.pack()
	nahty=tkinter.Button(f,text="nähty",command=f.destroy,bg=color2)
	nahty.pack()
