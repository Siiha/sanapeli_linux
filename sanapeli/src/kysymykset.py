import sqlite3,random,os,sys
os.chdir("sanapeli/src")
con = sqlite3.connect('data.db')

cur = con.cursor()
def ekavika(x,ar):
	if ar == 0:
		v = [i[0] for i in cur.execute("SELECT sana FROM sanat where sana like '"+str(x)+"%'")]
		s="Sana jonka ensimmäinen kirjain on "+x
	else:
		v = [i[0] for i in cur.execute("SELECT sana FROM sanat where sana like '%"+ str(x)+"'")]
		s="Sana jonka viimeinen kirjain on "+x
	return v,s


def pitka(x):
	v = [i[0] for i in cur.execute("SELECT sana FROM sanat where len >= "+str(x))]
	s="Sana joka on vähintään "+str(x)+" merkkiä pitkä"
	return v,s
k = "a, b, c, d, e, f, g, h, i, j, k, l, m, n, o, p, q, r, s, t, u, v, w, x, y, z, å, ä".replace(", ","")
