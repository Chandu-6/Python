#Created by Chandana p
#Created on 3/03/24
#Pandas Series
import numpy as np
import pandas as pd
#Series
Age_Series=pd.Series([20,30,40,50,60],name="StuAge")
print(Age_Series)
Salary_series=pd.Series({"Chandu":20000,"Vicky":30000,"Chinna":28000,"Nikhil":35000,"Suntosh":40000},name="Salary Data")
print(Salary_series)
print("The max salary is:",Salary_series.max())
print("The min salary is:",Salary_series.min())
print("The size of Salary series is:",Salary_series.size)
print("The head values are:\n",Salary_series.head())
print("The tail values are:\n",Salary_series.tail(3))
print("The count is:",Salary_series.count())

#####
String_series=pd.Series(["Chandu",21,"Vicky",24,"Nikhil",16,"Sunthosh",14,"Pramod",17,"Vihitha",19],name="Details")
print(String_series)
Newcount=String_series.count()
print("The count is:",Newcount)
#Add of two lists
Newlist1=pd.Series([10,20,30,"Chandu",60,66],index=[1,3,5,7,9,6])
Newlist2=pd.Series([20,30,40,50,60,80],index=[1,3,5,6,8,0])
chandu=Newlist1+Newlist2
print("The newlist is:\n",chandu)
new=chandu.count()
print("The count is:\n",new)

numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
print("The slicing is:",numbers[1 :: 2])

