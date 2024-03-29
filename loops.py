# here we add using for loop
exp = [2340,2500,2100,3100,2980]
total = 0
for item in exp:
    total = total+item
print(total)

# the keyword range gives you the range of numbers
for i in range(1,11):
    print(i*i)


# here we add thexpense incuding the month number as well
exp1 = [2340,2500,2100,3100,2980]
for i in range(len(exp1)):
    print("month: ",(i+1),"expense : ", exp1[i])
    total = total + exp1[i]

print("total expense is : ",total)


# here we use break statement
key_location = "chair"
location = ["garage", "living room", "chair","closet"]

for i in location:
    if i == key_location:
        print("key is found in : ",i)
        break
    else:
        print("kry is not found in ", i)


# here we use continue statement
for i in range(1,6):
    if i%2==0:
        continue
    print(i*i)


# use pf while is seen
i=1
while i<=5:
    print(i)
    i = i+1
