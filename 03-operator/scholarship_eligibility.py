name=input("Enter Name=")

physics=int(input("Enter physics marks="))
chemistry=int(input("Enter chemistry marks="))
maths=int(input("Enter maths marks="))
attendence=int(input("Enter attendence percentage="))

Total_marks=physics+chemistry+maths
avg_percentage=(physics+chemistry+maths)/3

eligibility=(avg_percentage>=75 and attendence>=80)

print(f"total marks ={Total_marks}")
print(f"average percentage={avg_percentage}")
print(f"eligible={eligibility}")

