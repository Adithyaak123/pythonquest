string=input("enter a string\n")
revstring=""
count=len(string)
while count>0:
    revstring=revstring+string[count-1]
    count=count-1
if string==revstring:
    print(string,"is palindrome")
else:
    print(string,"is not palindrome")