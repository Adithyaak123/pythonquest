#capitalize()
'''a="welcome"
b=a.capitalize()
print(b)'''
#count()
'''a="hello"
b=a.count("l")
print(b)'''
#startswith()
'''a="hello"
b=a.startswith("h")
print(b)'''
#index()
#a="hello"
#print(a.index("o))  o/p:4
'''print(a.index("m")) o/p:error'''
#find()
'''a="hello"
print(a.find("h"))'''#o/p:0
'''print(a.find("m"))'''#o/p:-1
#upper()
#a="good"
#b=a.upper()
#print(b)'''
#lower()
'''a="HELLO"
b=a.lower()
print(b)'''
#zfill()
'''a="hello"
b=a.zfill(8)
print(b)'''
#strip()
'''a= "        hello       "
print(a)
b=a.strip()
print(b)'''
#split()
'''a="hello good morning"
b=a.split("o")
print(b)'''
#rjust()
#a="hello"
#b=a.rjust(7) o/p:  hello
#print(b)
#b=a.rjust(7,'a')
#rint(b) o/p:aahello
#ljust()
'''a="hello"
b=a.ljust(10,'a')
print(b)'''
#replace()
'''a="hello good hello morning"
print(a.replace("hello","hai"))'''
#len()
'''a="hello"
print(len(a))'''
#casefold()
'''a="APPLE"
b=a.casefold()
print(b)'''
#center()
'''a="hello"
b=a.center(50)
print(b)'''
#isalnum()
#a="9good"
#b=a.isalnum() o/p:true
#print(b)
'''a="%"
b=a.isalnum()
print(b)'''
#isalpha()
'''a="hai"
b=a.isalpha()
print(b)
'''
#isnumeric()
'''a="30"
b=a.isnumeric()
print(b)'''
#isdigit()
'''a="10"
b=a.isdigit()
print(b)
'''
#islower()
'''a="hello"
b=a.islower()
print(b)'''
#isupper()
'''a="APPLE"
b=a.isupper()
print(b)'''
'''a="Good Morning"
b=a.istitle()
print(b)'''
#swapcase()
'''a="hello"
b=a.swapcase()
print(b)'''
#isdecimal()
'''a="10"
b=a.isdecimal()
print(b)'''
#isidentifier()
'''a="APPLE"
b=a.isidentifier()
print(b)'''
#isspace()
'''a="  3  "
b=a.isspace()
print(b)'''
#endswith()
'''a="hello"
print(a.endswith("k"))'''
#formatting
#default formatting
'''a="apple is {} and {}".format("red","round")
print(a)'''
#positional formatting
'''a="apple is {1} and {0}".format("red","round")
print(a)'''
#keyword formatting
'''a="apple is {k} and {l}".format(l="round",k="red")
print(a)'''
#escape sequences
'''a="hello \"goodmorning\""
print(a)'''
#/n->new line
'''a="hello\nworld"
print(a)'''
#\t->tab space
'''a="hello\tworld"
print(a)'''
#\b->backspace
'''a="hello \bworld"
print(a)'''
'''a="hello"
print("o" in a)'''
'''a="hello"
for loop
for i in a:
    print(i)'''
#while loop
'''a="hello"
i=0
while i<len(a):
    print(a[i])
    i+=1'''