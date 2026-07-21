
def search_student(students):
    roll = int(input("Enter Roll Number to Search: "))

    if roll in students:
        print("\nStudent Details")
        print("Roll Number:", roll)
        print("Name:", students[roll]["Name"])
        print("Marks:", students[roll]["Marks"])
        print("Total:", students[roll]["Total"])
        print("Percentage:", students[roll]["Percentage"])
        print("Grade:", students[roll]["Grade"])
    else:
        print("Student not found.")


students = {}

n = int(input("How many students do you want to add? "))

for i in range(n):
    add_student(students)

search_student(students)
