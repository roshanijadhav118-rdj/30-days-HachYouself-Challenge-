length=input("Enter length=")
width=input("Enter width=")
cost_per_sqm=input("Enter cost per sq. meter=")

length=float(length)
width=float(width)
cost_per_sqm=float(cost_per_sqm)

area=length*width
total_cost=area*cost_per_sqm

print(f"Area = {area} sq.m")
print(f"Total cost={total_cost}")



