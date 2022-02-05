fname = input("enter file name: ")
fhand = open(fname)

for line in fhand:
    line1 = line.rstrip()

ans = line1.upper()
print(ans)
