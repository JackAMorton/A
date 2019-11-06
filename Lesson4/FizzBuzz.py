# FOR LOOP
# for number in range (50):
#     if number % 3 ==0 and number % 5 ==0:
#         print("Fizzbuzz")
#     elif number % 3 ==0:
#         print("Fizz")
#     elif number % 5 ==0:
#         print ("Buzz")
#     else: print(number)

# FUNCTION
def Fizzbuzz ():
  number = int(input("What is you number?"))
  for i in range(1,number):
    if i % 3 == 0 and i % 5 == 0:
        print("Fizzbuzz")
    elif i % 3 ==0:
         print("Fizz")
    elif i % 5 ==0:
         print ("Buzz")
    else: print(i)

Fizzbuzz()

#LOOP AND INPUT

# number = int(input("What is the limit?"))
# for i in range(1,number):
#     if i % 3 == 0 and i % 5 == 0:
#         print("Fizzbuzz")
#     elif i % 3 ==0:
#           print("Fizz")
#     elif i % 5 ==0:
#           print ("Buzz")
#     else: print(i)

# WHILE LOOP WITH INPUT

# number = int(input("What is the limit?"))
# i = 1
# while i <= number:
#     if i % 3 == 0 and i % 5 == 0:
#         print("Fizzbuzz")
#     elif i % 3 ==0:
#           print("Fizz")
#     elif i % 5 ==0:
#           print ("Buzz")
#     else: print(i)
#     i = i +1

# WHILE LOOP WITHOUT INPUT

# number = 67
# i = 1
# while i <= number:
#     if i % 3 == 0 and i % 5 == 0:
#         print("Fizzbuzz")
#     elif i % 3 ==0:
#           print("Fizz")
#     elif i % 5 ==0:
#           print ("Buzz")
#     else: print(i)
#     i = i +1

# INPUT WITHOUT LOOP
#
# i = int(input("What is your number?"))
#
# if i % 3 == 0 and i % 5 == 0:
#         print("Fizzbuzz")
# elif i % 3 ==0:
#           print("Fizz")
# elif i % 5 ==0:
#           print ("Buzz")
# else: print(i)