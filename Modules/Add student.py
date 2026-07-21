
def add_student(students):
    roll = int(input("Enter Roll Number: "))
    name = input("Enter Name: ")

    marks = []
    for i in range(5):
        mark = int(input(f"Enter marks of Subject {i+1}: "))
        marks.append(mark)

    total = sum(marks)
    percentage = total / 5
    grade = calculate_grade(percentage)

    students[roll] = {
        "Name": name,
        "Marks": marks,
        "Total": total,
        "Percentage": percentage,
        "Grade": grade
    }

    print("Student added successfully.\n")


