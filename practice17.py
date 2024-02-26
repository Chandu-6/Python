#Created  by Chandana
#Created on 26/02/24
#Dictionary
a={"name":"chandu","Place":"tadipatri","Age":21}
print("the data type is:",type(a),"\nThe adress is:",id(a))
print("The keys are:",a.keys())
print("the values are:",a.values())
print("The age is:",a.get("Age"))
print("The items present in dict are:",a.items())
a.update({"Qualification":"btech"})
print(a)
for i in {"name":"chandu","Place":"tadipatri","Age":21}:#By using for loop we can access only keys
    print(i)
for i in {"name":"chandu","Place":"tadipatri","Age":21}.values():#By using for loop we can access only values
    print(i)
for i,j in {"name":"chandu","Place":"tadipatri","Age":21}.items():#Here we can print both keys &values
    print(i,j)
#Set
c={1,3,4,0,5,4,1,0,7}
print("the data type is:",type(c))
print("The values presen in c is:",c)
c.add(66)
print("The updated set is:",c)
c.update({60,61})
print("The updated set is:",c)
c.pop()
print(c)
c.remove(66)
print(c)
set1={1,2,3,4,5,6,7}
set2={4,5,6,7,8,9,0}
print("The values are:",set1.union(set2))
print(set1.intersection(set2))
print(set1.issuperset(set2))
print(set1.issubset(set2))
#Pandas
import numpy as np
import pandas as pd
labels=['a','b','c']
d={'a':10,'b':20,'c':30}
mydata=[10,20,30]
c=pd.Series(data=mydata)
print(c)
c=pd.Series(mydata,labels)
print(c)
c=pd.Series(data=mydata,index=labels)
print(c)
d=pd.Series(d)
print(d)


