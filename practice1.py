#LIST
#Created by chandana p
#created on 28/12/23
#append
fruits=["Apple","Grapes","Banana"]
fruits.append("Cherry")
print(fruits)
#insert
fruits=["Apple","Grapes","Banana"]
fruits.insert(1,"Goa")
print(fruits)
#extend
fruits=["Apple","Grapes","Banana"]
fruits.extend(["Pineapple","Muskmelon","Berry"])
print(fruits)
#replace(single)
fruits=["Apple","Grapes","Banana"]
fruits[0]="Watermelon"
print(fruits)
#replace multiple strings
fruits=["Apple","Grapes","Banana"]
fruits[0:2]=["Goa","Orange"]
print(fruits)
#delete(del)
fruits=["Apple","Grapes","Banana"]
del fruits[1]
print(fruits)
#clear
fruits=["Apple","Grapes","Banana"]
fruits.clear()
print(fruits)
#remove(it takes string and removes)
fruits=["Apple","Grapes","Banana"]
fruits.remove("Banana")
print(fruits)
# fruits.remove("banana")
# print(fruits)
#pop(based on index it removes)
fruits=["Apple","Grapes","Banana"]
fruits.pop(0)
print(fruits)

#numbers
#sort(ascending order)
nums=[41,30,34,22,45,60,67,80]
nums.sort()
print(nums)
#sort(descending order)
nums=[41,30,34,22,45,60,67,80]
nums.sort(reverse=True)
print(nums)
#min
marks=[41,30,34,22,45,60,67,80]
marks=min(marks)
print(marks)
marks=[41,30,34,22,45,60,67,80]
marks=max(marks)
print(marks)
#reverse
nums=[41,30,34,22,45,60,67,80]
nums.reverse()
print(nums)


#TUPLE
#tuple converted into list
fruits=("Apple","Banana","Mango","Watermelon")
fruitsList=list(fruits)
print(fruitsList)
#list converted into tuple
fruits=["Apple","Banana","Mango","Watermelon"]
fruitsList=tuple(fruits)
print(fruitsList)
#index
fruits=("Apple","Banana","Mango","Watermelon")
fruits=fruits.index("Apple")
print(fruits)
#count
fruits=("Apple","Apple","Banana","Mango","Watermelon","Apple")
fruits=fruits.count("Apple")
print(fruits)
fruits=("Apple","Banana","Mango","Watermelon","Apple")
newfruits=list(fruits)
print(newfruits)
newfruits.append("Grapes")
print(newfruits)
fruits=tuple(newfruits)
print(fruits)

#set
flowers={"Rose","lotus","Jasmine"}
print(flowers)
print(len(flowers))
#Dictonary
person={"fname":"potturu","lname":"chandu","mobile":000}
newperson=person['fname']
newperson1=person['lname']
newperson2=person['mobile']
print(newperson)
print(newperson1)
print(newperson2)
person.update({"mobile":"555"})
print(person)
person.pop("mobile")
print(person)
person.popitem()
print(person)
person={"fname":"potturu","lname":"chandu","mobile":000}
del person[("fname")]
print(person)
person={"fname":"potturu","lname":"chandu","mobile":000}
person ["age"]=21
print(person)
person.clear()
print(person)
person={"fname":"potturu","lname":"chandu","mobile":000}
person=person.keys()
print(person)
person={"fname":"potturu","lname":"chandu","mobile":000}
person=person.values()
print(person)
person={'fname': 'potturu', 'lname': 'chandu', 'mobile': 0, 'age': 21}
if "age" in person:
    print("yes,the age is there")
else:
    print("the adress is not there")


#Find the repeated characters in string by using for loop
name = input("enter the name:")
repeated_chars = []
lenofstring = len(name)
print("length of string:", lenofstring)
count = 1
for strItr in name:
   if (name.count (strItr)>1 and strItr not in repeated_chars):
       print("the repeated is found it is position:", count, "and the repeated is:", strItr)
   count+=1
#Find the repeated characters in a string by using while loop
def find_repeated_characters(input_string):
    repeated_characters = []
    index = 0

    while index < len(input_string):
        current_char = input_string[index]

        # Check if the current character is repeated later in the string
        if current_char in input_string[index + 1:]:
            repeated_characters.append(current_char)

            # Remove all occurrences of the repeated character to avoid counting it again
            input_string = input_string.replace(current_char, '')

        else:
            index += 1

    return repeated_characters

# Example usage:
input_str = "hello world"
result = find_repeated_characters(input_str)

if result:
    print("Repeated characters:", result)
else:
    print("No repeated characters found.")












