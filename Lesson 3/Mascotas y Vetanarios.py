class Dog():
        def __init__(self,name,owner,age):
         self.name = name
         self.owner = owner
         self.age = age

         def bark (self):
             print("woof woof woof")

         def eat (self, food):
             print(self.name, "loved the ", food, " it tasted pretty bad")

         def sleep (self,hours):
             print(self.name, "slept for",hours,"hours")


