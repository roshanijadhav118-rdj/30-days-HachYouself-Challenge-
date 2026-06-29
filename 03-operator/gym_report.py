name=input("enter name =")
membership_fee=int(input("membership fee="))
personal_training_fee=int(input("personal training fee="))
protein_supplement_cost=int(input("protein cost ="))
discount_percentage=int(input("discount percentage="))
days_attended=int(input("days attended="))
total_day_in_month=int(input("total days in month="))

total_bill=membership_fee+personal_training_fee+protein_supplement_cost
discount_amount=(total_bill*discount_percentage)/100
final_amount=total_bill-discount_amount
attendence_percentage=(days_attended/total_day_in_month)*100
daily_spending=final_amount/days_attended
is_attendence_greaterthan_80=attendence_percentage>=80
is_final_amount_greater_5000=final_amount>5000
is_discount_greater_1000=discount_amount>=1000
is_training_greater_supplement=personal_training_fee>protein_supplement_cost
is_membership_greater_finalamount=membership_fee>=final_amount

print(f"===========GYM Report==========")
print(f"member={name}")
print(f"bill=₹{total_bill}")
print(f"discount amount=₹{discount_amount}")
print(f"final bill with discount=₹{final_amount}")
print(f"attendence ={attendence_percentage}%")
print(f"average daily spendig={daily_spending}")
print(f"attendence_percentage>=80={is_attendence_greaterthan_80}")
print(f"final_amount>5000={is_final_amount_greater_5000}")
print(f"discount_amount>=1000={is_discount_greater_1000}")
print(f"personal_training_fee>protein_supplement_cost={is_training_greater_supplement}")
print(f"membership_fee>=final_amount={is_membership_greater_finalamount}")
