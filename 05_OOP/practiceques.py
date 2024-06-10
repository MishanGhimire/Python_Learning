##Create a student class that takes name & marks of 3 subjects as argument in constructor.The create a method to print the average.
class Student:
    def __init__(self, name, marks):
        self.name = name
        self.marks = marks
        
    def get_avg(self):
        sum = 0
        for val in self.marks:
            sum += val
        print("hi", self.name, "Your avg score is:", sum/3)
        
s1 = Student("Tony Stark", [99, 98, 97])
s1.get_avg()