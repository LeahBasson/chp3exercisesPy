# 1. A loop that displays Python is fun 5 times
# for eachPass in range(5):
#     print("Python is fun")
    
#2.a.
# num = 3
# for count in range(num):
#     print(f"The value is {count}")
    
#b
# for count in range(0,9,2):
#     print(f"The answer is {count}")
    
#c
# for count in range(5):
#     print(f"The answer is {count**2}")

#d
# total = 0
# for count in range(0,9,2):
#     total += count
#     print(f"The answer is {count}")
#     
# print(f"The sum is {total}")

# 3.a. Input 2 numbers and display it.
# num1 = int(input("Enter the first number: "))
# num2 = int(input("Enter the second number: "))
# 
# print(f"The first number is {num1}")
# print(f"The second number is {num2}")

# 3.b. Reads in 2 numbers representing the lower bound and upper bound for a loop. Sum all the numbers in the range and display the sum.
# lower = int(input("Enter lower bound: "))
# upper = int(input("Enter upper bound: "))
# 
# sum = 0
#  
# for number in range(lower, upper + 1):
#     sum = sum + number
#        
# print(f"The sum is {sum}")

#4.
# for characters in "Hello everyone":
#     print(f"{characters}")

#5.
# for characters in "Helloeveryone":
#     print(characters, ord(characters))
    
# Exercises on formatting text for output
# x = 15
# y = 12
# z = 2004
# 
# result = f"{x:>6}{y:>6}{z:>6}"
# 
# print(result)

#Exercises combining loops, input, and formatting.
# sum_of_items = 0
# 
# print(f"Price of items in store {127978:c}")
# print("====================================================")

# for eachItem in range(1, 5):
#     price = float(input(f"Enter the price of item {eachItem}: R"))
#     print(f"{price:.2f}")
#     sum_of_items += price
#     average = sum_of_items / eachItem
    
# print("====================================================")
# print(f"Total : R{sum_of_items:.2f}")
#print(f"Amount of items are : {eachItem} items")
# print(f"Average of items is : R{average:.2f}")

#Exercises on if statements

#1. program that asks the user for a number and checks if it is divisible by five.
# num = int(input("Enter number: "))
# 
# if num % 5 == 0:
#     print(f"The number {num} is divisble by 5.")
# else:
#     print(f"The number {num} is not divisble by 5.")
    
#2. determine if mark of a student is a fail, pass or distinction.
# mark = int(input("Please enter mark of student: "))
# 
# if mark < 50:
#     print("Fail")
# elif mark >= 50 and mark < 75:
#     print("Passed")
# else:
#     print("Distinction")
 
# 3.check if they are a child (below 13), a teenager (13-19), or an adult (20+).
# user_age = int(input("Please enter your age: "))
# 
# if user_age < 13:
#     print(f"You are a child {128512:c}")
# elif user_age >= 13 and user_age <= 19:
#     print(f"You are a teenager {128526:c}")
# else:
#     print(f"You are an adult {128523:c}")

# 4. Check if a given year is a leap year or not.
# year = int(input("Please enter year: "))
# 
# if year % 4 == 0:
#     print(f"The year {year} is a leap year.")
# else:
#     print(f"The year {year} is not a leap year.")
 
# 5. ask for two numbers and print which one is greater, or if they are equal.
# num1 = int(input("Please enter the first number: "))
# num2 = int(input("Please enter the second number: "))
# 
# if num1 > num2:
#     print(f"{num1} is greater than {num2}.")
# elif num2 > num1:
#     print(f"{num2} is greater than {num1}.")
# elif num1 == num2:
#     print(f"{num1} is equal to {num2}.")

 
#6. Ask the user for three numbers and print them ranking from smallest to greatest.
# num1 = int(input("Please enter the first number: "))
# num2 = int(input("Please enter the second number: "))
# num3 = int(input("Please enter the third number: "))
# 
# if num1 <= num2 <= num3:
#     print(f"1. {num1} \n2. {num2} \n3. {num3}")
# elif num1 <= num3 <= num2:
#     print(f"1. {num1} \n2. {num3} \n3. {num2}")
# elif num2 <= num1 <= num3:
#     print(f"1. {num2} \n2. {num1} \n3. {num3}")
# elif num2 <= num3 <= num1:
#     print(f"1. {num2}  \n2. {num3} \n3. {num1}")
# elif num3 <= num1 <= num2:
#     print(f"1. {num3}  \n2. {num1} \n3. {num2}")
# elif num3 <= num2 <= num2:
#     print(f"1. {num3}  \n2. {num2} \n3. {num1}")

#7. checks if the entered password matches a predefined password.
# pd_pwd = "leah20"
# new_pwd = input("Please enter the password: ")
# 
# if pd_pwd == new_pwd:
#     print("This password already exists!")
# else:
#     print(f"Your new password is {new_pwd}")
 
#Exercises combining loops, input and if statements
#1. asks the user for 5 numbers and tells them whether each one is even or odd.

<<<<<<< HEAD
#asks the user for 5 numbers and tells them whether each one is even or odd.
# for count in range(1,6):
#     number = int(input(f"Enter number {count}: "))
#     print(number)
#     if number % 2 == 0:
#         print("The number is even")
#     else:
#         print("The number is odd")

#asks the user for 5 numbers and calculates the sum of all positive numbers.
# sum = 0
# for count in range(1,6):
#     number = int(input(f"Enter number {count}: "))
#     print(number)
#     if number % 2 == 0:
#         sum += number
# 
# print(f"The sum of all the even numbers is {sum}")
        
#Ask the user for 7 numbers and determine which is the largest.
numbers = []
first_number = int(input("Enter number 1: "))
largest = first_number
numbers.append(largest)
cnt = 2

for number in range(6):
    number = int(input(f"Enter number {cnt}: "))
    cnt += 1
    numbers.append(number)
    if number > largest:
        largest = number

print(numbers)
print(f"{largest} is the largest number.")










 
 
