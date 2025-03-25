hours = input("Hours: ")
try:
    hours = float(hours)
except ValueError:
    print("Error, please enter numeric input")
    hours = 0
rate = 10
if hours > 40:
    pay = hours * (rate * 1.5)
else:
    pay = hours * rate
print(pay)