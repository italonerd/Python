grocery_lists = ['Juice', 'Tomatoes','Bananas']
print grocery_lists[0]

grocery_lists[0] = 'Green Juice'
print("First Item", grocery_lists[0])
print(grocery_lists[0:2])

other_things = ["Wash car","Pick up kids","Car check"]

to_do_list = [other_things, grocery_lists]

print to_do_list 
print ((to_do_list[1][1]))

grocery_lists.append("Chicken")
print to_do_list

grocery_lists.insert(1, "Pickle")
grocery_lists.remove("Tomatoes")
print grocery_lists
grocery_lists.sort()
print grocery_lists

to_do_list.reverse()
print to_do_list

del grocery_lists[0]
print to_do_list

to_do_list2 = other_things + grocery_lists
print len(to_do_list2)
print max(to_do_list2)
print min(to_do_list2)

int_list = [1,2,3,4,5,6]
print("max %s min %s" % (max(int_list) , min(int_list)) ) 
