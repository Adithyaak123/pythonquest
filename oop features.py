class Human:
    eyes=2
    legs=2
    def talking(self):
        print("hlo")
    def walking(self):
        print("hi")
# adithya=Human()
# print(adithya.eyes)
# print(adithya.legs)

# minnu=Human()
# print(minnu.eyes)
# print(minnu.legs)

# adithya.talking()
# adithya.walking()
# minnu.talking()
# minnu.walking()


# class new:
#     name="ammu"
# obj1=new()
# print(obj1.name)#ammu
# obj1.name="minnu"
# print(obj1.name)#minnu  ->here,updation possible

# obj2=new()
# print(obj2.name)
# del obj2.name

# class hlo():
#     def hai(self,name):
#         print("welcome",name)
# obj1=hlo()
# obj1.hai("ammu")
# obj2=hlo()
# obj2.hai("anu")

#constructor method
#when you use construction method ,you created object is automatically called.there no need to call seperate.

#non-parametrized constructor/default constructor
# class Cons():
#     def __init__(self):
#         print("constructor method")
#     def details(self):
#         print("welcome")
# one=Cons()
# one.details()

#parametrized constructor
# class New():
#     def __init__(self,name,age):
#         print("hai",name,age)
#         self.n=name
#         self.a=age
#     def details(self):
#         print(self.n,self.a)
# obj1=New("ammu",13)
# obj1.details()
# obj2=New("anu",47)
# obj2.details()

#addition of two numbers using 3 methods
#1.constructor method(passing arguments)
#2.2nd method(addition occur)
#3.3rd metho(print sum)

# class Sum():
#     def __init__(self,a,b):
#         self.a=a
#         self.b=b
#     def add(self):
#         self.c=self.a+self.b
#     def addition(self):
#         print(self.c)
# obj1=Sum(12,4)
# obj1.add()
# obj1.addition()
# obj2=Sum(5,3)
# obj2.add()
# obj2.addition()

#inheritance
#types of inheritance
# 1.single level inheritance

# example 1.use normal function in inheritance

# class parent():
#     def parentdetails(self):
#         print("parent details")
# class child(parent):
#     def childdetails(self):
#         print("child details")
# obj1=child()
# obj1.childdetails()
# obj1.parentdetails()

# example 2.use pass in inheriance

# class A:
#     a=10
#     def New(self):
#         print("welcome")
# class B(A):
#       pass #class B has no atributes and metods to pass here,so just "pass" use here.
# obj1=B()
# print(obj1.a)
# obj1.New()

# example 3.use constructor method in inheritance(constructor method used in one class)

# class person:
#     def __init__(self,name,age):
#         self.a=name
#         self.b=age
#     def New(self):
#         print(self.a,self.b)
# class Employee(person):
#     pass
# obj1=Employee("ammu",45)
# obj1.New()

# ->constructor method used in two class

# class student:
#     def __init__(self,name,age):
#         self.a=name
#         self.b=age
#     def New(self):
#         print(self.a,self.b)
# class student1(student):
#     def __init__(self,name,age):
#         print("hi")
#         # student.__init__(self,name,age)
#         super().__init__(name,age)
        
# obj1=student1("ammu",45)
# obj1.New()

# 2.multi-level inheritance

# class A:
#     def first(self):
#         print("first class")
# class B(A):
#     def second(self):
#         print("second class")
# class C(B):
#     def third(self):
#         print("third class")
# obj=C()
# obj.third()
# obj.second()
# obj.first()

# 3.multiple inheritance

# class parent1:
#     def first(self):
#         print("dg")
# class parent2:
#     def second(self):
#         print("odjk")
# class Child(parent1,parent2):
#     def third(self):
#         print("fggh")
# obj1=Child()
# obj1.third()
# obj1.second()
# obj1.first()

# 4.hierarchical inheritance

# class parent:
#     def parent(self):
#         print("parent")
# class child1(parent):
#     def first(self):
#         print("1st child")
# class child2(parent):
#     def second(self):
#         print("2nd child")
# class child3(parent):
#     def third(self):
#         print("third child")
# obj1=child1()
# obj1.first()
# obj1.parent()
# obj2=child2()
# obj2.second()
# obj2.parent()
# obj3=child3()
# obj3.third()
# obj3.parent()

# 5.hybrid inheritance

# class first:
#     def first(self):
#         print("1st class")
# class second(first):
#     def second(self):
#         print("2nd class")
# class  third(first):
#     def third(self):
#         print("third class")
# class fourth(third,second):
#     def fourth(self):
#         print("fourth class")
# obj1=fourth()
# obj1.fourth()
# obj1.third()
# obj1.second()
# obj1.first()

