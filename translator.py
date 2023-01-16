from googletrans import Translator,LANGUAGES
from tkinter import *
from tkinter import ttk
def transla(text="type",src="English",dest="Japanese"):
    text1=text
    src1=src
    dest1=dest
    t=Translator()
    t1=t.translate(text,dest=dest1,src=src1)
    return t1.text
def data():
    o=comb1.get()
    k=comb2.get()
    msg=source.get(1.0,END)    
    tget=transla(text=msg,src=o,dest=k)
    dest.delete(1.0,END)
    dest.insert(END,tget)





obj=Tk()
obj.title("This Is A Translator")
#for size
obj.geometry("500x700")
#for background
obj.config(bg="Blue")
#for label
ltext=Label(obj,text="Translator",font=("Open Sans",40,"bold"),bg="Blue")
ltext.place(x=10,y=50,height=60,width=450)
#for frame
frame=Frame(obj).pack(side=BOTTOM)
rtext=Label(obj,text="Main Text",font=("Open Sans",20,"bold"),bg="Blue")
rtext.place(x=10,y=100,height=60,width=400)
source=Text(frame,font=("Open Sans",18,"bold"),wrap=WORD)
source.place(x=10,y=150,height=100,width=480)
listext=list(LANGUAGES.values())
#comboboxes
comb1=ttk.Combobox(frame,value=listext)
comb1.place(x=10,y=270,height=60,width=100)
comb1.set("english")
button=Button(frame,text="Translate",relief=RAISED,command=data)
button.place(x=140,y=270,height=60,width=100)
comb2=ttk.Combobox(frame,value=listext)
comb2.place(x=270,y=270,height=60,width=100)
comb2.set("english")
dtext=Label(obj,text="Output Text",font=("Open Sans",20,"bold"),bg="Blue")
dtext.place(x=10,y=350,height=30,width=400)
dest=Text(frame,font=("Open Sans",18,"bold"),wrap=WORD)
dest.place(x=10,y=400,height=100,width=480)
obj.mainloop()