fname = input("enter the file name: ")
fhand = open(fname)

count = 0
for word in fhand:
    #checking whether line has more than two elements space seperated
    if word.startswith("From") and len(word.split()) > 2:
        temp = word.split()
        print(temp[1])
        count = count + 1

print("There were", count, "lines in the file with From as the first word")
