count = 0
s = 0

fname = input("enter file name:")
fhand = open(fname)

for line in fhand:
    if not line.startswith("X-DSPAM-Confidence:"):
        continue
    else:
        count = count + 1
        a = line.find("0")
        x = line[a:]
        s = s + float(x)
average = s / count 
print("Average spam confidence:", average)
