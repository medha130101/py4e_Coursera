fname = input("Enter file name: ")
fh = open(fname)
lst = list()
for line in fh:
    temp  = line.rstrip()
    res  = temp.split()
    for resword in res :
        if not resword in lst :
            lst.append(resword)
fin = lst.sort()
print(lst)
