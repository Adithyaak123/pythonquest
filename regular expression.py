import re
# built in methods
# 1.search()

# text="hello how are you"
# x=re.search("w",text)
# print(x)

# 2.findall()

# text="hello how are you"
# f=re.findall('h',text)
# print(f)

# 3.split()

# text="hello how are you"
# g=re.split("h",text)
# print(g)

# 4.sub()

# text="hello how are you"
# h=re.sub("how","baby",text)
# print(h)

# meta characters

# 1.[]: to print datas in a given range

# text="hello how are you"
# c=re.findall("[l-y]",text)
# print(c)

# 2./d :to display all digits in a string

# text="hello how 90are you"
# t="hello how are you"
#x=re.findall("\d",text)
# f=re.findall("\d",t)
#print(x)
# print(f)

# 3. dot symbol(.)

g="good morning"
# f=re.findall("m..n",g)
# print(f)
# v=re.findall("g.(7)n",g)
# print(v)

# 4. ^ :to check the string starts in given letter
# g="good morning ammu"
# r=re.findall("^g",g)
# print(r)

# 5. $ :to check the string ends in given letter
# p="good morning anu"
# j=re.findall("anu$",p)
# print(j)

# 6. * :to display the given character involved in string,othrwise returns empty list
# p="good morning anu"
# f=re.findall("nn*",p)
# print(f)

# 7. + :
# p="good morning anu"
# g=re.findall("an+",p)
# print(g)

# 8.|(straight slash)

# p="good morning anu"
# f=re.findall("b|j",p) #returns empty list
# b=re.findall("g|m",p) #displays g,m
# n=re.findall("o|c",p) #displays 'o' only
# print(f)
# print(b)
# print(n)

#special sequences
p="good morning %6&09anu"

# 1.\A: to check the string starts in given character

# f=re.findall("\Ay",p) #returns empty list
# g=re.findall("\Ag",p) #returns starting character 'g'
# print(g)
# print(f)

# 2.\Z :to check the string ends in given character

#f=re.findall("r\Z",p) #returns empty list
#j=re.findall("u\Z",p)  #returns ending character 'u'
# print(f)
# print(j)

# 3.\b: to check words starts in given character in a string

# c=re.findall("j\B",p) 
# v=re.findall("go\B",p)
# print(v)
# print(c)

# 4.\D:to display all datas,except digits from a string

# c=re.findall('\D',p)
# print(c)

# 5.\s:it returns spaces from given string

# v=re.findall('\s',p)
# print(v)

# 6.\S:it returns all datas,except spaces in a string

# v=re.findall('\S',p)
# print(v)

# 7.\w:it returns all letters and digits from a string
# v=re.findall('\w',p)
# print(v)

# 8.\W:it returns spaces,special chracters

# v=re.findall('\W',p)
# print(v)

# 9.set-[]

d=re.findall("[a-n]",p)
print(d)