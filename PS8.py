# 1.Write a program using function to find greatest of three numbers.
def maximum(a,b,c):
    list = [a,b,c]
    return max(list)
a = 26
b = 15
c = 13
print(maximum(a,b,c))   

# 2.Write a program using function to convert celsius to fahrenheit.
def cel_to_fah(num):
    fah = float(1.8 * num + 32)
    print("Fahrenheit is", fah)
cel_to_fah(40)    

# 3.How do you prevent a python print() function to print a new line at the end.


# 4.Write a recursion function to calculate the sum of first n natural numbers.
def recur_sum(n):
    if n<=1:
        return n
    else:
        return n + recur_sum(n-1)

num = 16
if num<0:
    print("Enter Positive Number: ")
else:
    print("The sum is", recur_sum(num))

# 5.Write a python function to print first n lines of following pattern.


# 6.Write a python function which converts inches to cms.
def inches_to_cms(num):
    print("Length of a centimeter is", num*2.45)

inches_to_cms(2)
inches_to_cms(6)

# 7.Write a python function to remove a given word from a list and strip it at the same time.


# 8.Write a python function to print multipliction table of given number.
def print_tab(num):
    for i in range(1, 11):
        print(num, "x", i, "=", num*i)

n = int(input("Enter Your Number: "))
print_tab(n)        