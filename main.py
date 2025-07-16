from student import Student
from utils import load_students, save_students, catch_errors
import random

students = load_students()

def generate_id():
    return "S" + str(random.randint(1000, 9999))

@catch_errors
def add_student():
    name = input("Enter student name: ")
    dob = input("Enter date of birth (YYYY-MM-DD): ")
    print("Enter marks out of 100:")
    math = int(input("Math: "))
    sci = int(input("Science: "))
    eng = int(input("English: "))
    marks = {"math": math, "science": sci, "english": eng}
    sid = generate_id()

    student = Student(name, dob, marks, sid)
    students.append(student.to_dict())
    print(f"Student {name} added successfully with ID: {sid}")

@catch_errors
def view_students():
    if not students:
        print("No students found.")
        return
    for s in students:
        print(f"{s['id']} - {s['name']} - Avg: {s['average']} - Grade: {s['grade']}")

@catch_errors
def search_student():
    query = input("Enter student name or ID to search: ").lower()
    found = False
    for s in students:
        if query in s['name'].lower() or query in s['id'].lower():
            print(s)
            found = True
    if not found:
        print("Student not found.")

@catch_errors
def delete_student():
    sid = input("Enter student ID to delete: ")
    global students
    before = len(students)
    students = [s for s in students if s['id'] != sid]
    after = len(students)
    if before == after:
        print("No student deleted. ID not found.")
    else:
        print("Student deleted successfully.")

@catch_errors
def analytics():
    if not students:
        print("No student data to analyze.")
        return
    topper = max(students, key=lambda x: x['total'])
    print(f"Topper: {topper['name']} - {topper['total']} marks")
    avg_all = sum(s['average'] for s in students) / len(students)
    print(f"Overall Class Average: {avg_all:.2f}")

def menu():
    while True:
        print("\n=== Smart Student Management System ===")
        print("1. Add Student")
        print("2. View Students")
        print("3. Search Student")
        print("4. Delete Student")
        print("5. Analytics")
        print("6. Save & Exit")
        choice = input("Enter your choice (1–6): ")

        if choice == '1':
            add_student()
        elif choice == '2':
            view_students()
        elif choice == '3':
            search_student()
        elif choice == '4':
            delete_student()
        elif choice == '5':
            analytics()
        elif choice == '6':
            save_students(students)
            print("Data saved. Goodbye!")
            break
        else:
            print("Invalid choice. Try again.")

if __name__ == "__main__":
    menu()
