# sears.py
bill_thickness = 0.11/10/100 # 0.11 mm converted to meters
sears_height = 442
num_bills = 1 
day = 1

while num_bills*bill_thickness < sears_height:
    print(day, num_bills, num_bills*bill_thickness)
    day = day + 1
    num_bills = num_bills * 2

print('Number of bills:', num_bills)
print('Number of days:', day)
print('Final height: ', num_bills*bill_thickness)
