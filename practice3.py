# myList=["chandana",1,"60",["vikas",2,"70"]]
# myList.append(["nikhil",3,"50"])
# print(myList)
# list=myList[0][1]
# print("The roll no is:",list)

#Task
#Created by chandana
#created on 30/12/23
# stulist=list()
# record=list()
# bool=("Y","y")
# while(True):
#     baddlist=input("Enter yes to add No to exit YES/yes")
#     if baddlist == Y or Y:
#         stuName=input("enter a student name")
#         record.append(stuName)
#         rollNo=input("enter a roll no")
#         record.append(rollNo)
#         marks=input("enter student marks")
#         record.append(marks)
#     else:
#         print("student enrolled completed")
#         break
#         stuName = input("enter a student name")
#         record.append(stuName)
#         rollNo = input("enter a roll no")
#         record.append(rollNo)
#         marks = input("enter student marks")
#         record.append(marks)
# Initialize an empty list to store student information
# students = []
#
# # Use a while loop to continue adding students until the user decides to stop
# while True:
#     # Get input from the user
#     name = input("Enter student name (or 'exit' to stop): ")
#
#     # Check if the user wants to exit the loop
#     if name.lower() == 'exit':
#         break
#
#     # Get other details from the user
#     roll_no = input("Enter student roll number: ")
#     marks = float(input("Enter student marks: "))
#
#     # Create a tuple to represent the student information
#     student_info = (name, roll_no, marks)
#
#     # Add the student information to the list
#     students.append(student_info)
#
# # Display the list of students
# print("\nList of Students:")
# for student in students:
#     print(f"Name: {student[0]}, Roll No: {student[1]}, Marks: {student[2]}")
#
#


# stulist = []
# while True:
#     add_list = input("Enter 'yes' to add a student or 'no' to exit: ")
#     if add_list.lower() == 'yes':
#         record = []
#
#         stu_name = input("Enter student name: ")
#         record.append(stu_name)
#
#         roll_no = input("Enter roll number: ")
#         record.append(roll_no)
#
#         marks = input("Enter student marks: ")
#         record.append(marks)
#
#         stulist.append(record)
#     elif add_list.lower() == 'no':
#         print("Student enrollment completed.")
#         break
#     else:
#         print("Invalid input. Please enter 'yes' or 'no'.")
# for student in stulist:
#     # print(f"Name: {student[0]}, Roll No: {student[1]}, Marks: {student[2]}")
#     print("\nList of Students as :")
#     # for student in stulist:
#     print(stulist)
#list.append(value)--->
#list.insert
#Tuple
#tuple is immutable
#mytuple=()----empty tuple
#mytuple=tuple()----empty tuple
# mytuple=("a","b","c","d","e","f","g","h")
# mytuple=tuple([1,2,3,4,5])
# mytuple()
# count
# index()
#set
#{}---unordered---no indexing-----no duplicates
#sets are preffred for numbers
# myset1={}
# print(myset1)
# myset2=set()
# print(myset2)
# myset3={11,23,13,40,53,64,37,28}
# print(myset3)
# myset4=set([1,2,3,4,5,6,])
# print(myset4)
# myset5=set((1,2,3,4,5,6,7,8,9))
# print(myset5)
# myset6=set({1,2,3,4,5,6})
# print(myset6)
# myset7=set({1,2,3,4,5,6,2,3})
# print(myset7)
# add
# pop---removes first element
# remove----remove particular given element
# discard--if it exist it removes does not through error
# clear
# update
#Created on 4/01/24
myset={1,2,3,4,5,6,7,8}
meset1={"chandu","vicky","deva"}
# myset.add()
#myset.remove(value)---->through error when the value is not present in list or tuple
#myset.discard(value)---->It does not through error .it removes given value from the list
#myset.update()-->
#myset.pop()--->it removes first element in set
#myset.union(myset1)-->add the lsit items to the myset
#myset.intersection()
#myset.difference()---a-b
#myset.difference(myset3)---->removes common element in both sets--->a-b
#myset.symmetric_difference_update(myset2)--->
#myset.isdisjoint(myset2)--->it shows the common elements in both sets otherwise it through error
#myset.clear()--->it clear all elements
#myset.issuperset()--->the set B values present in A set
#myset.issubset()--->the set A values present in B set











