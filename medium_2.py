name=input("Enter Name=")

marks1=int(input("Enter maths marks="))
marks2=int(input("Enter science marks="))
marks3=int(input("Enter english marks="))
marks4=int(input("Enter computer marks="))
marks5=int(input("Enter social marks="))

Total_marks=marks1+marks2+marks3+marks4+marks5

print(f"Total marks = {Total_marks}")

percentage=float(int(Total_marks)*100/500)

print(f"percentage= {percentage}")