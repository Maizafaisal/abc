class Student:
    def __init__(self, name, age, grade):
        self.name = name
        self.age = age
        self.grade = grade

    def display_details(self):
        print(f"Name: {self.name}")
        print(f"Age: {self.age}")
        print(f"Grade: {self.grade}")


class Teacher:
    def __init__(self, name, subject):
        self.name = name
        self.subject = subject

    def display_details(self):
        print(f"Name: {self.name}")
        print(f"Subject: {self.subject}")


class Course:
    def __init__(self, name, teacher):
        self.name = name
        self.teacher = teacher

    def display_details(self):
        print(f"Course Name: {self.name}")
        print(f"Teacher: {self.teacher.name}")


class School:
    def __init__(self):
        self.students = []
        self.teachers = []
        self.courses = []

    def add_student(self, name, age, grade):
        self.students.append(Student(name, age, grade))

    def add_teacher(self, name, subject):
        self.teachers.append(Teacher(name, subject))

    def add_course(self, name, teacher):
        self.courses.append(Course(name, teacher))

    def display_students(self):
        for student in self.students:
            student.display_details()
            print("--------------------")

    def display_teachers(self):
        for teacher in self.teachers:
            teacher.display_details()
            print("--------------------")

    def display_courses(self):
        for course in self.courses:
            course.display_details()
            print("--------------------")


def main():
    school = School()

    while True:
        print("School Management System")
        print("1.	Add Student")
        print("2.	Add Teacher")
        print("3.	Add Course")
        print("4.	Display Students")
        print("5.	Display Teachers")
        print("6.	Display Courses")
        print("7.	Exit")

        choice = input("Enter your choice: ")

        if choice == "1":
            name = input("Enter student name: ")
            age = input("Enter student age: ")
            grade = input("Enter student grade: ")
            school.add_student(name, age, grade)
        elif choice == "2":
            name = input("Enter teacher name: ")
            subject = input("Enter teacher subject: ")
            school.add_teacher(name, subject)
        elif choice == "3":
            name = input("Enter course name: ")
            teacher_name = input("Enter teacher name: ")
            teacher = next((t for t in school.teachers if t.name == teacher_name), None)
            if teacher:
                school.add_course(name, teacher)
            else:
                print("Teacher not found.")
        elif choice == "4":
            school.display_students()
        elif choice == "5":
            school.display_teachers()
        elif choice == "6":
            school.display_courses()
        elif choice == "7":
            break
        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
      main()

