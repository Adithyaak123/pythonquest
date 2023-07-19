a=int(input("enter a number"))
if a%2==0:
    if a%5==0:
        print("the number is divisible by 2 and 5")
    else:
        print("the number is not divisible by 5")
else:
    print("the number is not divisible by 2 and 5")
