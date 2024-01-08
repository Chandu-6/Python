#Topic:Functions
#created on 06/01/24
#Created by chandana p
#Type 1(without input and without output)
def add(num1,num2):
    result=num1+num2
    print("result",result)
add(30,40)
def Add():
    num1=100
    num2=200
    result=num1+num2
    print("The result of num1 and num2 is:",result)
Add()
def myfunction(name="user"):
    print("My name is ",name)
myfunction("santhosh")
user_name="vikas"
myfunction(user_name)

myfunction("chandu")
myfunction("VIKAS")
myfunction("DEVA")
myfunction("NIKHIL")
#With input and without output
def sub(num1,num2):
    result=num1-num2
    print("with input and without output:",result)
sub(30,20)
#without input and with output
def mul():
    num1=20
    num2=30
    sum=num1*num2
    return sum
result=mul()
print("without input and with output:",result)
#with input and with output
def div():
    num1=30
    num2=5
    result=num1/num2
    return result
result=div()
print("with input and with output:",result)







