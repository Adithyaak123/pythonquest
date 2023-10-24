
a={}
class phone_book:
    def add_contact(self,name="",email=[],phone_no=[]):
        b={}
        self.name=name
        name=input("enter a name")

        email=[]
        count1=int(input("Enter number of emails:"))
        for i in range(count1):
            e=input("enter email:")
            email.append(e)

        phone_no=[]
        count2=int(input("Enter number of phone no:"))
        for i in range(count2):
            p=int(input("enter a phone number:"))
            phone_no.append(p)

        b["Name"]=name
        b["Email"]=email
        b["Phone_no"]=phone_no 
        a[name]=b
        print("contact added")
        # print(b)
    def update_contact(self,name="",email=[],phone_no=[]):
        name=input("whose details are updated")
        update=int(input("""Enter your choice:
              1.Name
              2.Email
              3.phone no"""))
        if update==1:
          nm=input("enter a name")
          a[name].update({"Name":nm})
          print("name updated")
        elif update==2:
            e=input("enter a email")
            a[email].update({"email":e})
            print("email updated")
        elif update==3:
            ph=int(input("enter phone number"))
            a[phone_no].update({"Phone_no":ph})
            print("phone number updated")
        else:
            print("invalid choice")

    def delete_contact(self,name="",email=[],phone_no=[]):
        name=input("whose details deleted")
        del a[name]
        print("contact deleted")

    def view_contact(self,name="",email=[],phone_no=[]):
        name=input("whose details displayed")
        print(a[name])
    def view_all(self,name="",email=[],phone_no=[]):
        print("Full contact details in phone book are\n",a)
    
    def delete_email_or_phone_no(self,name="",email=[],phone_no=[]):
        name=input("whose email and phone number are deleted")
        choice=int(input("1.delete email \n2.Delete phone no\n"))
        if choice==1:
            del a[name]["Email"]
            print("email deleted")
        elif choice==2:
            del a[name]["Phone_no"]
            print("phone number deleted")
        else:
            print("inavalid choice")
    

while 1:
    print("""
          1.add contact
          2.update contact
          3.delete contact
          4.view contact
          5.view all
          6.Delete email or phone number""")
    ch=int(input("enter your choice\n"))
    if ch==1:
       obj=phone_book()
       obj.add_contact()
    elif ch==2:
        obj=phone_book()
        obj.update_contact()
    elif ch==3:
        obj=phone_book()
        obj.delete_contact()
    elif ch==4:
        obj=phone_book()
        obj.view_contact()
    elif ch==5:
        obj=phone_book()
        obj.view_all()
    elif ch==6:
        obj=phone_book()
        obj.delete_email_or_phone_no()
    else:
        print("invalid choice")

exit()
        
            

        
    



