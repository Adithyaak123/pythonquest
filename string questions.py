# 4.split a given string on hyphens into several substrings and display each substring given
# s=input("enter a string\n")
# a=s.split("-")
# for i in a:
#     print(i)

# 2.count all lower case,upper case,digits,and special symbols from a given string
# s=input("enter a string\n")
# alphabets=digits=symbol=0
# count=len(s)
# for i in range(count):
#     if(s[i].isalpha()):
#         alphabets=alphabets+1
#     elif(s[i].isdigit()):
#         digits=digits+1
#     else:
#         symbol=symbol+1
# print("alphabets=",alphabets)
# print("digits=",digits)
# print("symbols=",symbol)

#1.given 2 strings s1 and s2,return a new string made of the first,middle and last char each input string

# s1=input("enter a string\n")
# s2=input("enter a string\n")
# new_string=" "
# first_char=s1[0]+s2[0]
# middle_char=s1[int(len(s1)/2):int(len(s1)/2)+1]+s2[int(len(s2)/2):int(len(s2)/2)+1]
# last_char=s1[len(s1)-1]+s2[len(s2)-1]
# new_string=first_char+middle_char+last_char
# print("the new string is",new_string)

# 3.Given 2 strings s1 and s2,create a mixed string

# s1=input("enter a string:\n")
# s2=input("enter a string:\n")
# s3=" "
# for i in range(len(s1)):
#     s3+=s1[i]
#     s3+=s2[-i-1]
# print(s3)

# 6.write a python program to get a string made of the first 2 and the last 2 chars from a given string.if the string length is less than 2,return instead of the empty string.

# s=input("enter a string\n")
# if len(s)<2:
#     print()
# else:
#     print(s[0:2]+s[-2:])

#7.write a python program to get a string from a given string where all occurences of its first char have been changed to '$',except the first char itself.

# s=input("enter a string\n")
# print("given string,",s)
# char=s[0]
# s=s.replace(char,'$')
# s=char+s[1:]
# print("new string\n",s)

# 8.write a python program to add 'ing' at the end of a given string(length should be atleast 3).if the given string already ends with 'ing' then add 'ly' instead.if the string length of the given string is less than 3,leave it unchanged.

s=input("enter a string:\n ")
if len(s)<3:
    print(s)
elif s[-3:]=='ing':
    print(s+'ly')
else:
    print(s+'ing')
    









