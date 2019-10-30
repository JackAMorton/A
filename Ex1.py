# First Lesson (Variables)

# a = 1 #int
# b = 2 #int
# c = 3.5 #float
# hi = "Hello World!" #String
# d = 'hello'
# e = 1
# f = 2
#
# print(d,e,f)
# print(type(d),type(e),type(f))
#
# print("Enter your name")
# name = input()
# print("your name is", name)
# print("How old are you?")
# age = input(int)
# print ("You are", age)
# print("When is your birthday?")
# DOB = input()
# print("Your Birthday is", DOB)


# 1. Int, 2. Float, 3. Long, 4. Complex

# a = 1
# # b = 2
# # print(a + b)
# #
# # FloatNum = 1.234
# # IntNum = 5
# #
# # print( FloatNum + IntNum)

# STRING DATA TYPES
#
# Single_quotes = 'Look! single quotes'
#
# Double_quotes = "Look! double quotes"
#
# print(Single_quotes)
# print (Double_quotes)


# escape_example_1 = 'I said \'WoW!\''
# Quote_in_quote = 'I said "WoW!"'
# Reverse_quote_in_quote = "I said 'WoW!'"
#
# print(escape_example_1)
# print(Quote_in_quote)
# # print(Reverse_quote_in_quote)
#
# # SLICING STRINGS
#
# # Hw= "Hello! World"
# # print (len(Hw))
# # print(Hw[7:])
# # print (Hw[-5:])
# # print(Hw[:5])
# # print(Hw[0:5])
#
#
# # STRING METHODS
#
# # White_space = "Lot's of Space at the end                              "
# # print(len(White_space))
# # print(len(White_space.strip()))
#
# # COUNTING OCCURENCES OF SUBSTRING WITHIN A STRING
# Example_text = "here's some text with lot's of text"
# # print(Example_text.count("text"))
#
# # CHANGING TO LOWER CASE
#
# print(Example_text.lower())
#
# #CHANGING TO UPPER CASE
#
# print (Example_text.upper())
#
# #CAPITALISING
#
# print(Example_text.capitalize())
#
# #REPLACING TEXT
#
# print(Example_text.replace("with ", ","))
#
# #CONCATENATION
#
# a = "beth"
# b = "is"
# c = "cool"
#
# print(a.capitalize() + " " + b + " " + c)
#
# x = 2
# y = 2.5
# z = "cool number"
#
# print(str(x) + str(y) + " " + z)

# age = int(input(" what is your age: "))
# currentyear = int(input("What is the current year: "))
# print(currentyear + 100 - age)

# print("What is your Full name?")
# name = input()
# if name != "Beth Ryan":
#     print("Hello ", name, "Nice to meet you")
# else:
#     print("What a terrible name")
# print("How old are you", name, "?")
# age = input()
# if int(age) > 21:
#     print("Wow! You're old!", name)
# else:
#     print("You're way too young", name)
# print("What is the number of your house and street name", name, " ?")
# street_address = input(str)
# print("And what town or city?")
# City_address = input(str)
# print("And what County and Postal Code?")
# County_Postal_Code = input(str)
# print("So you live at " + "\n" + street_address + "\n" + City_address + "\n" + County_Postal_Code)
#
# a = True
# b = False
#
# print(a == b)
# print(a != b)
# print(a >= b)
# print(a <= b)
#
# print(True and False)
# print(False and True)
# print(False or True)
#
# # BOOLEAN METHODS WITHIN STRINGS
#
# hi = "Hello World!"
#
# print(hi.isalpha())
# print(hi.islower())
# print(hi.endswith("!"))
# print(hi.startswith("H"))

# BOOLEAN NUMBERS

# x = 0
# y = 10
#
# print(bool(x))
# print(bool(y))


# shopping_list = ["eggs", "bread", "bananas", "biscuits", "milk"]
# print(shopping_list)
# print(type(shopping_list))
# print(shopping_list[0])
# print(shopping_list[-1])
# shopping_list[0] = "sugar"
# print(shopping_list)
# shopping_list.pop()
# print(shopping_list)

#
# mixture = [1, 2, 3,"one", "two", "three"]
#
# print(mixture)
# print(mixture[1:3])
# print(mixture[-2::])
# print(mixture[::2])

# TUPLES

# A tuple is a collection which is ordered awnd unchangeable. In Python tuples are written with round brackets

# essentials = ("bread", "eggs", "milk")
# essentials[0] = "beans"
#
# print(essentials)
# print(essentials.count("bread"))

# Dictionaries
# A dictionary is a collection which is unordered
# changeable and indexed. In Python dictionaries are written
# with curly brackets, and they have keys and values

#Creating a dictionary

# student_1 = {
#      "name": "susan",
#      "stream": "tech",
#      "completed_lessons": 4,
#      "completed_lessons_names": ["variables", "data_types", "set up"]
#     }
# student_1["gender"]= "Female"
# print (student_1)
# student_1.pop("Stream")
# print(student_1)
#
# # accessing data using the key
# print(student_1["stream"])
# print(student_1["completed_lessons_names"][2])
#
# # Changing a value
#
# student_1["completed_lessons"] = 3
# print(student_1["completed_lessons"])
#
# #getting the keys
# print(student_1.keys())
# print(student_1.values())


# Sets
# A set is a collection which is unordered and unindexed
# In python sets are written with curly brackets.

# car_parts = {"wheels", "doors", "exhaust"}
# print(car_parts)
#
# car_parts.add("windows")
# print(car_parts)
#
# car_parts.discard("exhaust")
# print(car_parts)
#
# car_parts.update(["Engine","Seats","Steering"])
# print(car_parts)


#FROZEN SETS
# Elements are immutable versions of the set list, similar to a tuple although not ordered or indexed.
# WIll be relatively rare to use a frozen set without clear reasons for its use

# x = frozenset([1, 2, 3, 4])

# CONTROL FLOW




