def computepay(h,r):
    res = h*r
    if h <= 40 :
        return res
    else :
        res = 40*r
        r = r*1.5
        h = h-40
        temp = h*r
        res = res + temp
        return res

hrs = input("Enter hours:")
rate = input("Enter the rate per hour:")
hr = float(hrs)
r = float(rate)
p = computepay(hr,r)
print("Pay",p)
