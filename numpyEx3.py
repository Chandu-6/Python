import numpy as np
#Addion operation by using numpy array
myarray=np.array([[1,2,3],[4,5,6],[7,8,9]])
newarray=np.array([1,2,3])
result=myarray+newarray
print(result)
myarray=np.array([[1,2,3],[4,5,6],[7,8,9]])
newarray=np.array([[1,2,3],[4,5,6],[7,8,9]])
result=myarray+newarray
print(result)
myarray=np.array([[1,2,3]])
newarray=np.array([[1,2,3],[4,5,6],[7,8,9]])
result=myarray+newarray
print("The result is:\n",result)
#Multiplication
myarray1=np.array([[2,3,4,5]])
newarray1=np.array([2,3,4,5])
result1=myarray1*newarray1
print(result1)
myarray1=np.array([[2,3,4,5]])
newarray1=np.array([2])
result1=myarray1*newarray1
print(result1)
#Matrix multiplication
myarray2=np.array([[1,2,3],[4,5,6]])
newarray2=np.array([[1,2,3],[4,5,6],[7,8,9]])
result2=myarray2@newarray2
print("the result matrix multiplication is:\n ",result2)

myarray3=np.array([[1,2,3],[4,5,6],[1,2,3]])
newarray3=np.array([[1,2,3],[4,5,6],[7,8,9]])
result3=myarray3@newarray3
print("the result3",result3)

# slicing
myarray=np.array([[1,2,3],[4,5,6],[7,8,9]])
result4=myarray3
print(myarray[0:1,1])
