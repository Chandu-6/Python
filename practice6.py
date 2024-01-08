#Created by chandana p
#Created on 05/01/24
#Set
myset1={1,2,3,4,5}
myset2={6,7,8,9}
myset=myset1.union(myset2)
print(myset)
# #Intersection
myset1={1,2,3,4,5,6}
myset2={7,3,4,2,1,4,5,6}
myset=myset1.intersection(myset2)
print(myset)
# #Difference
myset1={1,2,3,4,5,6}
myset2={2,3,4,5,6,7,8,9}
myset=myset2.difference(myset1)
print(myset)
#Symmetric

#Dictonary
#{}----set item is single datatype
#{}----dict item is pair of key and value(can be different data type)
#Dictnary keys are unique
#Dictionary values are no need to unique
#mydict=dict()
# mydict={(key1:value1),(key2:value2)......(keyn:valuen)}
# mydict.keys()=[key1,key2....keyn]
# mydict.values()=[valu1....valuen]
# mydict.items()=[key1:value1]
emptydict={}
emptyDict=dict()
print("empty dict is:",emptydict)
myDict={"fruits":10,"vegetables":12,"flowers":20}
print("The keys present in myDict:",myDict.keys())
print("The values present in myDict:",myDict.values())
print("The items present in myDict:",myDict.items())
print(len(myDict))
print(type(myDict))
myDict={"fruits":10,"vegetables":12,"True":{2:0,2:3,3:4}}
print("The items present in myDict:",myDict.items())
#Append
myDict["Deserts"]=["quality","creamstone","DB&R",434,["Danish","Wealthy"]]
print(myDict)
# myDict=myDict.pop()
# print("Remove item from mydict:",myDict)
# print("values present in mydict:",myDict)
myDict={"fruits":10,"vegetables":12,"flowers":20}
myDict = {1:"A",2:"B",3:"C",4:"D"}
print(myDict[1:3])
print(myDict)





