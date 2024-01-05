#Created on 4/01/24
#myset={1,2,3,4,5,6,7,8}
#meset1={"chandu","vicky","deva"}
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

#Add
myset={1,2,3,4,5}
myset.add("chandu")
print(myset)
#Remove
myset={"chandu","deva","vikas","nikhil"}
myset.remove("deva")
print(myset)
#Disacrd
myset={1,2,3,4,5,6,7}
myset.discard(8)
print(myset)
#Pop
myset={1,2,3,4,5,6,7,8}
myset.pop()
print(myset)
#Update
myset={1,2,3,4,5,6,7,8}
myset.update("cha")
print(myset)
#myset1=set({1,2,3})
print(myset1)
#myset2={"New classes"}
print(myset2)
#myset3="New classes"
print(myset3)
#Frozenset(immutable)
+print(frozenset1)

#numset=set([1,2,3,4,5])
numset={1,2,3,4,5}
for i in numset:
    print(numset)