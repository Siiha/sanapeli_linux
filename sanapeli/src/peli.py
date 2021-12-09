import kysymykset as ksms
import random,tkinter,sys,os,getpass
os.chdir('/home/'+getpass.getuser()+'/sanapeli/src')
for i in range(int(input("kuinka monta kysymystä haluat: "))):
	ks = ksms.ekavika(ksms.k[random.randint(0,len(ksms.k)-1)],random.randint(0,1))
	print(ks[1])
	print(input("Anna sana: ") in ks[0])
