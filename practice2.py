#If
# age=float(input("enter the age"))
# if(age>18):
#     print("Eligible for vote")
#If else
# marks=float(input("Enter the student marks"))
# if marks>=35:
#     print("The student will be passes")
# else:
#     print("The student will be failed")
#if elif else
# marks=float(input("Enter the student marks"))
# if marks ==35:
#     print("you are promoted")
# elif marks>35:
#     print("you pass the exam")
# else:
#     print("you fail the exam")
#nested if
# marks=float(input("Enter the student marks"))
# if marks == 35:
#     print("The student will be promoted:",marks)
# elif marks>35 and marks<=100:
#     print("the student will be pass!")
#     if marks >=75 and marks<=85:
#        print("The student got good marks:",marks)
#     elif marks > 85 and marks<=95:
#        print("great marks:", marks)
#     elif marks > 95 and marks<=100:
#         print("The are the best marks:", marks)
# else:
#     print("the student failed:",marks)

#LIST
#created by chandana p
#created on 29/12/23
#empty list
mylist=[]
print(mylist)
#covert to list
mylist=list()
print(mylist)
#Homogeneous list
mylist=["deva","chandana","arun"]
print(mylist)
#heterogenous list
mylist=list(("chandu",1,2,3,4,"true","bool",False))
print(mylist)
#nested list
mylist=["deva","chandu","arun",["frruits","vegetables"]]
print("access vegetables:",mylist[3][1])
print("the size of list:",len(mylist),type(mylist))
#replace
mylist=["deva","chandana","arun"]
mylist[2]="sreedhar"
print(mylist)
#apppend
mylist=["deva","chandu","arun",["frruits","vegetables"]]
mylist.append(["chandu,vikas"])
print(mylist)
#insert(adding in particular position)
mylist.insert(2,1)
print(mylist)
#pop
mylist=["deva","chandu","arun",["frruits","vegetables"]]
mylist.pop()
print(mylist)
mylist.pop(1)
print(mylist)
mylist.pop(-1)
print(mylist)
#index
mylist=["chandu","vikas","vihitha"]
mylist=mylist.index("chandu")
print(mylist)
mylist=["chandu","vikas","vihitha"]
del mylist[0:4]
print(mylist)





