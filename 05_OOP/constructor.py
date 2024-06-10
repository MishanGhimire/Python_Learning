class Student:
    # default constructors
    def __int__(self):
        print("adding new student in Database..")
        
    #Paramaterized constructors
    def __init__(self, name, marks):
        self.name = name
        self.marks = marks
        print("adding new student in Database..")
        
        
s1 = Student("Mishan", 98)
print(s1.name, s1.marks)

s2 = Student("Ghimire", 99)
print(s2.name, s2.marks)