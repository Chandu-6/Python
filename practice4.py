#Tuple
#empty tuple
mytuple=()
print(mytuple)
#empty tuple
mytuple=tuple()
print(mytuple)
mytuple=(1,2,3,4,5,6)
print(mytuple)
#list to tuple convertion
mytuple=tuple(["chandu","vicky","nikhil","santhosh"])
print(mytuple)
#Count
mytuple=(1,2,3,3,2,3,3,"chandu","santhosh","nikhil","vikas","chandu")
mytuple=mytuple.count("chandu")
print(mytuple)
#index
mytuple=("chandu","vikas","santhosh","nikhil")
mytuple=mytuple.index("nikhil")
print(mytuple)
#length
mytuple=("chandu","vikas","santhosh","nikhil")
mytuple=len(mytuple)
print(mytuple)
#forward slicing
mytuple=tuple(["chandu","vicky","nikhil","santhosh"])
print(mytuple)
mytuple=mytuple[0:2]
print(mytuple)
mytuple=tuple(["chandu","vicky","nikhil","santhosh"])
print(mytuple)
mytuple=mytuple[0:2]
print(mytuple)

#while loop
c=0
while c<10:
    c += 1
    print(c, "Hello world")
    if c==3:
        print("My name is chandu")

#break
c=0
while c<10:
    c += 1

    print(c, "Hello world")
    if c==3:
        print("My name is chandu")
        break






