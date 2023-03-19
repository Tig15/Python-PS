# 1. Write a python program to add two numbers.
a = 23
b = 54
sum = a + b 
print(sum)

# 2. Write a python program to find remainder...
x = 15
y = 6
rem = x % y # % is modulus 
quo = x // y # // is floor division
print(rem)
print(quo)

# 3. Check the type of value assigned using input() function.
"""Name = input("Enter your name: ")
Age = input("Enter your age: ")
Percentage = input("Enter your percentage: ")

print(type(Name))
print(type(Age))
print(type(Percentage))"""

# 4. Use the comparison operator whether a given varibale is greater than or not...
eng10 = 65
eng12 = 58
if(eng10 > eng12):
    print("English 10th mark is better than 12th")
else:
    print("English 12th mark is better than 10th")     

# 5. Write a python program to find average of number entered by the user.
"""num1 = float(input("Enter the first number: ")) 
num2 = float(input("Enter the second number: "))
avg = (num1 + num2)/2
print("The average of num1 and num2 is %.2f" %avg)"""

# 6. Write a python program to find the square of number entered by the user.
num = int(input("Enter your number: "))
sqr = num ** 2
print(sqr)