a=int(input("enter a number"))
rev=0
temp=a
while temp>0:
    rem=temp%10
    rev=rev*10+rem
    temp=temp//10
if a==rev:
        print("it is palindrome")
else:
        print("it is not palindrome")