#encapsulation

#access specifiers/access modifiers

#1.public(default)
# 2.private
# 3.protected

# 1.public

# class A:
    #inside the class
#     a="hjk"
#     print(a)
# class B(A):
    #inside the derived class
    # print(A.a)
#outside the class
# obj=B()
# print(obj.a)

# 2.private

# class B:
#     __a=90 #__ used variable set as a private
    # print(__a)
# class C(B):
#     print(B.__a)
# obj=C()
# print(obj.__a)

# 3.protected

# class A:
#     _a="fdhh" #_(single underscore) used variable set as a protected
#     print(_a)
# class B(A):
#     print(A._a)
# obj1=B()
# print(obj1._a)

# class A:
    "this is docstring"
#     a=10
#     def normal(self):
#         print("hii")
# obj=A()
# print(obj.a)
# obj.normal()
# print(A.__doc__)
# print(A.__name__)
# print(A.__dict__)

#atribute methods

#1.getattr()
# class A:
#     c=34
#     b=23
# obj=A()
# print(getattr(obj,'c'))
# print(getattr(obj,'b'))

# 2.hasattr()
# class A:
#     c=34
#     b=23
# obj=A()
# print(hasattr(obj,'c'))
# print(hasattr(obj,'j'))

# 3.setattr()
# class A:
#     c=34
#     b=23
# obj=A()
# setattr(obj,'h',45)
# print(obj.h)

# 4.delattr()
# class A:
#     c=34
#     b=23
# obj=A()
# delattr(obj,'c')
# print(obj.c)

# Abstraction
# from abc import ABC,abstractmethod
# class first(ABC):
#     @abstractmethod
#     def empdetails(self):
#         print("hii")
#     def one(self):
#         print("welcome")
# class second(first):
#     def empdetails(self):
#         print("hjk")
# class Third(second):
#     def empdetails(self):
#         print("ok")
#     def normal(self):
#         print("ooi")
# obj=second()
# obj.empdetails()
# obj=Third()
# obj.empdetails()
# obj.normal()
# obj.one()

# polymorphism
#1.method overriding
# class A:
#     def normal(self):
#         print("hii")
# class B(A):
#     def normal(self):#one method can be override another method work
#         print("hlo")
# obj=B()
# obj.normal()

# 2.method overloading
#python do not support method overloading
# def g(a,b):
#     print(a+b)
# def p(a,b,c):
#     print(a+b+c)
# p(2,3)
# p(2,3,5)

#operator overloading
# 1.addition
# class A:
#     def __init__(self,a):
#         self.n=a
#     def __add__(self,g):
#         return self.n+g.n
# obj1=A(2)
# obj2=A(3)
# print(obj1+obj2)

#2.subtraction
# class A:
#     def __init__(self,a):
#         self.n=a
#     def __sub__(self,g):
#         return self.n-g.n
# obj1=A(2)
# obj2=A(3)
# print(obj1-obj2)

#3.multiplication
# class A:
#     def __init__(self,a):
#         self.n=a
#     def __mul__(self,g):
#         return self.n*g.n
# obj1=A(2)
# obj2=A(3)
# print(obj1*obj2)

#4.division
# class A:
#     def __init__(self,a):
#         self.n=a
#     def __truediv__(self,g):
#         return self.n/g.n
# obj1=A(6)
# obj2=A(3)
# print(obj1/obj2)

#5.power
# class A:
#     def __init__(self,a):
#         self.n=a
#     def __pow__(self,g):
#         return self.n**g.n
# obj1=A(2)
# obj2=A(3)
# print(obj1**obj2)

#6.less than
# class A:
#     def __init__(self,a):
#         self.n=a
#     def __lt__(self,g):
#         return self.n<g.n
# obj1=A(2)
# obj2=A(3)
# print(obj1<obj2)
# print(obj2<obj1)

#instance variable and instance method
# class A:
#     def __init__(self,a,b):
#         self.n=a
#         self.n=b
#     def avg(self):
#         print((self.n+self.n)/2)
# obj1=A(4,4)
# obj2=A(10,10)
# obj1.avg()
# obj2.avg()


#class variable 
# class A:
#     b="welcome"
#     def new(self):
#         print("hii")
# obj=A
# print(obj.b)
# obj1=A
# print(obj1.b)

#class method
# class A:
#     @classmethod
#     def new(cls):
#         print("hii")
# obj=A
# obj.new()

#static method
class A:
    @staticmethod
    def new():
        print("hii")
obj=A()
obj.new()















        


    


     


        