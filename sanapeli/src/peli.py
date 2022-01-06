import random,tkinter,sys,os,getpass,spui
if os.getcwd() != "/home/"+getpass.getuser()+"/sanapeli/src":
	os.chdir('/home/'+getpass.getuser()+'/sanapeli/src')
base = spui.pohja()
base.geometry("600x300")
base.configure(bg=spui.color1)
base.title("Sanapeli")
tippi = tkinter.Button(text="Tippi(paypall)",command=spui.callback,bg=spui.color2)
tippi.pack(side="left", anchor="nw")
spui.seuraava()
base.mainloop()
