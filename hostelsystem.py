class Student:
    def __init__(self, student_id, name, room_no):
        self.student_id = student_id
        self.name = name
        self.room_no = room_no

    def display(self):
        print(f"ID: {self.student_id}")
        print(f"Name: {self.name}")
        print(f"Room No: {self.room_no}")
        print("-" * 20)


class Hostel:
    def __init__(self, hostel_name):
        self.hostel_name = hostel_name
        self.students = []

    def add_student(self, student):
        self.students.append(student)
        print(f"{student.name} has been assigned Room {student.room_no}.\n")

    def view_students(self):
        if not self.students:
            print("No students in the hostel.\n")
            return

        print(f"\nStudents in {self.hostel_name}\n")
        for student in self.students:
            student.display()

    def search_student(self, student_id):
        for student in self.students:
            if student.student_id == student_id:
                print("\nStudent Found:")
                student.display()
                return
        print("Student not found.\n")


# ---------------- Main Program ----------------

hostel = Hostel("COMSATS Boys Hostel")

while True:
    print("\n===== Hostel Management System =====")
    print("1. Add Student")
    print("2. View Students")
    print("3. Search Student")
    print("4. Exit")

    choice = input("Enter your choice: ")

    if choice == "1":
        sid = int(input("Student ID: "))
        name = input("Student Name: ")
        room = input("Room Number: ")

        student = Student(sid, name, room)
        hostel.add_student(student)

    elif choice == "2":
        hostel.view_students()

    elif choice == "3":
        sid = int(input("Enter Student ID: "))
        hostel.search_student(sid)

    elif choice == "4":
        print("Thank you!")
        break

    else:
        print("Invalid choice. Try again.")