# Student Management System

## About the Project
The Student Management System is a Python console-based application that helps manage student records using CSV file storage. Users can add, search, delete, and view student records through an interactive menu.

## Features
- Add new student records
- Search students by student ID
- Delete student records
- View all student records
- Validate numeric and unique student IDs
- Validate student names and email formats
- Store student data in a CSV file
- Interactive menu-driven interface

## Technologies Used
- Python 3
- CSV module
- OS module

## Project Structure
```text
student-management-system/
├── student_manager.py
├── students.csv
└── README.md
```

## Requirements
- Python 3 installed
- Visual Studio Code or another Python editor

No external libraries are required.

## How to Run

1. Open the project folder in Visual Studio Code.
2. Open the terminal in the project directory.
3. Run the following command:

```bash
python student_manager.py
```

4. Choose an option from the menu:

```text
===== STUDENT MANAGEMENT SYSTEM =====
1. Add Student
2. Search Student
3. Delete Student
4. View All Students
5. Exit
```

## CSV Data Storage
Student records are stored in `students.csv` using these columns:

| Column | Description |
|---|---|
| `student_id` | Unique numeric student ID |
| `name` | Student name |
| `course` | Student's course |
| `email` | Student's email address |

The records remain saved in the CSV file after the program exits.

## Input Validation
- Student ID must contain numbers only.
- Duplicate student IDs are not allowed.
- Student name cannot be empty.
- Student name must contain letters and spaces only.
- Email must contain `@` and a dot in the domain portion.

*Note: Email validation is basic and does not verify whether an email address actually exists.*

## Learning Outcomes
This project demonstrates practical use of:
- Python functions
- Lists and dictionaries
- Loops and conditional statements
- CSV file handling
- File operations
- Input validation
- Menu-driven programming

## Author
**Savita Swami**
