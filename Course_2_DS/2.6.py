fname = input("Enter file name: ")
fh = open(fname)
counts = dict()
count = 0
for line in fh :
    if line.startswith('From ') :
        temp = line.split()
        str = temp[1]
        counts[str] = counts.get(str,0) + 1
bigword = None
bigcount = None
for key,value in counts.items():
    if bigcount is None :
        bigcount = value
    elif bigcount < value :
        bigcount = value
        bigword = key
print(bigword,bigcount)
#print(counts)
#print("There were", count, "lines in the file with From as the first word")
