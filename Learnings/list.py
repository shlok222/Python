# 1. Reverse a list without using .reverse() or slicing

list = [1, 2, 3, 4, 5]
list.reverse()
print(list)

# Another Option 

list = [1,2,3,4,5]
i = len(list) - 1   //  We can also add i = 4 since the list is 5 elements long but if we dont know the length of the list we can use len(list) - 1
print(i)

new_list = []

while i >= 0:
    new_list.append(list[i])
    i -= 1
    
print(new_list)