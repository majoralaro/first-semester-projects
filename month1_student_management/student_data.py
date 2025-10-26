students = []

def add_student():
    name = input("Enter student name: ")
    age = int(input("Enter student age: "))
    grade = float(input("Enter student grade: "))

    student = {
        "name": name,
        "age": age,
        "grade": grade
    }

    students.append(student);
    

def view_students():
    if not students:
        print("\n📭 No students found.\n")
        return

    print("\n🎓 Student List:")
    for i, student in enumerate(students, start=1):
        print(f"{i}. Name: {student['name']}, Age: {student['age']}, Grade: {student['grade']}")
    print();
    

def get_average_grade():
    if not students:
        print("\n⚠️ No student data available to calculate average.\n")
        return

    total = sum(student["grade"] for student in students)
    average = total / len(students)
    #print(f"\n Average Grade: {average:.2f}\n")
    return average;
    