class Student:
    college_name = "ABC college"
    name = "anonymous" #Class attribute
    
    def __init__(self, name, marks):
        self.name = name ##instance attribute
        self.marks = marks # obj attr > class attr
        print("adding new student in Database..")
        
        
s1 = Student("Mishan", 98)
print(s1.name, s1.marks)

s2 = Student("Ghimire", 99)
print(s2.name, s2.marks)

print(Student.college_name)