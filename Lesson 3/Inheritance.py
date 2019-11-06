from Abstraction import *

class reptile(Animal):

    def __init__(self):
        super().__init__()
        self.cold_blooded = True
        self.tetrapod = None
        self.heartchambers = [3,4]
        self.amniotic_eggs = None

    def seek_heart(self):
            print("I'm one cold lizard")
    def hunt(self):
            print("Going to kill some bugs or something")
    def use_venom(self):
            print("*Spit*")
    def scream(self):
            print("AAAAHHHHHHHHHHHHHH")

xBadLizard9x = reptile()
print(xBadLizard9x.eat("soup")),xBadLizard9x.use_venom(),xBadLizard9x.hunt(),
print("I have",xBadLizard9x.heartchambers[1], "heart chambers"),
xBadLizard9x.scream(), print(xBadLizard9x.Tweet("BigLizardBoi"))
