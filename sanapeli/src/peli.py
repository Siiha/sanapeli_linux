import random,tkinter,sys,os,getpass,spui
os.chdir('/home/'+getpass.getuser()+'/sanapeli/src')
base = tkinter.Tk()
base.title("Sanapeli")
seuraava = tkinter.Button(base, text="seuraava",command=spui.seuraava)
seuraava.pack()
base.mainloop()
