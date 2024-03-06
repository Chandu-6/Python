# A="Apple"
# B="Animal"
# count=0
# for i in (A and B):
#     if("A==A","p==p","l==l","e==e","n==n","i==i","m==m"):
#         print("The repeated character is")
#     else:
#         print("There is no repeated character")
#         count+=1
def find_repeated_characters(string1, string2):
    repeated_characters = []

    # Iterate over characters in the first string
    for char in string1:
        # Check if the character is in both strings and not already in repeated_characters list
        if char in string2 and char not in repeated_characters:
            repeated_characters.append(char)

    return repeated_characters

# Main function to test the find_repeated_characters function
def main():
    string1 = input("Enter the first string: ")
    string2 = input("Enter the second string: ")

    repeated_chars = find_repeated_characters(string1, string2)
    if repeated_chars:
        print("Repeated characters:", repeated_chars)
    else:
        print("No repeated characters found.")

if __name__ == "__main__":
    main()
def count_repeated_characters(string1, string2):
    char_count1 = {}  # Dictionary to store character counts for string1
    char_count2 = {}  # Dictionary to store character counts for string2
    repeated_count = 0  # Initialize count of repeated characters

    # Count characters in the first string
    for char in string1:
        char_count1[char] = char_count1.get(char, 0) + 1

    # Count characters in the second string
    for char in string2:
        char_count2[char] = char_count2.get(char, 0) + 1

    # Iterate over keys in the first dictionary
    for char in char_count1:
        # Check if the character is in the second string and count the minimum occurrences
        if char in char_count2:
            repeated_count += min(char_count1[char], char_count2[char])

    return repeated_count


# Main function to test the count_repeated_characters function
def main():
    string1 = input("Enter the first string: ")
    string2 = input("Enter the second string: ")

    count = count_repeated_characters(string1, string2)
    print("Count of repeated characters:", count)

if __name__ == "__main__":
    main()
#What is the output in python
a=19%2
print("The output is:",a)
#Write a code the given number is even or odd
num=int(input("Enter a number"))
if(num%2==0):
    print("The given number is even ")
else:
    print("The given number is odd")
#Write a code to print for two  max numbers
num1=int(input("Enter a number"))
num2=int(input("Enter a number"))
maximum=max(num1,num2)
print("The max value is:",maximum)
#Write a code for to check prime numbers
num=int(input("Enter a number"))
if((num%2)+1):
    print("The given number is a prime number")
else:
    print("The given number is not a prime number")
#Swapping of two numbers
num1=int(input("Enter a first number"))
num2=int(input("Enter a second number"))
print("The first value before swapping",num1)
print("The second value before swapping",num2)
marks = num1
num1 = num2
num2 = marks
print("The first value after swapping",int(num1))
print("The second value after swapping",int(num2))

#Python program to display calendar

import calendar

# Get the month and year from the users
year = int(input("Enter the year: "))
month = int(input("Enter the month: "))

# Displaying the calendar for the given year and month
print(calendar.month(year, month))


