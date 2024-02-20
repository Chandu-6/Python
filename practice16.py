import numpy as np
mylist=[[1,2,3],[4,5,6],[7,8,9]]
matrix= np.array(mylist)
print(matrix)
#sub matrix slicing
result=matrix[ : , : ]
print("The result matrix is :\n",result)
result=matrix[0:3,0:3]
print("the result matrix is:\n",result)
result=matrix[1:3,1:3]
print("The 2*2 matrix is:\n",result)
result=matrix[0:2,0:3]
print("the 2*3 matrix is:\n",result)
# result=matrix[0:1:3, 1:1:1]
# print("The 2nd coloumn is:\n",result)
print("the matrix is:\n",matrix)
print("The size of matrix is:",matrix.size)
print("The shape of matrix is:",matrix.shape)
print("the data type of matrix is:",matrix.dtype)
print()
print()
mylist=[10,20,30,40,50,60,70,80,90]
arr=np.array(mylist)
print("The array is:",arr)
print("the shape of array is:",arr.shape)
print("The dimension of array is:",arr.ndim)
result=arr.reshape(3,3)
print("the resultant matrix is:\n",result)
# print("the resultant matrix is:\n",arr.reshape(2,3))
print("the size of reshape array is:",result.size)
print("the dimension of reshape array is:",result.ndim)

