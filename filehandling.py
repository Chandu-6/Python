#Topic:File handling
#Created by chandana.p
#Created on 22/02/24
#Read mode
c=open("demo.txt",mode="r")
print(c.read())
c.close()
# #write mode
c=open("demo.txt",mode="w")
c.write("i like listening music")
c.close()
# #append
c=open("demo.txt",mode="a")
c.write(",playing chess")
c.close()
#r+(read write)
c=open("demo.txt",mode="w+")
c.write("w+ method")
c.seek(0)
print(c.read())
c.close()
# c=open("demo.txt",mode="r")
# print(c.read())
# c.close()




