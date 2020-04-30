students = []

class Student:
    # class attribute
    school_name = "Springfield Elementary"
    # self refers to the instance of the class
    # do not need to pass this self as a parameter when calling the function
    def __init__(self, name, student_id=332):
        self.name = name
        self.student_id = student_id
        students.append(self)

    def __str__(self):
        return "Student: " + self.name

    def get_name_capitalize(self):
        return self.name.capitalize()

    def get_school_name(self):
        return self.school_name

# Inheritance:
class HighSchoolStduent(Student):
    school_name = "Springfield High School"

    #  override!
    def get_school_name(self):
        return "This is a high school student"

    # original value of get name capitalize
    #  super is override while including parent class
    def get_name_capitalize(self):
        original_value = super().get_name_capitalize()
        return original_value + "-HS"

james = HighSchoolStduent("james")
print(james.get_name_capitalize())