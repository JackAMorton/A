# ABSTRACTION: MEANS HIDING THE COMPLEXITY AND SHOWING THE
# ESSENTIAL FEATURES OF THE OBJECT:

# INHERITANCE: ALLOWS US TO DEFINE A CLASS THAT INHERITS
# ALL THE METHODS AND PROPERTIES FROM A PARENT CLASS

#ENCAPSULATION IS THE INTERNAL REPRESENTATION OF AN OBJECT THAT WILL
# NOT BE SHOWN TO THE USER

# POLYMORPHISM REFERS TO THE ABILITY OF AN OBJECT TO ADAPT THE CODE

class Animal():

    def __init__(self):
        self.alive = True
        self.spine = True
        self.eyes = True
        self.lungs = True


    def eat(self,food):
        return "I ate " + food + " ,it was disgusting"
    def sleep (self):
        return "ZZzzzzzzz *drooling*"
    def breathe(self):
        return("Huffin")
    def Tweet(self,twitter_handle):
        return("Hey guys please follow me @" + twitter_handle)

