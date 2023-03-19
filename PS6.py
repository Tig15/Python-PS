# 1. Write a program to find greatest of four number entered by the user.
"""num1 = input("Enter Your First Number: ")
num2 = input("Enter Your Second Number: ")
num3 = input("Enter Your Third Number: ")
num4 = input("Enter Your Fourth Number: ")
if(num1 > num2 and num1 > num4):
    print("First Number is Greater!")
elif(num2 > num3):
    print("Second Number is Greater!")
elif(num3 > num4):
    print("Third Number is Greater!")
elif(num4 > num2):
    print("Fourth Number is Greater!")    
else:
    print("Done")"""

# 2. Write a program to find out whether a student is pass or fail, if it requires total 40% and at least 33% in each subject to pass. Assume 3 subjects and take marks as an input.    
"""math = float(input("Enter Your Marks: "))
science = float(input("Enter Your Marks: "))
english = float(input("Enter Your Marks: "))

total = float(input("Enter Total Marks: "))

percen = (math + science + english)*100/total

if(percen>=33):
    print("Pass!")
else:
    print("Fail!")"""    

# 3.A spam comment is defined by text containing some comments. Write a program to detect this spam.


# 4.Write a program to find whether a given username contain 10 characters or not.
"""username = input("Enter Your Full Name: ")
if len(username) > 10:
    print("Yes, username contain 10 characters")
else:
    print("No, it don't contain more than 10")"""

# 5.Write a python program to find out whether a name present in a list or not.
group_name = ["Aman", "Tig", "Aze", "Ishwar"]
if "Ishwar" in group_name:
    print("Yes, Ishwar is present in Group Name!")
else:
    print("No, It is not presen!")

# 6.Write a program to calculate the grade of marks.
"""my_marks = int(input("My Marks is "))

if(my_marks > 90):
    print("A+ Grade")
elif(my_marks > 80):
    print("A Grade")
elif(my_marks > 70):
    print("B Grade")
elif(my_marks > 60):
    print("C Grade") 
elif(my_marks > 50):
    print("D Grade")
elif(my_marks > 40):
    print("E Grade")
else:
    print("F Grade")"""

# 7.Write a program whether the given post is talking about "Aman" or not 
post = ""   