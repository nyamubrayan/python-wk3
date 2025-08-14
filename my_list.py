my_list = [] #creating an empty list

#appnding the following elements to my_list: 10,20,30,40,
my_list.append(10)
my_list.append(20)
my_list.append(30)
my_list.append(40)

my_list.insert(1,15) #insering 15 at the second position

my_list.extend([50, 60,70])  # extending the list with following elements: 50, 60, 70

my_list.pop() #removing the last element

my_list.sort() #sorting in ascending order

index_30 = my_list.index(30) #finding the index of element 30
print("Index of 30:", index_30)

print("Final list:", my_list)