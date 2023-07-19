#read a file
# f=open("function.py")
# print(f.read())
# f.close()
# f=open("function.py",'r'):to use 'r' mode on read a file
# print(f.read(5))
# f.close()
# print(f.readline())
# print(f.readline())

#write a file:to use append mode 'a' to append a content at the end of a file
# f=open("function.py",'a')
# f.write("\nhello")
# f.close()

# f=open("function.py",'w')
# f.write("welcome")

# f=open("a.py",'w')
# f.write("elk")

#create a file using x mode
# f=open("ak.py",'x')
# f.close()


#rename file 
#rename method is included in os library,so first import os library
# import os
# os.rename("a.py","b.py")

#remove a file 
#remove method is included in os library,so first import os library
# import os
# os.remove("b.py")

#remove a empty file
import os
os.rmdir("ak.py")

