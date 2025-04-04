items = ["bread","pasta","fruits","veggies"]
print(items)
print(items[1])
items[0] = "chips"
print(items) #we can change an elemnt in list

print(items[0:2])

# printing the last element from the list
print(items[-1])

# adding an item at the end of the list
items.append("butter")
print(items)

# inserting an item in the list 
items.insert(1,"sauce")
print(items)


# concatenating two list
food = ["bread","pasta","fruits"]
bathroom = ["shampoo","soap"]
items = food + bathroom

print(items)

# checking length of list
print(len(items))

# checkig wheather these two elements are present in list or not
print("bread" in items)

print("soda" in items)



