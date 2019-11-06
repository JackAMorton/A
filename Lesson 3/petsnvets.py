class Dog():
    def __init__(self, name, owner, age):
        self.name = name
        self.owner = owner
        self.age = age

    def bark(self):
          print("woof woof woof")

    def eat(self, food):
            print(self.name, "loved the", food, "it tasted pretty bad")

    def sleep(self, hours):
             print(self.name, "slept for", hours, "hours")



class Vet():
    def __init__(self, name, phone, email, location, speciality):
            self.name = name
            self.phone = phone
            self.email = email
            self.location = location
            self.speciality = speciality
    def see_patient(self,Dog):
        print("This is your Vet",self.name,"she specialises in", self.speciality)
        status = input("How's " + Dog.name + ", Healthy or Sick?")
        if status.lower() == "healthy":
            print("Get outta here! Wasting my time!")
        elif status.lower() == "sick":
            print("Nurse come put", Dog.name, "down!")
            next_q = input("Did it die?")
            if next_q.lower() == "no":
             print("INCREASE THE DOSAGE")
            elif next_q.lower() == "yes":
             print("Good job Nurse, NEXT DOG!!!!")
            else: "Please the answer the question correctly"
        else: "What are you about?"


