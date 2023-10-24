from tkinter import*
import re
from tkinter import messagebox
X=Tk()
X.title("valid form")
X.geometry("400x400")

s1=StringVar()
s2=StringVar()
s3=StringVar()
s4=StringVar()

def validation():
    a=en1.get()
    v=re.search("[A-Z]+[\s]+[A-Z]+[\s+[A-Z]",a)
    if v:
        messagebox.showinfo("your name is",v)
    else:
        messagebox.showerror("name is invalid")
    

    b=en2.get()
    t=re.search("[a-z 0-9]+[\._]?[@][a-z]+[\.][a-z]{2,3}",b)
    if t:
        messagebox.showinfo("email is valid")
    else:
        messagebox.showerror("email is invalid")


    c=en3.get()
    p=re.search('[0|91]?[\s]?[6-9]?[0-9]{9}',c)
    if p:
        messagebox.showinfo("phone_no","phone number is valid")
    else:
        messagebox.showerror("ph_no","phone number is invalid")
        

    d=en4.get()
    if (len(d)<8):
        messagebox.showerror("password must be 8 character long")
    elif len(d)>20:
        messagebox.showerror("the size of password should not be greater than 20")
    elif not re.search('[A-Z]',d):
        messagebox.showerror("not valid!,password must contain atleast 1 uppercase letter")
    elif not re.search('[a-z]',d):
        messagebox.showerror("not valid!,password must contain atleast 1 lowercase letter")
    elif not re.search('[0-9]',d):
        messagebox.showerror("not valid!,password must contain atleast 1 digit")
    elif re.search('\s',d):
        messagebox.showerror("not valid!,password should not contain white space")
    elif not re.search("[!@#%&*_+=$]",d):
        messagebox.showerror("not valid!,password must contain atleast one special character")
    else:
        messagebox.showinfo("password is valid")


    e=en5.get()
    if  e==d:
        messagebox.showinfo("password confirmed")
    else:
        messagebox.showerror("password doesn't match")

lb=Label(X,text="Name").grid(row=0,column=0)
en1=Entry(X,textvariable=s1)
en1.grid(row=0,column=1)

lb=Label(X,text="Email").grid(row=1,column=0)
en2=Entry(X,textvariable=s2)
en2.grid(row=1,column=1)

lb=Label(X,text="phone no").grid(row=2,column=0)
en3=Entry(X,textvariable=s3)
en3.grid(row=2,column=1)

lb=Label(X,text="pasword").grid(row=3,column=0)
en4=Entry(X,bd=3,show="*")
en4.grid(row=3,column=1)

lb=Label(X,text="confirm pasword").grid(row=4,column=0)
en5=Entry(X,bd=3,show="*")
en5.grid(row=4,column=1)

bn=Button(X,text="submit",command=validation).grid(row=20,column=1)




X.mainloop()
