a={}
while 1:
    choice=input("enter a option: \n1.ADD \n2.UPDATE \n3.DELETE \n4.VIEW \n5.DISPLAY ALL\n")
    if choice==1:
        b={}
        name=input("enter a name:")
        email=[]
        count1=input("how many emails are added:")
        e=input("enter email")
        for i in range(count1):
            print(i)
            email.append(e)
        
        phone_no=[]
        count2=input("how many phone numbers are added:")
        p=input("enter a phone number:")
        for i in range(count2):
            print(i)
            phone_no.append(p)
        b["Name"]=name
        b["Email"]=email
        b["Phone_no"]=phone_no 
        a[b]=b  
    elif choice==2:
        u=input("which contact details are updated:")
        u1=input("which data to change:\n 1.Name 2.Email 3.Phone_no")
        if u1==1:
            name=input("enter a name:")
        elif u1==2:
            email=input("enter a email:")
        else:
            phone_no=input("enter a phone number")
    elif choice==3:
        d=input("which contact details deleted")
        del d
    elif choice==4:
        v=input("which contact details are displayed:")
        print(v)
    else:
        s=input("display all")
        print(a)


    





