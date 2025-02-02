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

# Swap 2 Nos

# Input: a = 2, b = 3
# Output: a = 3, b = 2

a = 10
b = 20

a = a + b
b = a - b
a = a - b

print(a,b)

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