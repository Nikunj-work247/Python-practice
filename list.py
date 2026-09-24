my_list = [1,2,"Mango","Orange"]
print(my_list)

my_list2 = list((1,2,3,2,3))
print(my_list2)

my_list[3] = 7
my_list2.append(30)
my_list2.extend([43,23])
my_list.insert(2,"litchi")
my_list.remove("Mango")
print(my_list)
print(my_list2)

my_list2.remove(43)
print(my_list2)

print(my_list2.pop(3))
print(my_list.clear())

my_list3 = [55,22,77,44]
my_list3.sort()
my_list3.sort(reverse =True)
print(my_list3)

# List comprehension 
my_list4 = [n*n for n in range(1,6)]
print(my_list4)