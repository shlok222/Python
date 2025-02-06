# Table 

a = eval(input('Enter a no'))

for i in range(1,11):
    print(a,'*',i,'=',a * i)

# Sum of Natural Nos

# Input: n = 3
# Output: 6
# Explanation: Note that 1 + 2 + 3 = 6

a = eval(input('Enter a no'))
Sum = 0

for i in range(1,a + 1):
    Sum += i
print(Sum)

# Swap 2 Nos

# Input: a = 2, b = 3
# Output: a = 3, b = 2

a = 10
b = 20

a = a + b
b = a - b
a = a - b

print(a,b)

# Closest No

a = 19 
b = 6

c = a // b 
d = c * b
# print(c)
print(d)


# Dice Problem 

# Print the opp side of the dice like opp to 1 is 6, 2 is 5 etc

a = eval(input('Enter a no between 1 to 6:'))

if a == 1:
    print('The opposite side of the dice for',a,'is 6')
elif a == 2:
    print('The opposite side of the dice for',a,'is 5')
elif a == 3:
    print('The opposite side of the dice for',a,'is 4')
elif a == 4:
    print('The opposite side of the dice for',a,'is 3')
elif a == 5:
    print('The opposite side of the dice for',a,'is 2')
elif a == 6:
    print('The opposite side of the dice for',a,'is 1')
else:
    print('Enter Wrong Input')

# Sum of GP (Geometric Series)

# A Geometric series is a series with a constant ratio between successive terms.
# The first term of the series is denoted by a and common ratio is denoted by r. 
#The series looks like this :- a, ar, ar2, ar3, ar4, . . .. 
#The task is to find the sum of such a series. Examples :

# Input : a = 1
#         r = 0.5
#         n = 10
# Output : 0.9990234375

a = 1
r = 0.5
n = 10
Sum = 0

for i in range(1,n+1):
    Sum += a*(r**i)
print(Sum)

# Simple Intrest

# Given Principal p, Rate r and Time t, the task is to calculate Simple Interest.

# Input: p = 10000, r = 5, t = 5 
# Output:2500 
# Explanation: We need to find simple interest on  Rs. 10,000 at the rate of 5% for 5  units of time. 

p = 10000
r = 5
t = 5

SI = (p * t * r)/100
print(SI)

# Area of Circle

Radius = eval(input('Enter the radius of circle'))

Area = 3.14 * Radius ** 2
print('Area of circle with raduis',Radius,'is',Area)

# wap to reverse internal content of each word.

a = input('Enter a string')
i = 0
b = a.split()

while i < len(b):
    print(b[i][::-1])
    i += 1

 # wap to iterate over a string and print each character twice

a = input('Enter a string')
i = 0

while i < len(a):
    print(a[i]*2)
    i += 1

# wap to iterate over a string and print each character twice

a = input('Enter a string')
i = 0

while i < len(a):
    print(a[i]*2)
    i += 
    
 # wap to print all the consonents from the given string.

a = input('Enter a string')
i = 0
vowels = ('a','e','i','o','u')

# while i < len(a):
#     if a[i] not in 'aeiouAEIOU':
#         print(a[i])
#         i += 1

while i < len(a):
    if a[i] in vowels:
        print(a[i])
    i += 1

# wap to reverse internal content of each word.

a = input('Enter a sentence')
b = a.split()
i = 1

while i < len(b):
    print(b[i][::-i])
    i += 1

# wap to display the sum of first n numbers.

a = eval(input('Enter no'))
i = 0
Sum = 0

while i <= a:
    Sum += i
    i += 1
print(Sum)

# wap to achieve given output.
#  output = "one owt three ruof five xis seven"
a ="one two three four five six seven"

b = a.split()
print(b)

final = []
i = 0

while i < len(b):
    if i % 2 == 0:
        final.append(b[i])
    else:
        final.append(b[i][::-1])
    i += 1
print(final)