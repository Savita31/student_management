
import csv
import os

print("Python file location:", os.path.abspath(__file__))
print("CSV file location:", os.path.abspath("students.csv"))


def read_student():
    if not os.path.exists("students.csv"):
        with open("students.csv", "w", newline="") as file:
            writer = csv.DictWriter(
                file,
                fieldnames=["student_id", "name", "course", "email"]
            )
            writer.writeheader()
        return []
    with open("students.csv", "r", newline="") as file:
        reader = csv.DictReader(file)
        students = list(reader)
        return students
# read_student()


def add_student():
    student_id = input("Enter Student ID: ")
    if not student_id.isdigit():
        print("Error: Student ID must contain only numbers!")
        return

    students=read_student()
    for student in students:
        if student["student_id"]==student_id:
            print("error:Student already exist")
            return 
    name = input("Enter Name: ")
    if not name:
        print("Error: Student name cannot be empty!")
        return
    if not any(char.isalpha() for char in name):
        print("Error: Name must contain letters!")
        return

    if not all(char.isalpha() or char.isspace() for char in name):
        print("Error: Name can contain only letters and spaces!")
        return
    course = input("Enter Course: ")
    email = input("Enter Email: ").strip()
    if "@" not in email or "." not in email.split("@")[-1]:
        print("Error: Enter a valid email address!")
        return


    student = {
        "student_id": student_id,
        "name": name,
        "course": course,
        "email": email
    }

    with open("students.csv", "a", newline="") as file:
        writer = csv.DictWriter(
            file,
            fieldnames=["student_id", "name", "course", "email"]
        )
        writer.writerow(student)

    print("Student added successfully!")

    print("Records saved:", read_student())
# add_student()



def search_students():
    search_id=input("enter the student id: ")
    students=read_student()

    for student in students:
        if student["student_id"]==search_id:
            print("student found!")
            print("Student ID:", student["student_id"])
            print("Name:", student["name"])
            print("Course:", student["course"])
            print("Email:", student["email"])
            return
        
    print("Student not found!")
# search_students()


def save_students(students):
    with open("students.csv","w",newline="") as file:
        fieldnames=["student_id", "name", "course", "email"]
        writer=csv.DictWriter(file,fieldnames=fieldnames)
        writer.writeheader()
        writer.writerows(students)
# save_students()
def delete_student():
    delete_id = input("Enter Student ID to delete: ")

    students = read_student()
    updated_students = []
    found = False

    for student in students:
        if student["student_id"] == delete_id:
            found = True
        else:
            updated_students.append(student)

    
    if found:
        confirm = input(
            "Are you sure you want to delete this student? (yes/no): "
        ).strip().lower()

        if confirm == "yes":
            save_students(updated_students)
            print("Student deleted successfully!")
        else:
            print("Deletion cancelled!")
    else:
        print("Student not found!")

# delete_student()


def view_all_students():
    students = read_student()

    if not students:
        print("No student records found!")
        return

    print("\n========== ALL STUDENTS ==========")

    for student in students:
        print("----------------------------------")
        print("Student ID:", student["student_id"])
        print("Name:", student["name"])
        print("Course:", student["course"])
        print("Email:", student["email"])
# view_all_students()
print("==================================")

#### Menu

def main():
    while True:
        print("\n===== STUDENT MANAGEMENT SYSTEM =====")
        print("1. Add Student")
        print("2. Search Student")
        print("3. Delete Student")
        print("4. View All Students")
        print("5. Exit")

        choice = input("Choose an option (1-5): ").strip()

        if choice == "1":
            add_student()

        elif choice == "2":
            search_students()

        elif choice == "3":
            delete_student()

        elif choice == "4":
            view_all_students()

        elif choice == "5":
            print("Exiting Student Management System. Goodbye!")
            break

        else:
            print("Invalid option! Please choose from 1 to 5.")


if __name__ == "__main__":
    main()
