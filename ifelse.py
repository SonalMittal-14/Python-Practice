num = input("enter a number : ")
num = int(num) #num will be integer

if num %2 == 0:
    print("number is even")
else:
    print("number is odd")


indian = ["samosa", "daal", "naan"]
chinese = ["egg role", "fried rice","chowmin"]
italian = ["pizza","pasta", "risotto"]

dish = input("enter a dish name : ")

if dish in indian:
    print("indian")
elif dish in chinese:
    print("chinese")
elif dish in italian:
    print("italian")
else:
    print("i don't know dish",dish)
    
