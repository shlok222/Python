# 1.wap to check whether the given character is uppercase/lowercase/digit/special
# (with and without using inbuilt function)

ele=input("Enter a character")
if ele.isupper():
    print("Given character is upper")
elif ele.islower():
    print("Given character is lower")
elif ele.isdigit():
    print("Given character is digit")
else:
    print("It is special character")

# without using inbuilt
ele = input("Enter a character")
if ord("A")<=ord(ele)<=ord("Z"):
    print("its uppercase")
elif ord("a")<=ord(ele)<=ord("z"):
    print("its lowercase")
elif ord("0")<=ord(ele)<=ord("9"):
    print("its number")
else:
    print("special")


# 2.wap to check a data is a sequence/iterable/individual data type

char=eval(input("Enter a element"))
if isinstance(char,(int,float,complex,bool)):
    print("indiviual datatype")
elif isinstance(char,(str,list,tuple)):
    print("Sequence datatype")
else:
    print("COllection datattype")

# 3.wap if input is string return its length,else if input is list pop element,else
#  if input is tuple reverse else invalid input
#
ele=eval(input("Enter a element"))
if isinstance(ele,str):
    print(len(ele))
elif isinstance(ele,list):
    print(ele.pop())
elif isinstance(ele,tuple):
    print(ele[::-1])
else:
    print("invalid output")

# 4.wap to check a age belongs to category 0 to 17 child and 18 to 30 ur adult,31 to 60 ur men,
# 61 to 100 senior citizen,else
#  invalid

num=eval(input("Enter a number"))
if num>=0 and num<=17:
    print("child")
elif num >= 18 and num <= 30:
    print("adult")
elif num >= 31 and num <= 60:
     print("men")
elif num >= 61 and num <= 100:
     print("senior citizen")
else:
    print("invalid")

# 5.wap to check which is smallest value among 3 numbers
a=65
b=34
c=76

if a<b and a<c:       #65<34 and 65<76
    print("a is smaller",a)


elif b<a and b<c:           #34<65 and 34<76
    print("b is smaller",b)

else:
    print("c is smaller",c)

# 6.wap to take marks of 5 sub,calculate the average if the average is b/w 90-100 print Distinction
# if 75-89 print first class and if it's 60-74 print second class, if 50-59 print Third class,below 50 is fail
#
# note:-->max marks is 100

# marks1=eval(input("Enter the maths marks"))
# marks2=eval(input("Enter the sci marks"))
# marks3=eval(input("Enter the bio marks"))
# marks4=eval(input("Enter the draw marks"))
# marks5=eval(input("Enter the computer marks"))
# average=marks1+marks2+marks3+marks4+marks5
# total=average/5
#
# if total>=90 and total<=100:
#     print("Distinction")
# elif total>=75 and total<=89:
#     print("first Class")
# elif total>=60 and total<=74:
#     print("second class")
# elif total>=50 and total<=59:
#     print("Third Class")
# else:
#     print("fail")
#
# 8.wap to check eligibility for marriage

# maleage=eval(input("ENter male age"))
# femaleage=eval(input("Enter female age"))
# if maleage>=21 and femaleage>=18:
#     print("Both are eligible for marriage")
# elif maleage>=21 and femaleage<=18:
#     print("female is not eligible for marriage")
# elif maleage<=21 and femaleage>=18:
#     print("Male is not eligible for marriage")
# else:
#     print("Both are not eligible for marriage")

# 9.wap to give discount to customer based on total price(p1+p2+p3)
# 1000 to 3000 price 500 discount and 3001 to 5000 price 1000 discount more than 5001 price
# 1200 discount and less than 1000 price no discount


# product1=eval(input("Enter the amount1"))
# product2=eval(input("Enter the amount2"))
# product3=eval(input("Enter the amount3"))
# total=product1+product2+product3
# print(total)
# if total<=1000:
#     print("No discount")
# elif total>=1000 and total<=3000:
#     print(total-500)
# elif total>=3001 and total<=5000:
#     print(total-1000)
# else:
#     print(total-1200)




# 10.wap to check if the given number is even or odd or Zero
# num=eval(input("Enter number"))
# if num%2==0:
#     print("Given number is even number")
# elif num%2==1:
#     print("Given number is odd number")
# else:
#     print("zero")