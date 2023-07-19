string=input("enter the string:")
rev_string=string[::-1]
print("reversed string:",rev_string)
if string==rev_string:
    print("the string is palindrome")
else:
    print("the string is not palindrome")
