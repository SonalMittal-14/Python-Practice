# you are given two lists of numbers and you need to find total of each of these list


# function body
def cal_total(exp): #exp -> function argument
    total = 0
    for item in exp:
        total = total+item
    return total # total -> return value



list1 = [2100,3400,3500]
list2 = [200,500,700]

list1_total = cal_total(list1)
list2_total = cal_total(list2)

print("list1 total : ",list1_total)
print("list2 total : ",list2_total)


# sum of two numbers
def sum(a,b):
    total = a+b
    return total

n = sum(2,3)
print("total : ",n)


