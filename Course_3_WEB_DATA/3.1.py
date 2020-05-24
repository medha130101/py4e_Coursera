import re
fhand = open("file1.txt")
lst = list()
temp =list()
sum =0
for line in fhand :
    line.rstrip()
    lst = re.findall('[0-9]+',line)
    for curr in lst :
        val = int(curr)
        sum = sum+val
#print(temp)
print(sum)
