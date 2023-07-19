def calc():
    x=int(input("enter your choice 1.add 2.subtract 3.multiply 4.divide 5.remainder\n"))
    a=int(input("enter a number"))
    b=int(input("enter a number"))
    
    if x==1:
        print(a+b)
    elif x==2:
        print(a-b)
    elif x==3:
        print(a*b)
    elif x==4:
        print(a/b)
    else:
        print(a%b)
calc()


