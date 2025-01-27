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

# 6. Waf to search for character in a given string and return corresponding index

string="coding part is done"

def index(string):
    a = eval(input('Enter a character from a string'))
    for i in range(len(string)):
         if string[i] == a:
             print(i)
index("coding part is done")

# 8.Wap to read 3 numbers from the user,
# first two numbers should be added and the result of addition should be subtracted by third number

def Num():
    a = eval(input('Enter a no'))
    b = eval(input('Enter a no'))
    c = eval(input('Enter a no'))

    d = a + b
    e = c - d
    print('Sum =',d)
    print('After Subtraction =',e)

Num()

# def Number(a,b,c):
#     x=a+b
#     y=x-c
#     return(x,y)
# print(Number(6,7,8))

# 9. Wap to find square,cube,square root and cube root of a number

def Square_Cube_root(x):
    return x**2,x3,x0.3333,x*0.5
Square_Cube_root(2)

# 10. Wap to check the given characters is alphabets or digit or special characters

# def Chr_Alp():
#     a = eval(input('Enter a no or character'))
#     if a.isalpha():
#         print('The Given input is Alphabet')
#     elif a.isdigit():
#         print('The Given input is Character')
#     else:
#         print('It is a special Character')
# Chr_Alp()

def Char(a):
   if a.isalpha():
       print("its alpha")

   elif a.isdigit():
       print("is digit")

   else:
       print("its special")

Char('abcd')
Char('1234')
Char('@#$')