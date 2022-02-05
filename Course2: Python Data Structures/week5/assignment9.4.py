fname = input("enter the file name: ")
fhand = open(fname)

check = dict()
for line in fhand:
    if not line.startswith("From "):
        continue
    word = line.split()
    check[word[1]] = check.get(word[1], 0) + 1

maxword = None
maxcount = -1  #'OR' maxcount = None
for word, count in check.items():
    if count > maxcount:  #'OR' maxcount is None or count > maxcount:
        maxword = word
        maxcount = count
print(maxword, maxcount)
