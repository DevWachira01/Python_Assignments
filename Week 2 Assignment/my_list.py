my_list=[] #creates an empty list 
print(my_list)

#appending values to my_list
my_list.append(10)
my_list.append(20)
my_list.append(30)
my_list.append(40)
print(my_list)

#inserting the value 15 into index 1(second position)
my_list.insert(1,15)
print(my_list)

#extending list
newlist=[50,60,70]
my_list.extend(newlist)

print(my_list)

#remove the last item from the list
my_list.pop()
print(my_list)

#Sort my_list in ascending order
my_list.sort()
print(my_list)

#Find and print the index of the value 30 in my_list

index= my_list.index(30)
print(index)


