#Created by chandana
#created on 07/02/24
#polymorphism wkth addition
a=2
b=3
print(a+b)
a="vikas"
b="Naidu"
print(a+b)
a="60"
b=60
c=a+str(b)
print(c)
#Method overloading
class Moverload:
    def fun1(self, a=None,b=None):
     print(a,b)
obj=Moverload()
obj.fun1()
obj.fun1(10)
obj.fun1(10,20)
#Method overriding



