from tkinter import*

X=Tk()
X.title("ADI")
X.geometry("500x600")
a=StringVar()
def calc(num):
    global n
    n=en1.get()
    n=n+str(num)
    a.set(n)

def eql():
    global result
    result=str(eval(n))
    a.set(result)

def clr():
    c=""
    a.set(c)
en1=Entry(X,bd=7,bg="skyblue",fg="purple",font=("bold",14),textvariable=a)
en1.pack(ipadx=11,ipady=8)

def back():
    count=len(n)
    for i in range(count):
        s=n.removesuffix(count-1)
        a.set(s)




bn=Button(X,text="AC",font=("bold",10),height=2,width=3,bg="orange",command=clr).place(relx=0.17,rely=0.2)
bn=Button(X,text="->",font=("bold"),height=2,width=3,bg="orange",command=back).place(relx=0.35,rely=0.2)
bn=Button(X,text="%",font=("bold"),height=2,width=3,bg="orange",command=lambda:calc("%")).place(relx=0.53,rely=0.2)
bn=Button(X,text="/",font=("bold"),height=2,width=3,bg="orange",command=lambda:calc("/")).place(relx=0.70,rely=0.2)

bn=Button(X,text="7",font=("bold,30"),foreground="black",bg="cyan",height=2,width=3,command=lambda:calc(7)).place(relx=0.17,rely=0.38)
bn=Button(X,text="8",font=("bold,30"),height=2,width=3,bg="cyan",command=lambda:calc(8)).place(relx=0.35,rely=0.38)
bn=Button(X,text="9",font=("bold,30"),height=2,width=3,bg="cyan",command=lambda:calc(9)).place(relx=0.53,rely=0.38)
bn=Button(X,text="X",font=("bold,30"),height=2,width=3,bg="orange",command=lambda:calc("*")).place(relx=0.70,rely=0.38)

bn=Button(X,text="4",font=("bold,30"),height=2,width=3,bg="cyan",command=lambda:calc(4)).place(relx=0.17,rely=0.55)
bn=Button(X,text="5",font=("bold,30"),height=2,width=3,bg="cyan",command=lambda:calc(5)).place(relx=0.35,rely=0.55)
bn=Button(X,text="6",font=("bold,30"),height=2,width=3,bg="cyan",command=lambda:calc(6)).place(relx=0.53,rely=0.55)
bn=Button(X,text="-",font=("bold,30"),height=2,width=3,bg="orange",command=lambda:calc("-")).place(relx=0.70,rely=0.55)

bn=Button(X,text="1",font=("bold,30"),height=2,width=3,bg="cyan",command=lambda:calc(1)).place(relx=0.17,rely=0.72)
bn=Button(X,text="2",font=("bold,30"),height=2,width=3,bg="cyan",command=lambda:calc(2)).place(relx=0.35,rely=0.72)
bn=Button(X,text="3",font=("bold,30"),height=2,width=3,bg="cyan",command=lambda:calc(3)).place(relx=0.53,rely=0.72)
bn=Button(X,text="+",font=("bold,30"),height=2,width=3,bg="orange",command=lambda:calc("+")).place(relx=0.70,rely=0.72)

bn=Button(X,text="+/-",font=("bold,30"),height=2,width=3,bg="green",fg="white",command=lambda:calc("+/-")).place(relx=0.17,rely=0.89)
bn=Button(X,text="0",font=("bold,30"),height=2,width=3,bg="green",fg="white",command=lambda:calc(0)).place(relx=0.35,rely=0.89)
bn=Button(X,text=".",font=("bold,300"),height=2,width=3,bg="green",fg="white",command=lambda:calc(".")).place(relx=0.53,rely=0.89)
bn=Button(X,text="=",font=("bold,30"),height=2,width=3,bg="green",fg="white",command=eql).place(relx=0.70,rely=0.89)






X.mainloop()