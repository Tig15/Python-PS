# 1.Write a program to print multiplication table of a given number using for loop.
"""tab = int(input("Enter Your Number: "))

for i in range(1, 11):
    print(tab, 'x', i, '=', tab*i)"""

# 2.Write a program to greet all the person names stored in a list and which starts with S.
name_list = ["Aman", "Shubham", "Sarvesh", "Jack"]
check = 'S'
specify_list = []
for i in name_list:
    if i.find(check) == 0:
        specify_list.append(i)

print(specify_list)        

# 3.Write a program to print multiplication table of a given number using while loop.
num  = 6
i = 1
while i < 11:
    print(num, "x", i, "=", num*i)
    if i == 10:
        break
    i +=1   

# 4.Write a program to find the whether given number is prime or not.
pri = int(36)
flag = False

if pri > 1:
    for i in range(2, pri):
        if (pri % i) == 0:
            flag = True
            break
if flag:
    print(pri, "Is not a prime number")
else:
    print(pri, "Is a prime number")                

# 5.Write a program to find the sum of firt n natural numbers using while loop.
nat = 18
if nat < 0:
    print("Enter Positive Number")
else:
    sum = 0
    while (nat>0):
        sum += nat
        nat -=1
        print("The sum is", sum)    

# 6.Write a program to calculate the factorial of a given number using for loop.


# 7. Write a program to print the following star pattern for n. (n=3)
""" *
   ***
  ***** """
rows = 3
k = (2*rows) - 2
for i in range(0,rows):
    for j in range(0,k):
        print(end=" ")
    k -= 1
    for j in range(0, i+1):
        print("*", end=' ')
    print("")       

# 8. Write a program to print the following star pattern for n . (n=3)
""" *
    **
    *** """
n = 3
m = (2*n) - 2
for i in range(0,n):
    for j in range(0,m):
        print(end="")
    m = m-1
    for j in range(0, i+1):
        print("* ", end="")
    print("")        

# 9. Write a program to print the following star pattern for n. (n=3)
""" ***
    * *
    *** """


# 10.Write a progran to print multiplication table of n using for loop in reversed order.
