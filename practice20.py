#Created by chandana p
#Created on 28/03/24
name="Chandana"
result=name[::-1]
print(name)
print(result)
#Comparision operators
a=20
b=40
print(a==b)
a=20
b=20
print(a==b)
a=10
b=20
print(a!=b)
a=10
b=10
print(a!=b)
name="chandana"
if(name==name[::-1]):
    print("The given string is a palindrome")
else:
    print("The given string is not palindrome")
#String methods
Name="chandana"
print(Name.upper())
print(Name.lower())
print(Name.isupper())
print(Name.islower())
print(Name.isnumeric())
print(Name.isdigit())
print(Name.isalpha())
print(Name.isnumeric())
print(Name.isdecimal())
print(Name.isascii())
print(Name.isidentifier())
print(Name.capitalize())
print(Name.index("a"))
print(Name.count("a"))
print(Name.replace("ana","u"))
print(Name.find("a"))#It gives position of a given letter or num
print(Name.rfind("a"))
print(Name.split())
Name="     Chandana    "
print(Name.strip())
print(Name.lstrip())
print(Name)
print(Name.rstrip())
Friends=("Sathvi","Pooji","Nani")
print("Akhila".join(Friends))
import  numpy as np
arr = np.array([10, 15, 20, 25, 30, 35, 40])
print(arr[0:4])