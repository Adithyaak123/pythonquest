a=int(input("enter a number"))
if a>=0 and a<=9:
    print("one digited")
elif a>=10 and a<=99:
    print("two digied")
elif a>=100 and a<=999:
    print("three digited")
else:
    print("more than three digited")