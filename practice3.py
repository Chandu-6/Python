# Comparison operators
# Created by Chandana p
# Created on 22/12/23

#==
a=10
b=20
result= a==b
print("The result is:",result)
a=10
b=10
result= a==b
print("The result is:",result)

#!=
a=10
b=20
result=a!=b
print("The result is:",result)
a=10
b=10
result=a!=b
print("The result is:",result)
#>
a=20
b=10
result=a>b
print("The result is:",result)
result=b>a
print("The result is:",result)
#<
a=20
b=10
result=b<a
print("The result is:",result)
result=a<b
print("The result is:",result)

#>=
a=10
b=13
result= a>=b
print("The result is:",result)
#<=
a=13
b=12
result=a<=b
print("The result is:",result)


#LOgical operators
#And
a=5
print(a<7 and a>10)#(True False)
b=10
print(b>=10 and b<11)#(True True)
c=15
print(c<14 and c<16)#(False True)
d=20
print(d<10 and d>19)#(True True)

#OR
a=5
print(a<7 or a>10)#(True False)
b=10
print(b>=10 or b<11)#(True True)
c=15
print(c<14 or c<16)#(False True)
d=20
print(d<10 or d>=22)#(True True)

#Not
x=5
print(not(x>3 and x<6))#(True True)

#Membership operators
stringmsg="Chandana"
print("The character c is in stringmsg:",'C'in stringmsg)
print("The character a is in stringmsg:",'v'not in stringmsg)
print("The character a is in stringmsg:",'v'in stringmsg)


#Conditional statements
#IF
a=10
b=20
if a<b:
    print("yes")
#If else
a=50
b=60
if(a>b):
    print("A is grater than b")
else:
    print("Ais less than b")

#If elif
a=30
b=50
if(a>b):
    print("Ais grater than B")
elif(a<b):
    print("A is less than B")
    







