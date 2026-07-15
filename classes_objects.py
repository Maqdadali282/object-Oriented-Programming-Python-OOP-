# Creating a Class
class Student:

    # Constructor
    def __init__(self, name, age, department):
        self.name = name
        self.age = age
        self.department = department

    # Method to display student information
    def display(self):
        print("Student Information")
        print("Name:", self.name)
        print("Age:", self.age)
        print("Department:", self.department)
        print("---------------------------")


# Creating Objects for the classes
student1 = Student("Ali", 21, "Artificial Intelligence")
student2 = Student("Ahmed", 22, "Computer Science")

# Calling Methods using Objects
student1.display()
student2.display()