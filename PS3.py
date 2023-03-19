# 1. Write a python program to display user entered name by Good Afternoon using input() function...
"""Name = input("Enter your name: ")
print("Good Afternoon " + Name)"""

# 2.Write a python program to fill in a letter template.
letter = '''Dear <|Name|>,
        You are seleted!
        <|Date|>'''
print(letter.replace("Name", "Aman"))

# 3. Write a python program to detect white spaces in string.
sen = "Hey,  How are you doing?"
print(" " in sen)

# 4. Replace the double space from the string with single space
sent = "Hey,  How are you doing?"
print(sent.replace("  ", " "))

# 5. Write a python program to format the following letter using escape character sequence.
senc = "Hey, this practice set is amazing.\nThank you!"
print(senc)