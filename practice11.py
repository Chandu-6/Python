#Single inheritance
class Bank:
    def fun1(self,Name,Type,Age,Branch):
        self.Name=Name
        self.Type=Type
        self.Age=Age
        self.Branch=Branch
        print("Name:",Name)
        print("Type:",Type)
        print("Age:",Age)
        print("Branch:",Branch)
class Privatebank(Bank):
    def fun2(self,Gender):
        self.Gender=Gender
        print("Gender:",Gender)
obj=Privatebank()
obj.fun2("Female")
obj.fun1("Chandana","Savingsaccount",21,"Madhapur")
print("-----------")
#Multilevel inheritance
class Bank:
    def fun1(self,Name,Type,Age,Branch):
        self.Name=Name
        self.Type=Type
        self.Age=Age
        self.Branch=Branch
        print("Name:",Name)
        print("Type:",Type)
        print("Age:",Age)
        print("Branch:",Branch)
class Privatebank(Bank):
    def fun2(self,Gender):
        self.Gender=Gender
        print("Gender:",Gender)
class Publicbank(Privatebank,Bank):
    def fun3(self,Nationality,Limit):
        self.Nationality=Nationality
        self.Limit=Limit
        print("Nationality:",Nationality)
        print("Limit:",Limit)
obj=Publicbank()
obj.fun3("Indian",100)
obj.fun2("Female")
obj.fun1("Chandana","Savingsaccount",21,"Madhapur")
print("-------------")
#Multiple inheritance
class Father:
    def fun1(self,gold,Money,Land):
        self.gold=gold
        self.Money=Money
        self.Land=Land
        print("Gold:",gold)
        print("Money:",Money)
        print("Land:",Land)
class Mother:
    def fun2(self,Building):
        self.Building=Building
        print("Building:",Building)
class Child(Father,Mother):
    def fun3(self,Newflat):
        self.Newflat=Newflat
        print("Newflat:",Newflat)
obj=Child()
obj.fun3("2bhk")
obj.fun2("1bhk")
obj.fun1(20,"20laksh","10ac")
#Hybrid inheritance
list1=[1,2,"c",4,5]
list2=list1
# list2[2] = 7
print("list2:",list2,id(list2))
print("list1:",list1,id(list1))
#
b=10
a=b
a=5
print(a)
print(b)
#shallow copy
list1=[1,2,3,4]
list2=list1.copy()
print(list1,id(list1))
print(list2,id(list2))
# list2[2]=5
# print(list2,id(list2))
# print(list1,id(list1))
#Default constructor
# class Chandu:
#     def __init__(self):
#         self.A=100
#         self.B=300
# obj=Chandu()
# print("Addition=",(A+B))

#Parameter constructor
class Sum:
    def __init__(self,x,y):#------>formal arguments
        self.a=x
        self.b=y
        print("Addition=", a + b)
obj=Sum(10,10)#----->Actual arguments















