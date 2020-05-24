hrs = input("Enter Hours:")
h = float(hrs)
rate = input("Enter the rate:")
r = float(rate)
res = h*r
if h <= 40 :
    print(res)
else :
    res = 40*r
    r = r*1.5
    h = h-40
    temp = h*r
    res = res + temp
    print(res)
