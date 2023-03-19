# 1.Write a program to create dictionary with Hindi words and its english translation. Provide user with an option to look it up.
hindi_word = {
    "tum" : "you",
    "kaun" : "who",
    "kab" : "when",
    "kaise" : "how"
}
print(hindi_word)

# 2.Write a program to input eight numbers from the user and display all the unique number(once).
num_list = [50,50,60,70,80,40,40,40,30,60]
uni_set = set(num_list)
print(uni_set)

# 3.Can we have a set with 18(int) and "18"(str) as a value in it?
just_set = {18, "18", 18.0}
print(just_set) #Yes, we can have

# 4.What will be the length of following set?
jus_set = set()
jus_set.add(20)
jus_set.add("20")
jus_set.add(20.0)
print(len(jus_set))

# 5.What is the type of this is?
this_type = {}
print(type(this_type))

# 6. Create an empty dictionary. Allow 4 friends to enter their favourite language as key and name as value. Assume that names are unique.
empty_dict = {}
empty_dict['Aman'] = "Japanese"
empty_dict['Aman'] = "Spanish" # What if keys are same
empty_dict['Aze'] = "Japanese" # What if values are same
empty_dict['Ishwar'] = "Hindi"
print(empty_dict)

