import sqlite3,random,sys,itertools
con = sqlite3.connect('data.db')

cur = con.cursor()
def ekavika(x,ar):
	if ar == 0:
		v = [i[0] for i in cur.execute("SELECT sana FROM sanat where sana like ?",(x+"%",))]
		s="Sana jonka ensimmäinen kirjain on "+x
	else:
		v = [i[0] for i in cur.execute("SELECT sana FROM sanat where sana like ?",("%"+x,))]
		s="Sana jonka viimeinen kirjain on "+x
	return v,s


def pitka(x):
	v = [i[0] for i in cur.execute("SELECT sana FROM sanat where len >= ?",(str(x),))]
	s="Sana joka on vähintään "+str(x)+" merkkiä pitkä"
	return v,s
def sisaltaa(x):
	v = [i[0] for i in cur.execute("SELECT sana FROM sanat where sana like ?",("%"+x+"%",))]
	s = "Sana joka sisältää kirjainyhdistelmän "+x
	return v,s
def sanoja(x):
	v = [i[0] for i in cur.execute("Select sana from sanat where sanoja >= ?",(str(x),))]
	s = "Sana joka sisältää vähintään "+str(x)+" sanaa"
	return v,s
k = "a, b, c, d, e, f, g, h, i, j, k, l, m, n, o, p, q, r, s, t, u, v, w, x, y, z, å, ä".replace(", ","")
yh=["".join(i) for i in itertools.product(k,repeat=2)]+[i*2 for i in k]
def loppu(n,p):
	cur.execute("Insert into pelit(pelaaja,pisteet) values(?,?)",(str(n),str(p),))
	con.commit()
def aiemmat():
	return [(i[0],i[1]) for i in cur.execute("SELECT * FROM pelit ORDER by pisteet DESC Limit 10")]
	
