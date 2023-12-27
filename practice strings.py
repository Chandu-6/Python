strmsg="chandana"
print(strmsg.upper())
strmsg="CHANDANA"
print(strmsg.lower())
print(strmsg.capitalize())
print(strmsg.isnumeric())
print(strmsg.count("@"))
print(strmsg.find("A"))
print(strmsg.rfind("D"))
print(strmsg.find("N"))
strmsg="   CHANDANA VIKAS VIHITHA    "
print(strmsg)
print(strmsg.strip(" "))
print(strmsg.rstrip(" "))
print(strmsg.lstrip(" "))
message="i like reading books"
print(message.replace("reading books","apples"))
print(message.split())
#find If numbers are odd or even
a=1444
if(a%2==0):
    print("The given number is even")
else:
    print("The given number is a odd")

#print even numbers
for numItr in range(2,50,2):
    print("This is even number:",numItr)
#print odd numbers
for numItr in range(1,51,2):
    print("This is even number:",numItr)
#find vowels in the name(Forward direction)
employeeName=input("enter the employee name:")
print("The data stored in employeeName:",employeeName)
count=1
for strItr in employeeName:
    print("The vowel character in",count," iteration is:")
    if(strItr.upper()=="A" or strItr.upper()=="E" or strItr.upper()=="I" or strItr.upper()=="O" or strItr.upper()=="U"):
        print("The vowel found and it is at position",count,"and the vowel:",strItr)
    count += 1
 #Reverse direction
    # employeeName = input("enter the employee name:")
    # print("The data stored in employeeName:", employeeName)
    # count =1
    # for strItr in employeeName:
    #         print("The vowel character in", count, " iteration is:")
    #         if (
    #                 strItr.upper() == "U" or strItr.upper() == "O" or strItr.upper() == "I" or strItr.upper() == "E" or strItr.upper() == "A"):
    #             print("The vowel found and it is at position", count, "and the vowel:", strItr)
    #             count -= 1
#Reverse vowels



