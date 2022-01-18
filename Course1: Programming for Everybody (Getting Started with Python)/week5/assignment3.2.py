a = input("Enter Hours: ")
b = input("Enter Rate: ")
try :
    hours = float(a)
    rate = float(b)
except :
    print("Enter numeric value of hours and rate")
    quit()

#pay calculation
if hours <= 40 :
    pay = hours * rate
elif hours > 40 :
    pay = 40 * rate + (hours - 40) * rate * 1.5
print("Pay is:", pay)
