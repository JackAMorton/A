import time
import random

min =1yes
max =6

roll_again = "no"
print("Welcome to the 'Die Roller'. The most exciting game in existence. All you need to do is roll a 6")
time.sleep(4)
print("Are you ready for the experience of a lifetime?")
answer = input()
if answer == "yes" : roll_again = "yes"
else: print("Ok.")

while roll_again == "yes" or roll_again == "y":
    print("Rolling that die!")
    print("The result is...........")
    result = random.randint(min, max)
    time.sleep(4)
    print(result)
    if result == 6:
        print("You're the Winner!")
    elif result == 1:
        print("That was awful!")
    elif result == 5:
        print("That was close but still not great")
    else:print("You're pretty bad at rolling the die, I'm devastated")


    roll_again = input("Roll the die again?")


