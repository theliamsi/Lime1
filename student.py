class Student:
    def __init__(self, id, name, department, gpa):
        self.id = id
        self.name = name
        self.department = department
        self.gpa = gpa
    
    def display_info(self):
        print(f"ID: {self.id} Name: {self.name} Department: {self.department} GPA: {self.gpa}")

import os

class RecordSystem:
    def __init__(self, file_name):
        self.file_name = file_name
        self.students = []
        self.load_records()

    def load_records(self):
        if not os.path.exists(self.file_name):
            print("The file doesn't exist. Creating a new file.")
            open(self.file_name, 'w').close()
        else:
            with open(self.file_name, 'r') as file:
                for line in file:
                    id, name, department, gpa = line.strip().split(',')
                    self.students.append(Student(id, name, department, float(gpa)))

    def add_student(self, student):
        if any(s.id == student.id for s in self.students):
            print("Student with this ID already exists.")
        else:
            self.students.append(student)
            print(f"Student {student.name} added.")

    def view_students(self):
        if not self.students:
            print("No students to display.")
        for student in self.students:
            student.display_info()

    def find_student(self, id):
        found = False
        for student in self.students:
            if student.id == id:
                student.display_info()
                found = True
                break
        if not found:
            print("Student not found.")

    def delete_student(self, id):
        for i, student in enumerate(self.students):
            if student.id == id:
                del self.students[i]
                print(f"Student with ID {id} deleted.")
                return
        print("Student not found.")

    def save(self):
        with open(self.file_name, 'w') as file:
            for student in self.students:
                file.write(f"{student.id},{student.name},{student.department},{student.gpa}\n")
        print("Information saved to the file.")