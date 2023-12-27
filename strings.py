strName="CHANDANA P"
strRoll="199H1A0460"
strAdress='''Gudipadu(v),
            Yadiki(M),
            Anantapur(D)-515 408'''
print(len(strName))
print(len(strRoll))
print(len(strAdress))
print(strName)
print(strRoll)
print(strAdress)
print(strName[0:3])#--->Forward slice(Startindex:Endindex-->it does not include)
print(strName[-10:-2])#-->Reverse slice(Endindex-->it includes:Startindex)
print(strName[::-1])#-->Reverse a string by using[::-1]


#Palindrome
strName="madam"
if(strName==strName[::-1]):
    print("is a  palindrome")
else:
    print("Is not a palindrome")

#String methods
#Upper
strmsg="vikas naidu"
print(strmsg.upper())
#Lower
strmsg="SANTHOSH"
print(strmsg.lower())
#isupper and islower
strmsg="sunthos"
print(strmsg.isupper())
print(strmsg.islower())
strmsg="SUNTHOS"
print(strmsg.isupper())
print(strmsg.islower())
#Capitalize
strmsg="nikhil"
print(strmsg.capitalize())#--->capitalize
print(strmsg.isalpha())#--->isalpha
name="abc123"
print(name.isalnum())#--->isalnum
print(name.isnumeric())#--->is numeric
print(name.isdecimal())#--->isdecimal


#Count
name="chandana"
name=name.count("c")
print("the repeated character of A is:",name)


#Index(positon)
name="Vikas naidu"
name=name.index("naidu")
print("The index of naidu is:",name)

#Find(index)
name="Pramodh naidu"
x=name.find("n")
print("The index of n is:",x)


#rfind
name="chandana"
x=name.rfind("dana")
print("the index of a is:",x)

#strip
name="   java full stack   "
print("The name with spaces:",name)
name=name.strip( )
print("The name without spaces:",name)

#lstrip
message= "   full   "

x = message.lstrip()

print("java", x, "stack")

#rstrip
message= "   full   "

x = message.rstrip()

print("java", x, "stack")
name="***chandana@@"#---->rstrip
print(name.rstrip("@"))

#Replace
name="i like travelling"
name=name.replace("travelling","apples")
print(name)
employeename="vikas naidu"
print(employeename)
value=employeename.replace("n","N")
print(value)

#split
msg="i, like watching,   movies"
msg=msg.split( )
print(msg)
value="122"
value=value.split( )
print(value)

#Join
friends=("chandu","vicky","vihitha","santhosh")
cousins="nikhil".join(friends)
print(cousins)


#Take any input string and saperate numbers,alphabets and specialcharacters
# input="chandanapotturu@12343"
# result= separate_characters(input)
# print("The characters are in input:",saperate_characters())
# Python 3 program to split an alphanumeric
# string using STL
def splitString(str):
    alpha = ""
    num = ""
    special = ""
    for i in range(len(str)):
        if (str[i].isdigit()):
            num = num + str[i]
        elif ((str[i] >= 'A' and str[i] <= 'Z') or
              (str[i] >= 'a' and str[i] <= 'z')):
            alpha += str[i]
        else:
            special += str[i]

    print(alpha)
    print(num)
    print(special)
if __name__ == "__main__":
    str = "chandanapotturu2002@@@@@!!!gmial.com"
    splitString(str)





