from random import choice

class Student:
    def __init__(self,stdudent_names) -> None:
        self.student_names=stdudent_names

    def random_one_student(self):
        one_student=choice(self.student_names)
        return one_student
    
obj=Student(['oybek','azizbek','shahnoza'])
