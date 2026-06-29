name=input("enter name=")
hours_worked=int(input("hours worked="))
hourly_rate=int(input("hourly rate="))
performance_bonus=int(input("performance bonus="))
commission=int(input("commission="))

basic_payment=hours_worked*hourly_rate
gross_payment=basic_payment+performance_bonus
platform_commission=(gross_payment*commission)/100
final_payment=gross_payment-platform_commission
average_earning=final_payment/hours_worked
is_final_payment_above_50000=final_payment>50000
is_hours_above_160=hours_worked>160
is_bonus_greaterthan_commission=performance_bonus>commission
is_final_payment_above_basic_payment=final_payment>=basic_payment
is_commission_lessthan_15=commission<=15

print(f"======payment summary========")
print(f"Freelancer={name}")
print(f"basic payment=₹{basic_payment}")
print(f"gross payment=₹{gross_payment}")
print(f"commission={commission}")
print(f"final payment=₹{final_payment}")
print(f"average per hour=₹{average_earning}")
print(f"final payment>50000={is_final_payment_above_50000}")
print(f"hours worked>160={is_hours_above_160}")
print(f"bonus>commission={is_bonus_greaterthan_commission}")
print(f"final payment>=basic payment={is_final_payment_above_basic_payment}")
print(f"commission<=15={is_commission_lessthan_15}")
