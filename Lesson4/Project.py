class Batch():

    def __init__(self, batch_number, stream, start_date, list_of_students,list_of_modules):
        self.batch_number = batch_number
        self.stream = stream
        self.start_date= start_date
        self.list_of_students = list_of_students
        self.list_of_modules = list_of_modules

    def add_batch_trainee (self):
        batch_number = input("What is their Batch Number")
        stream = input("What stream are they on?")


    def List_students (self):
        print(self.batch_number, "Has the students:")
        for i in self.list_of_students:
            print(i.name)

    def list_modules(self):
        print("For",self.stream,",the modules available are:")
        for i in self.list_of_modules:
            print(i.module_name)


class Module():
    def __init__(self,module_name,duration):
        self.duration = duration
        self.module_name = module_name



class Trainer ():
    def __init__(self,trainer_name, stream):
        self.trainer_name = trainer_name
        self.stream = stream

class Trainee (Trainer):
    def __init__(self, name, age, trainee_id, stream, trainer_name):
        super().__init__(stream, trainer_name)
        self.name = name
        self.age = age
        self.trainee_id = trainee_id


def add_trainee ():
     name = input("What is the student's name?")
     age = input("How old are they?")
     trainee_id = input("What ID would you like them to have?")
     stream = input("What stream are they one?")
     trainer_name = input("What is their trainer's name?")
     new_trainee =  Trainee(name,age,trainee_id,stream,trainer_name)
     return new_trainee


Will = Trainee("Will","26",1,"data","Isabella")
Beth = Trainee("Beth","21",2,"data","Isabella")
Jack = Trainee("Jack","25",3,"data", "Isabella")

Python = Module("Python",4)
Tableau = Module("Tableau",1)
Excel = Module("Excel",1)
Business = Module("Business",1)
Modules = [Python,Tableau,Excel,Business]

Data_5 = Batch("Data_5","data","30-09-2019",[Jack,Will,Beth],[Python,Tableau,Excel,Business])

Isabella = Trainer("Isabella","data")

