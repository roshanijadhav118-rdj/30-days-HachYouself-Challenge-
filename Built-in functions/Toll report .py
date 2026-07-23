vehicle_numbers = ["MH12AB1234", "KA01XY5678", "DL10PQ1111", "MH14CD2222"]

toll_paid = [120, 90, 150, 110]

report = list(zip(vehicle_numbers, toll_paid))

print("Vehicle Toll Report")

for i, data in enumerate(report, start=1):
    print(i, data[0], "-", data[1])

highest = max(report, key=lambda x: x[1])

print("Highest Toll:")
print(highest[0], "-", highest[1])

sorted_report = sorted(report, key=lambda x: x[1], reverse=True)

print("Sorted Report:")

for data in sorted_report:
    print(data[0], "-", data[1])
