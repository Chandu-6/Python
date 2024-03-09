import numpy as np
import pandas as pd
#To create empty dataframe
emptyDf=pd.DataFrame()
print(emptyDf)
#Creation of dataframe with numpy array
array1=np.array([10,20,30,40,50])
array2=np.array([100,200,300,400,500,600])
array3=np.array([1000,2000,3000,40000,5000,6000,7000])
print(pd.DataFrame(array1))
array4=pd.DataFrame([array1,array2,array3],columns=["A","B","C","D","E","F","G"])
print(array4)
#Creation of Dataframe from list of dictionaries
listDict=[{"Name":"Chandu","Age":21},{"Name":"Vicky","Age":24,"place":"Bnglr"}]
listDf=pd.DataFrame(listDict)
print(listDf)
#Creation of Dataframe from dictionary of lists
dictlist={"Fruits":["Apple","Banana","Grapes","Orange"],"Flowers":["Roses","Jasmine","lilly","Hibiscus"]}
dictDf=pd.DataFrame(dictlist)
print(dictDf)
#Creation of Dataframes from series
seriesX=pd.Series([1,2,3,4,5],index=["A","B","C","D","E"])
seriesY=pd.Series([1,2,3,4,5],index=["A","B","C","D","E"])
seriesZ=pd.Series([10,20,30,40,50],index=["A","B","C","D","E"])
seriesXDf=pd.DataFrame(seriesX)
print(seriesXDf)
SeriesDf=pd.DataFrame(seriesX,seriesZ)
print(SeriesDf)
#Creation of Dataframes from dictionary series
Marks={"Chandu":pd.Series([30,40,50],index=["Telugu","Hindi","Maths"]),"Vikas":pd.Series([70,73,75],index=["Telugu","Hindi","Maths"]),"Nikhil":pd.Series([60,70,72],index=["Telugu","Hindi","Maths"])}
marksdf=pd.DataFrame(Marks)
print(marksdf)

