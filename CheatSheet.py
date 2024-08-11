# name = input("What is your name? ")
#
# print('Hello ' + name)


# birth_year = input("Enter your birth year: ")
# age = 2024 - int(birth_year)
# print('Your age is ' + str(age))


# # Calculator
# first_num = float(input("First: "))
# second_num = float(input("Second: "))
# print("Sum: " + str(first_num + second_num))


# # String objects
# course = 'This is a string'
# print(course.upper())
# print(course.lower())
# print(course.find('s')) # First occurrence of string
# print(course.replace('s','5')) # Replace all occurrences
# print('This' in course) #Check if This is in string, also returns bool

# # Arithmetic
# print(1+1)
# print(2-1)
# print(3*1)
# print(1/1) #returns float
# print(1//1) #returns int
# print(10%3) #module returns reminder of division
# print(10**3) #Power
#
# x = 10
# x += 3
# print(x) #This is 13
# x -= 3
# print(x) #This is 10
#
# x *= 3
# print(x) #This is 30
#
# x //= 3
# print(x) #This is 10 again
#
# #And so on


# # Logical Operators
# price = 25
# print(price >10 and price < 30) #True
# print(price >10 or price < 30) #True
# print(not price > 10) #False

# # If Statements Indentation inside if
# temperature = 19
# if temperature > 30:
#     print("It's a hot day")
# elif temperature > 20:
#     print("It's a nice day")
# else:
#     print("It's chilling")


# # While Loop
# # i = 1
# # while i <= 5: #print 1 to 5
# #     print(i)
# #     i += 1
# #
# # i = 1
# # while i <= 10:  # print 1 to 10 pyramid
# #     print(i * '*')  #python can multiply number to string
# #     i += 1


# Types
# ints
# floats
# strings
# bool
# Lists

# # Lists like arrays on javascript
#
# names = ["John", "Bob", "Fer", "Name1"]
#
# print(names)
# print(names[2])
# print(names[-1]) #Last element on list
#
# names[0] = 'Jon'
# print(names)
#
# print(names[0:2]) # print names from index to index - 1  [John, Bob]. Also does not modify list
#

# # List methods
# numbers = [1, 2, 3, 4, 5]
# numbers.append(6)  #Insert number at last
# print(numbers)
#
# numbers.insert(0, 0)  # insert(index,anything)
# print(numbers)
#
# numbers.remove(4) #Removes where the element is 4 no matter its position, also removes only the first instance
# print(numbers)
#
# numbers.clear() #Clears all list
# print(numbers)
#
# numbers_again = [1, 2, 3, 4, 5,]
#
# print(1 in numbers_again)  # True
# print(7 in numbers_again)  # False
#
# print(len(numbers_again))  # Length of List

# # For loop
# numbers = [1, 2, 3, 4, 5]
# for item in numbers:
#     print(item)


# # Range function
# numbers = range(5)  # Numbers from 0 to 4
# for number in numbers:
#     print(number)
#
# numbers_again = range(5, 10)  # Numbers from 5 to 9
# for number in numbers_again:
#     print(number)
#
# numbers_end = range(5, 10, 2)  # Third param is number of steps, meaning 5 , 7, 9
# for number in numbers_end:
#     print(number)
#
# for number in range(5):  # Shorter way
#     print(number)

# # Tuples
# numbers = (1, 2, 3, 3)
# # Cannot change element by index
# # Cannot append
#
# print(numbers.count(3))  # Prints 2
#
# print(numbers.index(3))  # index of First occurrence of 3
