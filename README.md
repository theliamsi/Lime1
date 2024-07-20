Student Information Management System
Overview:
This project is a comprehensive Student Information Management System designed to read, process, and record information about students. The system allows users to add, delete, find, and view student records. The program ensures that all operations are performed on a dynamically maintained list of student objects and saves any changes back to the file upon exit.

Features:

Add New Student:

Prompt the user for student details (ID, name, department, and GPA).
Create a new student object and add it to the list.

Delete Existing Student:

Allow the user to delete a student by specifying the student ID.
Remove the corresponding student object from the list.

Find Student:

Enable the user to find a student by their ID.
Display the student’s details if found.

View All Students:

Display all student records in a formatted manner.

File Handling:

Prompt the user to enter the name of the file from which to read student information.
Create the file if it doesn’t exist.
Read and process each line of the file to create student objects and populate the list.
Save all changes back to the same file upon exiting the program.

Function Breakdown:

Student Class:
Attributes: student_id, name, department, gpa
Methods: __init__, __str__, and other necessary methods for managing student data.
RecordSystem Class:
Methods:
add_student(student): Adds a new student to the list.
delete_student(student_id): Deletes a student by ID.
find_student(student_id): Finds and returns a student by ID.
view_all_students(): Displays all student records.
load_students(file_name): Reads student information from the specified file.
save_students(file_name): Saves the current list of students back to the file.
Execution Flow:

The program prompts the user to enter the file name.
The file is read line-by-line to create and populate a list of student objects.
The user is prompted to choose an operation: add, delete, find, view, or exit.
The chosen operation is performed on the list of students.
Upon exiting, the list of students is written back to the file, ensuring all changes are saved.
