fname = input("enter the file name: ")
fhand = open(fname)

count = dict()
for line in fhand:
    if not line.startswith("From "):  #selecting lines with 'From'
        continue
    word = line.split()
    hr = word[5].split(":")  #selecting hour (5th index) and splitting string with colon
    count[hr[0]] = count.get(hr[0], 0) + 1
    
check = list()
for key, value in count.items():
    tup = (key, value)
    check.append(tup)  #adding tuples to the list

check = sorted(check)  #sorting list according to hour
for key, value in check:
    print(key, value)  #printing (hour, times) in pair
