largest = None
smallest = None
while True:
    num = input("Enter a number: ")
    if num == "done" : break
    try :
        val = float(num)
        if smallest is None :
            smallest = val
        elif val < smallest :
            smallest = val
        if largest is None :
            largest = val
        elif val > largest :
             largest = val
    except :
        print("Invalid input")
print("Maximum is", int(largest))
print("Minimum is", int(smallest))
