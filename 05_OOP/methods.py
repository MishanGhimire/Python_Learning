class Student:
    def __init__(self, name, marks):
        self.name = name
        self.marks = marks
        
    def welcome(self):
        print("Welcome students,", self.name)
        
    def get_marks(self):
        return self.marks
    
s1 = Student("Mishan",20)
s1.welcome()
print(s1.get_marks())