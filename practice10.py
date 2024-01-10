#Created by chandana p
#Created on 10/01/24
#read
import os
filepath="c:\\Samples\EmployeeData.txt"
empFd=open(filepath,"r")
mydata=empFd.read()
print("The data present in employeedata file is:\n",mydata)
#Readline
empFd=open(filepath,"r")
empFd.seek(0)
mydata = empFd.readline(20)
print("The read line is:",mydata)
empFd.close()
#Readlines
empFd=open(filepath,"r")
# empFd.seek(0)
print(empFd.tell())
mydata = empFd.readlines()
print("The readlines is:",mydata)
empFd.close()


#Write
import os
filepath="c:\\Samples\EmployeeData_1.txt"
empFd=open(filepath,"w+")
mydata="My name is chandana.I am learning python"
empFd.write(mydata)
#empFd.close()
#writelines
list=[1,2,34,5,6,7,"chandu","vicky","vihitha"]
empFd.writelines(str(list))
empFd.close()
