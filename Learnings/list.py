# 1. Reverse a list without using .reverse() or slicing

# list = [1, 2, 3, 4, 5]
# list.reverse()
# print(list)

# # Another Option 

# list = [1,2,3,4,5]
# i = len(list) - 1   //  We can also add i = 4 since the list is 5 elements long but if we dont know the length of the list we can use len(list) - 1
# print(i)

# new_list = []

# while i >= 0:
#     new_list.append(list[i])
#     i -= 1
    
# print(new_list)

# 2. Find the largest and smallest number in a list without using max() or min()

# list = [20,19,30,55,762]

# minimum = list[0]
# maximum = 0 

# for i in range(len(list)):
#     if list[i] < minimum:
#         minimum = list[i]
#     elif list[i] > maximum:
#         maximum = list[i]

# print(minimum)
# print(maximum)

# 3. Count how many times each element appears in a list

# nums = [1, 2, 2, 3, 1, 4]
# visited = []

# for i in nums:
#     if i not in visited:
#         c = 0
#         for j in nums:
#             if i == j:
#                 c += 1
#         print(i, "->", c)
#         visited.append(i)

#  Another Easy way 

# nums = [1, 2, 2, 3, 1, 4]
# count = {}

# for i in nums:
#     if i in count:
#         count[i] += 1
#     else:
#         count[i] = 1

# print(count)

# 4. Remove duplicate elements from a list (keep original order)

# list = [1, 2, 2, 3, 1, 4]
# result = set(list)

# print(list(result))  # Converted Again to List and Printed


# 5. Calculate the sum of all elements in a list
# list = [1,4,7,2,9]
# sum  = 0

# for i in list:
#     sum += i
    
# print(sum)

# 6. Count the number of even and odd numbers in a list
# list = [1,4,7,2,9]
# Even = 0
# Odd = 0

# for i in list:
#     if i % 2 == 0:
#         Even += 1
#     else:
#         Odd += 1
            
# print(Even)
# print(Odd)

# 7. Reverse a list without using .reverse() or slicing
# list = [1,4,7,2,9]
# new_list = len(list)

# for i in range(new_list -1,-1,-1):
#     print(list[i])

# 8. Remove duplicate elements from a list (keep original order)
# list = [1,2,2,3,1]
# new_list = []

# for i in list:
#     if i not in new_list:
#         new_list.append(i)
    
    
# print(new_list)

# Find the second largest number in a list.

# list = [2,5,8,1,9,10,14,55,7]
# list.sort()

# print(list[-2])

