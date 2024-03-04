import numpy as np
StudentData=np.loadtxt("C:/StudentData.txt",dtype=int,delimiter=",",skiprows=1,unpack=True)
print(StudentData)
StudentData=np.genfromtxt("c:/StudentData.txt",skip_header=1,dtype=int,filling_values=10)
print(StudentData)
#StudentData=np.savetxt("C:/StudentnewData",StudentData,delimiter="@",fmt="%i")
#print(StudentData)