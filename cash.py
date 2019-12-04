change = [0, 0, 20, 5]
due = 0.75
quarter = change[0] * 0.25
dime = change[1] * 0.10
nickel = change[2] * 0.05
penny = change[3] * 0.01
total_sum = quarter + dime + nickel + penny
if total_sum >= due:
    print("true")
else:
    print("false")