import numpy as np
# stack value
array1=np.array([[1,2,3,4],[6,7,8,9]])
array2=np.array([[1,2,3,4],[6,6,7,8]])
result=np.stack((array1,array2),axis=2)
print("stack value:\n",result)

# hstack
array3=np.array([[1,2,3],[5,5,7]])
array4=np.array([[1,2,3],[5,6,7]])77
result=np.hstack((array3,array4))
print("hsatck value:\n",result)

# vstack
array5=np.array([[1,2,3],[4,5,6],[7,8,9]])
array6=np.array([[1,2,3],[5,6,7],[2,3,4]])
result=np.vstack((array5,array6))
print("vstack value:\n",result)

# repeat
array7=np.array([[1,2,3],[5,6,7]])
array8=np.array([[9,8,7],[5,4,3]])
result=np.repeat((array7,array8),1,axis=1)
print("repeat value is:\n",result)

# roll
array9=np.array([[1,2,3],[5,6,7]])
# array10=np.array([[9,8.7],[3,4,5]])
result=np.roll(array9,3)
print("roll value is:\n",result)