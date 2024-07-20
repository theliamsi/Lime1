from student import Student, RecordSystem

def main():
    file_name = input("Enter the file name: ")
    rs = RecordSystem(file_name)

    while True:
        choice = input("Choose an operation: v - to view all, a - to add, s - to show one, d - to delete, e - to exit: ").lower()

        if choice == 'a':
            student_info = input("Enter information about the student to add (ID,Name,Dept,GPA): ")
            try:
                id, name, department, gpa = student_info.split(',')
                gpa = float(gpa)
                student = Student(id, name, department, gpa)
                rs.add_student(student)
            except ValueError:
                print("Invalid input. Please enter the information in the correct format (ID,Name,Dept,GPA).")
            except Exception as e:
                print(f"An error occurred: {e}")

        elif choice == 'v':  
            rs.view_students()

        elif choice == 's': 
            id = input("Enter ID of the student to show: ")
            rs.find_student(id)

        elif choice == 'd':  
            id = input("Enter ID of the student to delete: ")
            rs.delete_student(id)

        elif choice == 'e': 
            rs.save()
            break
        else:
            print("Invalid choice.")

if __name__ == "__main__":
    main()