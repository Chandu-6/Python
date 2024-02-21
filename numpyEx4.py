import numpy as np
#Array data members and methods
#Created by chandana p
#cteated on 21/02/24
myarray=np.array([[1,2,3],[4,5,6]])
print("The elements present in array is:\n",myarray)
#size
print("The size of array is:",myarray.size)
#shape
print("The shape of myarray is:",myarray.shape)
#Dimension
print("The dimension is:",myarray.ndim)
#Data type
print("The data type of array is:",myarray.dtype)
#tolist
array1=np.array([[1,2],[3,4]])
list=array1.tolist()
print("The result list is:",list,type(list))
#concatenation
array1=np.array([[1,2],[3,4],[5,6]])
array2=np.array([[1,2],[3,4],[7,8]])
concatearray=np.concatenate((array1,array2))
print("The concatenation array is:\n",concatearray)
#reshape
mylist=[10,20,30,40,60,70]
newarray=np.array(mylist)
print("The elements present in newarray is:",newarray)
print("The dimension of array is:",newarray.ndim)
print("The shape of newarray is:",newarray.shape)
print("The size of newarry is:",newarray.size)
print("The data type of new array is:",newarray.dtype)
twodarray=newarray.reshape(2,3)
print("The twodarray is:\n",twodarray)
print("The dimension of twodarray is:",twodarray.ndim)
print("The shape of twodarray is:",twodarray.shape)
print("the size of twodarray is:",twodarray.size)
#Mean
array1=([[1,2,3,4,5,6,7]])
result=np.mean(array1)
print("The mean value of array1 is:",result)
#Min
array1=np.array([[1,2,3],[4,0,6]])
result=np.min(array1)
print("The min is:",result)
#Max
array2=np.array([[[23,50,33,55]],[[80,33,22,11]]])
result=np.max(array2)
print("The max value is",result)

#sum
#One dimension
array1=[1,2,3,4,5]
result=np.sum(array1)
print("The onedimension sum is:",result)

#Two dimension (return coloumn wise sum)
array1=np.array([[1,2,3],[4,5,6]])
result=np.sum(array1,axis=0)
print("The coloumn wise sum is:",result)
#It returns row wise sum
result=np.sum(array1,axis=1)
print("The row wise sum is:",result)
#Sort
myarray=([0,-1,2,3,2,1,0])
result=np.sort(myarray)
print(result)
#for axis=0
array1=np.array([[6,2,-1],[0,5,3]])
result=np.sort(array1,axis=0)
print("The result is:\n",result)
#for axis=1
array1=np.array([[6,2,-1],[0,5,3]])
result=np.sort(array1,axis=1)
print("The result is:\n",result)
#sort for strings
Names=np.array(["Chandu","Vicky","chinna","Lepakshi","rajitha","madhu"])
print("The result is:0",np.sort(Names))
#Transpose
myarray=np.array([[1,2,3],[4,5,6]])
print("The transposed matrix is:\n",np.transpose(myarray))
#Append(add of array1 and array2 like concatenation)
array1 = np.array([1, 2, 3])
array2 = np.array([4, 5, 6])
array3 = np.append(array1, array2)
print("The append array is:",array3)
#Astype(It converts one data type to another data type)
array=np.array([1,2,3,4,5])
result=array.astype(float)
print("The float array is:",result)
array=np.array([1.1,2.0,3.2,4.2,5.1])
result=array.astype(int)
print("The int array is:",result)
#arange
myarray=np.arange(5)#-->Range(end it start with 0)
print(myarray)
myarray=np.arange(10,20)#---->(start,end)
print(myarray)
myarray=np.arange(10,20,3)#--->(start,end,steping)
print(myarray)
#Item size
myarray=np.array([1.0,2.2,3.3])
result=myarray.itemsize
print("the itemsize of myarray is:",result)





