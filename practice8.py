def sayhello():
    print("good morning")
    print("Python full stack")
sayhello()
def sayhello(name="user"):
    print("good morning",name)
    print("Python full stack")
sayhello("chandu")
#Add
def add(fn,sn):
    result=fn+sn
    print("The sum of two numbers:",result)
add(20,30)

#Example
def name(name,age,country="india"):#----->Formal arguments
    print("Name:",name)
    print("Age:",age)
    print("I am from",country)
name("chandu",21)
name(21,"chandu")
name(age=21,name="chandu")#---->Actual arguments
name("sreedhar",22)
#Add multiple numbers by using *x
def getsum(*x):
    result=0
    for a in x:
        result+=a
    print("result:",result)
    print(x[::-1])
getsum(6,3,5,6,7)


def getsum(*nums):
    result=0
    value=88
    for a in nums:
        result+=a
    return result,value
getsum,z=getsum(3,5,6,7)
print(getsum,z)
#Example(*)
def person(*data):
    print(data)
person("chandu","potturu",21,630514)
#Arbitary keyword arguments(**)--->It gives output in dictionary format
def person(**data):
    print(data)
    for k,v in data.items():
        if k==fname
        print(k, ':', v)
person(fname="potturu",lname="chandana",age=21,mobileno=630514)
