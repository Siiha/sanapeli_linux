import kysymykset as ksms
import tkinter,random,webbrowser
from functools import partial
pisteet=[]
sanat = []
color1 = "#AADFFF"
color2 = "#AADDFF"
color3 = "#AAFBFF"
w = 50
p = False
def kehys():
	return tkinter.Frame(bg=color1)
def pohja():
	return tkinter.Tk()
def callback():
	webbrowser.open_new("https://www.paypal.com/donate/?hosted_button_id=KC5GC9TWEQ3F6")
def seuraava():
	f = kehys()
	f.pack()
	viesti = tkinter.Label(f,text="Valitse haluamasi kysymys tyyppi.",bg=color2)
	viesti.pack()
	ekaVika = tkinter.Button(f,text="eka tai vika kirjain",command=lambda:[eka_vika(),f.destroy()] ,bg=color2,width=w)
	ekaVika.pack()
	pituus1 = tkinter.Button(f,text="Tietyn pituinen sana",command=lambda:[pituus(),f.destroy()],bg=color2,width=w)
	pituus1.pack()
	EkaVikaPituus=tkinter.Button(f,text="Tietyn pituinen sana sekä alku- tai loppukirjain",command=lambda:[eka_vika_pituus(),f.destroy()],bg=color2,width=w)
	EkaVikaPituus.pack()
	Sisaltyy=tkinter.Button(f,text="Sisältää tietyn kirjain yhdistelmän",command=lambda:[sisaltyy(),f.destroy()],bg=color2,width=w)
	Sisaltyy.pack()
	Sisaltyy_pituiseen = tkinter.Button(f,text="Tietyn pituinen sana joka sisältää tietyn kirjain yhdistelmän",command=lambda:[sisaltyy_pituiseen(),f.destroy()],bg=color2,width=w)
	Sisaltyy_pituiseen.pack()
	SANOJA = tkinter.Button(f,text="Tietyn määrä sanoja sisältävä sana (myös oikealta vasemmalle)",command=lambda:[Sanoja(),f.destroy()],bg=color2,width=w)
	SANOJA.pack()
	
	p = True
def tarkistus(x,y):
	f = kehys()
	f.pack()
	x = x.get()
	sulje=tkinter.Button(f,text="Sulje osio" , command=lambda:[f.destroy(),seuraava()],bg=color2)
	sulje.pack()
	if x in y[0] and x not in sanat:
		v = True
		viesti = tkinter.Label(f,text=v,bg=color2)
		sanat.append(x)
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
	valmis=tkinter.Button(f,text="valmis",command=lambda:[tarkistus(syote,k1),f.destroy()],bg=color2)
	#sulje=tkinter.Button(f,text="Sulje osio" , command=f.destroy,bg=color2)
	valmis.pack()
	#sulje.pack()
	
def pituus():
	f = kehys()
	f.pack()
	k1 = ksms.pitka(random.randint(3,30))
	viesti = tkinter.Label(f,text=k1[1],bg=color2)
	viesti.pack()
	syote = tkinter.Entry(f,bg=color2)
	syote.pack()
	valmis=tkinter.Button(f,text="valmis",command=lambda:[tarkistus(syote,k1),f.destroy()],bg=color2)
	valmis.pack()
	#sulje=tkinter.Button(f,text="Sulje osio" , command=f.destroy,bg=color2)
	#sulje.pack()
def eka_vika_pituus():
	f = kehys()
	f.pack()
	k1 = ksms.pitka(random.randint(3,30))
	k2 = ksms.ekavika(ksms.k[random.randint(0,len(ksms.k)-1)],random.randint(0,1))
	k3 = []
	k3.append(list(set(k1[0]).intersection(k2[0])))
	viesti = tkinter.Label(f,text=k1[1]+"\n"+k2[1],bg=color2)
	viesti.pack()
	syote = tkinter.Entry(f,bg=color2)
	syote.pack()
	valmis=tkinter.Button(f,text="valmis",command=lambda:[tarkistus(syote,k3),f.destroy()],bg=color2)
	valmis.pack()
	#sulje=tkinter.Button(f,text="Sulje osio" , command=f.destroy,bg=color2)
	#sulje.pack()
def sisaltyy():
	f = kehys()
	f.pack()
	k1 = ksms.sisaltaa(ksms.yh[random.randint(0,len(ksms.yh))])
	viesti = tkinter.Label(f,text=k1[1],bg=color2)
	viesti.pack()
	syote = tkinter.Entry(f,bg=color2)
	syote.pack()
	valmis=tkinter.Button(f,text="valmis",command=lambda:[tarkistus(syote,k1),f.destroy()],bg=color2)
	valmis.pack()
def sisaltyy_pituiseen():
	f = kehys()
	f.pack()
	k1 = ksms.sisaltaa(ksms.yh[random.randint(0,len(ksms.yh))])
	k2 = ksms.pitka(random.randint(4,30))
	k3 = []
	k3.append(list(set(k1[0]).intersection(k2[0])))
	viesti = tkinter.Label(f,text=k1[1]+"\n"+k2[1],bg=color2)
	viesti.pack()
	syote = tkinter.Entry(f,bg=color2)
	syote.pack()
	valmis=tkinter.Button(f,text="valmis",command=lambda:[tarkistus(syote,k3),f.destroy()],bg=color2)
	valmis.pack()
def Sanoja():
	f=kehys()
	f.pack()
	k1 = ksms.sanoja(random.randint(3,20))
	viesti = tkinter.Label(f,text=k1[1],bg=color2)
	viesti.pack()
	syote = tkinter.Entry(f,bg=color2)
	syote.pack()
	valmis=tkinter.Button(f,text="valmis",command=lambda:[tarkistus(syote,k1),f.destroy()],bg=color2)
	valmis.pack()
def pisteetf():
	f = kehys()
	f.pack()
	viesti = tkinter.Label(f,text=sum(pisteet),bg=color2)
	viesti.pack()
	nahty=tkinter.Button(f,text="nähty",command=f.destroy,bg=color2)
	nahty.pack()
def tallenna():
	f = kehys()
	f.pack()
	t = tkinter.Label(f,text="anna nimesi",bg=color2)
	t.pack()
	n = tkinter.Entry(f,bg=color2)
	n.pack()
	valmis = tkinter.Button(f,text="valmis",command=lambda:[ksms.loppu(n.get(),sum(pisteet)),f.destroy()])
	valmis.pack()
	
def aiemmat():
	f = kehys()
	f.pack()
	l = [tkinter.Label(f,text=i,bg=color2) for i in ksms.aiemmat()]
	for i in l:
		i.pack()
	nahty=tkinter.Button(f,text="nähty",command=f.destroy,bg=color2)
	nahty.pack()
