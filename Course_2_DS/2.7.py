fname = input("Enter file name: ")
fh = open(fname)
counts = dict()
count = 0
for line in fh :
    if line.startswith('From ') :
        temp = line.split()
        str = temp[5]
        time = str.split(':')
        val = time[0]
        counts[val] = counts.get(val,0) + 1
print(counts)
t = sorted(counts.items())
for k,v in t :
    print(k,v)
