# A CLASS IS A BLUEPRINT FOR CREATING OBJECTS

#CREATING A CLASS

# class Dog:
#     animal_kind = "canine"
#     def __init__(self,name = "Tommy",age = "19"):
#         self.name = name
#         self.age = age
#     def bark(self):
#         print("Woof")
#     def speak(self,sound):
#         print("{} likes it when you {}".format(self.name,sound))
#     def eat(self):
#         print("Yummy Yummy")
#     def run(self):
#         print("Woosh")
#
# #ADDING METHOD
#
# # INSTANTIATION OF OBJECTS
#
# Dog1 = Dog("Ignacio", 9)
# Dog2 = Dog("Keith", 5)
# Dog3 = Dog("Ian",99)
#
# print(type(Dog1))
# Dog1.bark()
# Dog1.eat()
# Dog1.run()
#
# #PRINTING THE ATTRIBUTES
#
# print("The oldest dog is {}".format(max(Dog1.age, Dog2.age, Dog3.age)))
# print("The youngest dog is {}".format(min(Dog1.age, Dog2.age, Dog3.age)))


# def fizzbuzz(num):
#     for i in range(1,num +1):
#         if i % 5 == 0 and i % 3 ==0:
#             print("Fizzbuzz")
#         elif i % 5 ==0:
#             print("Fizz")
#         elif i % 3 ==0:
#             print("Buzz")
#         else: print(i)
#
# print("What is your limit?")
# num = int(input())
# fizzbuzz(num)


#
# def leapyear(year):
#     if (year % 4) == 0:
#         if (year % 100) == 0:
#             if (year % 400) == 0:
#                 print("{0} is a leap year".format(year))
#             else:
#                 print("{0} is not a leap year".format(year))
#         else:
#             print("{0} is a leap year".format(year))
#     else:
#         print("{0} is not a leap year".format(year))
#
#
# print("What is the year?")
# current_year = int(input())
# leapyear(current_year)


# def pallindrome (list1):
#     count = 0
#     for i in list1:
#          if i[0] == i[-1]:
#              count += 1
#     return count
#
# list1 = ["abc", "xyz", "aba", "1221"]
#
# print(pallindrome(list1))
#
# def sumlist(list):
#      new_element = len(list)
#      new_list = list.append(new_element)
#      sum = 0
#      for i in list:
#          sum += i
#      return sum
#
# list_3 = list(range(1, 5))
# print(sumlist(list_3))


