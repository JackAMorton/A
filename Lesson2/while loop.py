# WHILE LOOP
# WITH THE WHILE LOOP WE CAN EXECUTE
# A SET OF STATEMENTS AS LONG AS A CONDITION IS TRUE

# i = 1
# while i < 6:
#     print(i)
#     if i == 3:
#          break
# i = i + 1

# list_2 = [25,30,56,78,86,45]
# odd = 0
# even = 0
# for i in list_2:
#     if (i % 2) == 0:
#         print(i, "is an even number")
#         even += 1
#     else:
#         print (i, "is and odd number")
#         odd += 1
# print("Evens:", even)
# print("Odd:", odd)

print("What is your number?")
number = int(input())
for i in range(1, number):
    if i % 15 ==0 and i!= 0:
        print("Fizzbuzz")
    elif i % 3 == 0 and i!= 0:
        print("Fizz")
    elif i % 5 == 0 and i!= 0:
        print("Buzz")
    else: print(i)







