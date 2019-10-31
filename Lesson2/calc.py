def add(in1, in2):
    return in1 + in2

def mult(in1, in2):
    return in1*in2

def sub(in1,in2):
    return in1-in2

def div(in1,in2):
    return in1/in2

print("What is the first number you would like to use?")
number1 = int(input())
print("What is the second number you would like to use?")
number2 = int(input())
print("These numbers added together are: ",add(number1, number2))
print("These numbers multiplied together are: ",mult(number1,number2))
print("These numbers subtracted are: ", sub(number1, number2))
print("These numbers divided are: ", div(number1,number2))


