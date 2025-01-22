#1.wap to check the given number is even or odd (take user input)
number=eval(input("enter a number"))
if number%2==0:
    print("even number")
else:
    print("odd number")

#2.wap to check whether the male and female are eligible for wedding (take user input)
maleage=eval(input("Enter male age"))
femaleage=eval(input("Enter female age"))
if maleage>=21 and femaleage>=18:
    print("Elgible for wedding")
else:
    print("Not Eligible")


#3.wap to return uppercase if the char is lower,else return same char (by taking user input)

value=eval(input("Enter a charachter"))
if value.islower():
    print(value.upper())
else:
    print(value)


#4.wap to return lower case if the upper ,else return same char (by taking user input)

value=eval(input("Enter a charachter"))
if value.'upper():
    print(value.lower())
else:
    print(value)

#5.wap to find greater value among the two number

n1=91
n2=78
if n1>n2:
    print(n1)
else:
    print(n2)


#6.wap to check if the given number is even or not,if it is not even add+1 and make it even
# (take user input)

num=eval(input("Enter a number"))
if num%2==0:
    print("It is a even number")
else:
    print(num+1)



#7.wap to check whether the first character in the given string is starting with uppercase
# or Not if it is not Then capitalize it

string='python'
if string[0].isupper():
    print(string)
else:
    print(string.capitalize())


#8.wap to check if the given number is even ,
# if it is even reduce it to its Half else make exponent (take user input)
num=eval(input("Enter a number"))
if num%2==0:
    print(num/2)
else:
    print(num**2)



#9.wap to check number should be divisible by 3 and 7 (take user input)
num=eval(input("enter a number"))
if num%3==0 and num%7==0:
    print("entered number is  divisible by 4 and 7")
else:
    print("entered number is not divisible by 4 and 7")

#10.wap if the length of string is even then reverse else convert into upper case (take user input)
s=input("Enter a string")
if len(s)%2==0:
    print("Given string is even")
else:
    print(s.upper())

#11.wap to check a number is +ve/-ve number (take user input)
# num=eval(input("Enter a number"))
# if num>0:
#     print("Positive number")
# else:
#     print("Negative number")

#12.wap to check a data is individual or collection data type or not (take user input)
# element=eval(input("Enter element"))



#13.wap to check whether the specified character is present in the given string

# s="Vaishnavi"
# c=input("enter a character")
# if c in s:
#     print("character is present")
# else:
#     print("character is not present")

# 14.wap to check the length of dictionary and length of dictionary is even or Not if even
# print as it is or else add a item and make it even


# D={"a":"apple","b":"ball","c":"cat"}
# if len(D)%2==0:
#     print(f"dictionary is even {D}")
# else:
#     D['d']='dog'
#     print(f"dictionary is odd {D}")

# 15.wap to check the given number is greater than 5,if it is greater convert that number into negative number

# num=eval(input("enter a number"))
# if num>5:
#     print(-abs(num))
# else:
#     print(num)



# '''
# 16.wap to check the given number is smaller than 10 ,if it is smaller find the exponent of it
# else print the number as it is
# '''
# # num=eval(input("enter a number"))
# # if num<10:
# #     print(num**2)
# # else:
# #     print(num)
#
# '''
# 17.wap to check the given number is odd, if it is odd
# divide it by 2 and print reminder and quotient else print it is even (take user input)
# '''
# # num=eval(input("enter a number"))
# # if num%2==1:
# #     q=num//2
# #     r=num%2
# #     print(f"quotient {q} and reminder {r}")
# # else:
# #    print("number is even")
#
# ''
# 18.wap to check if the given character is alphabets or Not ,
# if it is alphabet create a replica of it for 2 times. (take user input)
# '''
# # c=input("enter a character")
# # if c.isalpha():
# #     print(c*2)
# # else:
# #     print("given character is not alphabate")
#
# '''
# 19.WAP to check whether the given number value is divisible by 6 or not,
# if it is divisible cube that number or else perform left shift operation by 3 (take user input)
# '''
# num=eval(input("enter a number"))
# if num%6==0:
#     print(6**3)
# else:
#     print(num<<3)