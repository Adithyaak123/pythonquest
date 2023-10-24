from tkinter import*
from tkinter.scrolledtext import ScrolledText
from tkinter.ttk import Combobox
from tkinter import messagebox
X=Tk()
X.title("ADI")
X.geometry("400x400")

lb1=Label(X,text="Name:",font="arial",fg="Blue").grid(row=0,column=0)
en1=Entry(X,bd=7,bg="violet").grid(row=0,column=1)

lb1=Label(X,text="Age:",font="arial",fg="blue").grid(row=1,column=0)
sp=Spinbox(X,from_=1,to=50,width=20,bg="yellow",bd=7).grid(row=1,column=1)

lb1=Label(X,text="Address:",font="arial",fg="blue").grid(row=2,column=0)
scr=ScrolledText(X,width=15,height=2,bg="skyblue",bd=7).grid(row=2,column=1)

lb1=Label(X,text="Email:",font="arial",fg="blue").grid(row=3,column=0)
en1=Entry(X,bd=7,bg="purple").grid(row=3,column=1)

first=IntVar()
lb1=Label(X,text="Gender:",font="arial",fg="blue").grid(row=4,column=0)
r1=Radiobutton(X,text="Male",variable=first,value=1,width=15,bd=5,fg="red").grid(row=4,column=1)
r1=Radiobutton(X,text="Female",variable=first,value=2,width=15,fg="red").grid(row=4,column=2)

lb1=Label(X,text="Languages:",font="arial",fg="blue").grid(row=5,column=0)
c1=Checkbutton(X,text="English",fg="green").grid(row=5,column=1)
c1=Checkbutton(X,text="Malayalam",fg="green").grid(row=5,column=2)
c1=Checkbutton(X,text="Hindi",fg="green").grid(row=5,column=3)
c1=Checkbutton(X,text="Tamil",fg="green").grid(row=5,column=4)


lb1=Label(X,text="Collage Name:",font="arial",fg="blue").grid(row=6,column=0)
cm=Combobox(X,foreground="purple")
cm["value"]=("RSM SNDP COLLEGE,KOYILANDY","ILAHIYA COLLEGE,KOYILANDY","SREE GOKULAM COLLEGE,BALUSSERY")
cm.current(0)
cm.grid(row=6,column=1)

lb1=Label(X,text="Phone number:",font="arial",fg="blue").grid(row=7,column=0)
en1=Entry(X,bd=7,bg="green").grid(row=7,column=1)

def click():
    messagebox.showinfo("info","you have registered")
b1=Button(X,text="Register",command=click,bg="dark orange",font=("bold,30")).place(x=150,y=280)

X.mainloop()