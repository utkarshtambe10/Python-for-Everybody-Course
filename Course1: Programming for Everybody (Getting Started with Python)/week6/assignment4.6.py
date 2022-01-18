def computepay(h, r) :
    if h > 40 :
        p = 40 * r + (h - 40) * r * 1.5
    else :
        p = h * r
    return p

a = input("Enter Hours: ")
hours = float(a)
b = input("Enter Rate: ")
rate = float(b)

pay = computepay(hours, rate)
print("Pay:", pay)
