name=input("enter name=")
previous_reading=int(input("previuos reading="))
current_reading=int(input("current reading="))

units_consumed=current_reading-previous_reading
cost_per_unit=float(input("cost per unit="))

total_bill=units_consumed*cost_per_unit
is_bill_above_2000=total_bill>2000
is_units_above_500=units_consumed>500

print("=====elecricity bill======")

print(f"customer={name}")
print(f"previous meter reading={previous_reading}")
print(f"current meter reading={current_reading}")
print(f"units consumed={units_consumed}")
print(f"cost per units=₹{cost_per_unit}")
print(f"total bill=₹{total_bill}")
print(f"bill>2000={is_bill_above_2000}")
print(f"unis>500={is_units_above_500}")
print(f"average cost per unit=₹{cost_per_unit}.")
