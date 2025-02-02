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