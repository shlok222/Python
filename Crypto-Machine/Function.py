# 1. Wap to return a dictionary with characters and ascii value pair

def Values(a):
    Dic = {}
    for i in a:
        Dic[i] = ord(i)
        print(Dic)
Values('Shlok')

# 2. Wap to perform addition and subtraction if "a" is greater than "b" return sum else return difference

def Cal(a,b):
    if(a > b):
        print(a + b)
    else:
        print(a - b)
Cal(20,30)

# 3. Waf to check string is palindrome or not (take user input)

def Palindrome(a):
    if a == a[::-1]:
        print('The Given string is palindrome')
    else:
        print('The Given string is not palindrome')

Palindrome('Shlok')

# 4. Wap to fetch last digit number

# def LastDigit(a):
#     print(a[-1])

# LastDigit('Shlok')

def Last_number(x):
    return x%10
print(Last_number(123))

# 5.Wap to squaring of the element in the given list

l=[1,2,3,4,5]
v=[]

def Square(l):
    for i in l:
        v.append(i**2)
    print(v)
Square(l)