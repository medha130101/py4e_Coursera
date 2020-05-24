# Use the file name mbox-short.txt as the file name
fname = input("Enter file name: ")
fh = open(fname)
count = 0
res = 0
for line in fh:
    if not line.startswith("X-DSPAM-Confidence:") : continue
    else :
        count = count+1
        str = line[19:]
        val = float(str)
        res = res + val
print('Average spam confidence:',float(res/count))
