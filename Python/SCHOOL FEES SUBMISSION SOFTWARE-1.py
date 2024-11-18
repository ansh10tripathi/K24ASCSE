class Student:
    def __init__(self, roll_no, name, class_name, fees_paid, total_fees):
        self.roll_no = roll_no
        self.name = name
        self.class_name = class_name
        self.fees_paid = fees_paid
        self.total_fees = total_fees

    def display_student_details(self):
        print(f"Roll No: {self.roll_no}")
        print(f"Name: {self.name}")
        print(f"Class: {self.class_name}")
        print(f"Total Fees: {self.total_fees}")
        print(f"Fees Paid: {self.fees_paid}")
        print(f"Remaining Fees: {self.total_fees - self.fees_paid}")
        print("-" * 30)

class SchoolFeesSubmission:
    def __init__(self, school_name):
        self.school_name = school_name
        self.students = {}

    def add_student(self, student):
        self.students[student.roll_no] = student

    def display_all_students(self):
        print(f"School Name: {self.school_name}")
        print("-" * 30)
        for roll_no, student in self.students.items():
            student.display_student_details()

    def submit_fees(self, roll_no, amount):
        if roll_no in self.students:
            student = self.students[roll_no]
            if amount <= student.total_fees - student.fees_paid:
                student.fees_paid += amount
                print(f"Fees submitted successfully for {student.name}.")
            else:
                print(f"Invalid amount. Cannot submit more than the remaining fees.")
        else:
            print("Student not found.")

# Input student details and fees submission
school_name = "SARASWATI VIDYA MANDIR RAMBAGH BASTI"
fees_submission_system = SchoolFeesSubmission(school_name)

while True:
    print("Options:")
    print("1. Add Student")
    print("2. Display All Students")
    print("3. Submit Fees")
    print("4. Exit")

    choice = input("Enter your choice: ")

    if choice == '1':
        roll_no = int(input("Enter Roll No: "))
        name = input("Enter Student Name: ")
        class_name = input("Enter Class: ")
        fees_paid = int(input("Enter Fees Paid: "))
        total_fees = int(input("Enter Total Fees: "))
        student = Student(roll_no, name, class_name, fees_paid, total_fees)
        fees_submission_system.add_student(student)
        print(f"Student '{name}' added successfully.")
    elif choice == '2':
        fees_submission_system.display_all_students()
    elif choice == '3':
        roll_no = int(input("Enter Roll No of Student: "))
        amount = int(input("Enter Fees Amount to Submit: "))
        fees_submission_system.submit_fees(roll_no, amount)
    elif choice == '4':
        print("Exiting the program.")
        break
    else:
        print("Invalid choice. Please choose a valid option.")
