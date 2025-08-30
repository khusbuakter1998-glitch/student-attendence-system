# Student Attendance System

# --- attendance.py ---
def mark_attendance(student_name):
    print(f"Attendance marked for {student_name}")


# --- main.py ---
def main():
    print("Welcome to Student Attendance System")
    
    students = []
    while True:
        print("\nOptions:")
        print("1. Add student")
        print("2. Mark attendance")
        print("3. Show students")
        print("4. Exit")
        
        choice = input("Enter choice: ")
        
        if choice == "1":
            name = input("Enter student name: ")
            students.append(name)
            print(f"{name} added.")
        elif choice == "2":
            if not students:
                print("No students added yet!")
                continue
            name = input("Enter student name to mark attendance: ")
            if name in students:
                mark_attendance(name)
            else:
                print("Student not found.")
        elif choice == "3":
            print("Students list:")
            for s in students:
                print("-", s)
        elif choice == "4":
            print("Exiting...")
            break
        else:
            print("Invalid choice. Try again.")

if __name__ == "__main__":
    main()


# --- README.md ---
"""
Student Attendance System
This is a simple student attendance system project.
- Add students
- Mark attendance
- Show students list
"""
