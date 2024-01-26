#Created by chandana
#Shallow copy and deep copy
#created on 26/01/24
#list
mylist1=[1,2,3,4,5,6]
mylist2=mylist1
print("Mylist1 items are:",mylist1)
print("Mylist2 items are:",mylist2)
# mylist2=[7,8,9,0]
# print("mylist2 after assigning:",mylist2)
# print("Mylist1 after assigning new values for mylist2:",mylist1)
mylist2.append(7)
print("mylist2 after appending:",mylist2)
print("mylist1 after appending mylist2:",mylist1)
mylist3=list(mylist2)
print("mylist3 items are:",mylist3)
mylist3.append(8)
del mylist3[0]
print("after deleting item 0 is:",mylist3)
print("mylist3 after appending:",mylist3)
print(mylist2)
print(mylist1)
#Tuple
mytuple=(1,2,3,4,5)
mylist=mytuple
print("mylist items are:",mylist)
print("mytuple items are:",mytuple)
mylist=(6,7,8,9,0)
print("mylist after assigning values:",mylist)
print("mytuple after assigning new values for mylist:",mytuple)
mylist1=list(mylist)
print("mylist1 items are:",mylist1)

#set
myset={1,2,3,4,5}
mylist=myset
print("The items in myset are:",myset)
print("the items in mylist are :",mylist)
myset.add(8)
print("myset after adding:",myset)
myset1=list(mylist)
print("the items in myset are:",myset1)
print("mylist are:",mylist)
#Dictionary
#shallowcopy
myset1={"key1":"value1","key2":"value2"}
myset2=myset1
print("myset1 items are:",myset1)
print("myset2 items are:",myset2)
myset2.update({"key3":"value3"})
print("The updated mylist2 is:",myset2)
print("myset1 after updating of myset2 is:",myset1)
#deep copy
myset3=list(myset2)
print(myset3)
print(myset2)
print(myset1)
#Super
class Parent:
    def fun1(self):
     print("This is parent class1")
     print("This is parent class2")
class Child(Parent):
    def fun1(self):
        print("This is child class1 ")
        print("This is child class2 ")
        print("This is child class3 ")
        super().fun1()
Child_obj=Child()
Child_obj.fun1()
# Child_obj.fun1()
class parentclass:
    def parent_method(self):
        print("This is parent class")
class childclass(parentclass):
    def parent_method(self):
        super().parent_method()
    def child_method(self):
        print("This is child class")
        super().parent_method()
child_obj=childclass()
child_obj.child_method()
# child_obj.parent_method()
#Interface
class Chandu:
    name ="abc"
    Age = 18
    DOB = "10-Jan-2024"
    def __init__(self,name,Age,DOB):
        self.name=name
        self.Age=Age
        self.DOB=DOB
    def display(self):
        pass
obj=Chandu("Chandu",21,"03/07/2002")
obj.display()
class deva:
    Qualification="Btech"
    Percentage=70
    def __init__(self,Qualificaton,Percentage):
        self.Qualification=Qualificaton
        self.Percentage=Percentage

    def display(self):
        pass
obj=deva("btech",70)
obj.display()





