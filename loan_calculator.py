name=input("enter name=")
principal=int(input("principal amount="))
anuual_interest=float(input("annual interest rate="))
time=float(input("time(years)="))
processing_fee=int(input("processing fee="))

simple_interest=(principal*anuual_interest*time)/100
amt_before_fee=principal+anuual_interest
final_amt=amt_before_fee-processing_fee
net_profit=final_amt-principal

print("====Bank Report====")

print(f"customer :{name}")
print(f"principal :{principal}")
print(f"annual interest rate :{anuual_interest}")
print(f"time :{time}")
print(f"processing fee :{processing_fee}")
print(f"simple interest :{simple_interest}")
print(f"amount before fee :{amt_before_fee}")
print(f"final amount :{final_amt}")
print(f"net profit :{net_profit}")
