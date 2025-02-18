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

# Sum of Digits

a = input('Enter 2 or more than 2 digit no')
Sum = 0

for i in a:
    Sum += int(i)
print(Sum)

# Iterative Python Code to find sum of digits

def sumOfDigits(n):
    sum = 0
    while n != 0:

        # Extract the last digit
        last = n % 10

        # Add last digit to sum
        sum += last

        # Remove the last digit
        n //= 10
    return sum

print(sumOfDigits(1234))

# Even or Odd

def Ans(n):
    if n % 2 == 0:
        print(n,'is even no.')
    else:
        print(n,'is odd no.')

Ans(2)

# Table by function 

def Table(n):
    for i in range(1,11):
        print(n,'*',i,'=',n * i)

Table(2)

# Sum of Natural Nos by function

# Input: n = 3
# Output: 6
# Explanation: Note that 1 + 2 + 3 = 6

def Sum(n):
    Sum = 0

    for i in range(1,n+1):
        Sum += i
    print(Sum)

Sum(3)

# Swap 2 Nos by function

# Input: a = 2, b = 3
# Output: a = 3, b = 2

def Swap(n,m):
    n = n + m
    m = n - m 
    n = n - m
    print(n,m)

Swap(2,3)

# Swap 2 Nos by function

# Input: a = 2, b = 3
# Output: a = 3, b = 2

def Swap(n,m):
    n = n + m
    m = n - m 
    n = n - m
    print(n,m)

Swap(2,3)

# Sum of Digits by fucntion

def Sum(n):
    Sum = 0 
    for i in str(n):
        Sum += int(i)
    print(Sum)

Sum(222)

# def Sum(n):

#     Sum = 0
#     while n != 0:
#         a = n % 10
#         Sum += a
#         n = n // 10
#     print(Sum)

# Sum(222)

# Prime Number 

def Prime(n):
    if n <= 1:
        return False
        
    for i in range(2,n):
        if n % i == 0:
            return False 
        else:
            return True

print(Prime(15))

# Distance between 2 points 

def distance(x1, y1, x2, y2):
   
  # Calculating distance
   
  return (((x2 - x1)**2 +(y2 - y1)**2)**0.5)
 
# Drivers Code
 
print( distance(3, 4, 4, 3))

# Vaild Triangle

# Given three sides, check whether triangle is valid or not. 
# Examples: 
 

# Input :  a = 7, b = 10, c = 5 
# Output : Valid

# Approach: A triangle is valid if sum of its two sides is greater than the third side. 
# If three sides are a, b and c, then three conditions should be met. 
 
# 1.a + b > c 
# 2.a + c > b 
# 3.b + c > a  

def Triangle(a,b,c):
    
    if (a + b > c) or (a + c > b) or (b + c > a) : 
        return False
    else: 
        return True 

Triangle(2,3,5)


# Factorial of a Number

def Fac(n):
    Sum = 1
    for i in range(1,n+1):
        Sum *= i
    print(Sum)

Fac(5)

# Square Root

# import math

# def Sqroot(n):
#     print(math.sqrt(n))

# Sqroot(9)

def Sqroot(n):
    a = n ** 0.5    # Like **2, **3 is used for Square and Cube - **0.5 is used for Squareroot
    print(a)

Sqroot(4)

# GCD or HCF (Follow Link - https://www.geeksforgeeks.org/program-to-find-gcd-or-hcf-of-two-numbers/)

def gcd(a, b):

    # Find minimum of a and b
    result = min(a, b)

    while result:
        if a % result == 0 and b % result == 0:
            break
        result -= 1

    # Return the gcd of a and b
    return result

gcd(98,56)

# Perfect Number

# Input: n = 15
# Output: false
# Divisors of 15 are 1, 3 and 5. Sum of 
# divisors is 9 which is not equal to 15.

def Perfect(n):
    Sum = 0
    for i in range(1,n):
        if n % i == 0:
            Sum += i
    print(Sum)

    if Sum != n:
        return False
    else:
        return True

Perfect(6)

# Perfect Number

# Input: n = 15
# Output: false
# Divisors of 15 are 1, 3 and 5. Sum of 
# divisors is 9 which is not equal to 15.

def Perfect(n):
    Sum = 0
    for i in range(1,n):
        if n % i == 0:
            Sum += i
    print(Sum)

    if Sum != n:
        return False
    else:
        return True

Perfect(6)

# Armstrong Number

# def Arm(n):
#     Sum = 0
#     for i in str(n):
#         Sum += int(i)**3
#     print(Sum)

#     if Sum == n:
#         print(n,'is an amstrong number')
#     else:
#         print(n,'is not an amstrong number')

# Arm(120)


def Arm(n):
    Main_no = n
    Sum = 0
    
    while n != 0:
        Last_No = n % 10
        Sum += Last_No**3
        n //= 10
    print(Sum)
    
    if Sum == Main_no:
        print(Main_no,'is an amstrong number')
    else:
        print(Main_no,'is not an amstrong number')
        
Arm(153)

# Subtract 1 without arithmetic

def Sub(n):
    c = n + ~0
    print(c)

Sub(12)

# N-th term of 1, 3, 6, 10, 15, 21…

# Given a number n, find the n-th term in the series 1, 3, 6, 10, 15, 21…

# Examples: 

# Input : 3
# Output : 6 -- As the #rd no in the series is 6 so output is 6

def term(n): 
    return n *(n + 1) / 2
      
term(2) 

#Digit to Binanry
def Bi(n):
    Result =[]
    while n == 0 or n == 1:
        c = n / 2
        Result.append(c)