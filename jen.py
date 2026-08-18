# ============================================
#        STUDENT MANAGEMENT SYSTEM
#        DEFAULT INPUT VERSION
# ============================================

class Student:

    def __init__(self, student_id, name, age, course, marks):
        self.student_id = student_id
        self.name = name
        self.age = age
        self.course = course
        self.marks = marks

    def total(self):
        return sum(self.marks)

    def average(self):
        return self.total() / len(self.marks)

    def grade(self):
        avg = self.average()

        if avg >= 90:
            return "A+"
        elif avg >= 80:
            return "A"
        elif avg >= 70:
            return "B"
        elif avg >= 60:
            return "C"
        elif avg >= 50:
            return "D"
        else:
            return "F"

    def result(self):
        if self.average() >= 40:
            return "PASS"
        else:
            return "FAIL"

    def display(self):
        print("\n-------------------------------")
        print("Student ID :", self.student_id)
        print("Name       :", self.name)
        print("Age        :", self.age)
        print("Course     :", self.course)
        print("Marks      :", self.marks)
        print("Total      :", self.total())
        print("Average    :", self.average())
        print("Grade      :", self.grade())
        print("Result     :", self.result())
        print("-------------------------------")


# ============================================
# DEFAULT STUDENT DATA
# ============================================

students = {}

students["101"] = Student(
    "101",
    "Akhil",
    22,
    "DevOps",
    [85, 90, 78, 88, 92]
)

students["102"] = Student(
    "102",
    "Rahul",
    23,
    "Python",
    [70, 65, 75, 80, 72]
)

students["103"] = Student(
    "103",
    "Kiran",
    21,
    "Java",
    [35, 42, 38, 40, 30]
)


# ============================================
# DISPLAY ALL STUDENTS
# ============================================

def display_all_students():

    print("\n===== ALL STUDENTS =====")

    for student in students.values():
        student.display()


# ============================================
# FIND TOPPER
# ============================================

def find_topper():

    print("\n===== TOPPER =====")

    topper = None

    for student in students.values():

        if topper is None:
            topper = student

        elif student.average() > topper.average():
            topper = student

    print("\nTopper Details:")
    topper.display()


# ============================================
# PASS STUDENTS
# ============================================

def display_pass_students():

    print("\n===== PASS STUDENTS =====")

    for student in students.values():

        if student.result() == "PASS":
            student.display()


# ============================================
# FAIL STUDENTS
# ============================================

def display_fail_students():

    print("\n===== FAIL STUDENTS =====")

    for student in students.values():

        if student.result() == "FAIL":
            student.display()


# ============================================
# STATISTICS
# ============================================

def statistics():

    print("\n===== STATISTICS =====")

    total_students = len(students)

    passed = 0
    failed = 0
    total_average = 0

    highest_average = 0
    lowest_average = 100

    for student in students.values():

        avg = student.average()

        total_average += avg

        if student.result() == "PASS":
            passed += 1
        else:
            failed += 1

        if avg > highest_average:
            highest_average = avg

        if avg < lowest_average:
            lowest_average = avg

    overall_average = total_average / total_students

    print("Total Students :", total_students)
    print("Passed         :", passed)
    print("Failed         :", failed)
    print("Overall Average:", round(overall_average, 2))
    print("Highest Average:", highest_average)
    print("Lowest Average :", lowest_average)


# ============================================
# MAIN PROGRAM
# ============================================

print("======================================")
print("       STUDENT MANAGEMENT SYSTEM")
print("======================================")

display_all_students()

find_topper()

display_pass_students()

display_fail_students()

statistics()

print("\n======================================")
print("       PROGRAM EXECUTED SUCCESSFULLY")
print("======================================")
