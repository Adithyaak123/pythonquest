from tkinter import*
from tkinter import messagebox
from tkinter.ttk import Progressbar
x=Tk()
x.title("ADI")
x.geometry("400x400")
# label
lb1=Label(x,text="Username:",font="arial",bg="green").grid(row=0,column=0)
#textbox
en1=Entry(x,bd=3).grid(row=0,column=1)
lb1=Label(x,text="password:",font="arial",bg="skyblue").grid(row=1,column=0)
en1=Entry(x,bd=3,show="*").grid(row=1,column=1)

def click():
    print("hii")
    lb1.configure(text="clicked")
    messagebox
    messagebox.showerror("Error","login failed")
    messagebox.showinfo("info","login successful")
    messagebox.showwarning("warning","login warning")
    # button
b1=Button(x,text="Login",font="arialbold",bg="orange",command=click).grid(row=2,column=1)
#progressbar
pr=Progressbar(x,length=500)
pr['value']=50
pr.grid(row=10,column=0)
evar=StringVar()
mvar=StringVar()
def setmsg():
     mvar.set(evar.get())
en=Entry(x,textvariable=evar,bd=7,bg="skyblue",fg="black",font="Arial").grid(row=13,column=13)
b1=Button(x,text="click",command=setmsg,bg="orange",height=3,width=5,font="arial").grid(row=18,column=13)
m=Message(x,textvariable=mvar).grid(row=18,column=13)

menu1=Menu(x)
new=Menu(menu1,tearoff=False)
menu1.add_cascade(label="file",menu=new)
new.add_command(label="new text file")
new.add_command(label="new file")
new.add_command(label="new window")
new.add_separator()
new.add_command(label="open file")
new.add_command(label="open folder")
new.add_separator()
new.add_command(label="exit",command=x.quit)
editmenu=Menu(menu1,tearoff=False)
menu1.add_cascade(label="edit",menu=editmenu)
editmenu.add_command(label="undo")
editmenu.add_command(label="redo")
editmenu.add_separator()
editmenu.add_command(label="cut")
editmenu.add_command(label="copy")
editmenu.add_command(label="paste")
editmenu.add_separator()
editmenu.add_command(label="find")
editmenu.add_command(label="replace")
x.configure(menu=menu1)

x.mainloop()