#a=1
#print(b)
#Error handling
#Created on 18/01/24
#Created by chandana
# try:
#     print("b")#risky code
# except:
#     print("error")
# else:
#     print("no error")
# finally:
#     print("always")
# #Indentation error
# try:
# print("My name is chandana")
# except:
# print("Indentation error")
#synatx error
# try:
#     print(20+30):
# except SyntaxError:
#     print("sytax error")
#Type error
try:
  print("a"+22)
except TypeError:
    print("type error")
except ValueError:
    print("Value error")
#Value error
try:
    num1=int(input("enter a number"))
    num2=int(input("enter a number"))
    num=num1+num2
    print("The sum of two numbers is:",num)
except ValueError:
    print("value error")
except TypeError:
    print("type error")
# a=int(input("enter a number"))
# b=int(input("enter a number"))
#Name error

