import random,tkinter,sys,os,getpass,spui
os.chdir('/home/'+getpass.getuser()+'/sanapeli/src')
base = spui.pohja()
base.geometry("400x250")
base.title("Sanapeli")
seuraava = tkinter.Button(base, text="seuraava",command=spui.seuraava)
seuraava.pack()

base.mainloop()
