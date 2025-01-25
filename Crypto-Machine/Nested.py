Travelling=["Bus","Car","Bike"]
user1=eval(input("Enter mode of travelling"))
if user1 in Travelling:
    print(f'The user have selected mode of travelling{user1}')

    Theater=["cinepole","city pride","amanora"]
    user2=eval(input("Enter the theater name"))
    if user2 in Theater:
        print(f'The user2 have selected the threater {user2}')

        Movie = ["Pushpa2", "Amaran", "Lucky Bhaskar"]
        user3 = eval(input("Enter the movie name"))
        if user3 in Movie:
            print(f'The user3 have selected the  movie name is {user3}')

            Price=[200,250,300]
            amount=eval(input("Enter the amount"))

            if amount==Price[0]:
                print(f'The amount  selected by the user {amount}')

            elif amount==Price[1]:
                print(f'The amount selected by the user {amount}')

            elif amount == Price[2]:
                print(f'The amount selected by the user {amount}')
            else:
             print("Enter price")
        else:
            print("Enter movie name")

    else:
        print("Enter theater name")

else:
    print("Enter mode of travelling")


# 1)wap to check whether the given number is even and greater than 5

# num=10
# if num%2==0 and num>=5:
#     print('number is even')

#2.wap to check the number is odd and check if the number is divisible by 7

# num=35
# if num%2==1:
#     if num%7==0:
#         print("number is odd")
# else:
#     print("number is even")
#
# #3)
#     num = 33
#     if num % 2 == 1:
#         if num % 7 == 0:
#             print("number is odd")
#     else:
#         print("number is even")

#4)4.wap to validate facebook username and password
# condition is:---> username-->"python"  and password="python masters"

username=eval(input("Enter username"))
password=eval(input("Enter password"))
if username=="python":
    print("valid username")
    if password=="python masters":
        print("valid password")
    else:
        print("invalid pass")
else:
    print("invalid username")

6)wap to find middle element is even or odd

s=[3,4,6,7,9,1,5]
mid=len(s)//2
x=s[mid]
if x%2==0:
    print("Middle number is even")
else:
    print("middle number is odd")

#7.wap to purchase a phone from the shopping app
apps=['flipkart','amazon']
print(apps)
user1=eval(input("enter the app name from above list"))
if user1 in apps:
    print(f"you are selected {user1} app")
    categories = ['electronics', 'mobile', 'fashion', 'furnitures']
    print(categories)
    user2=eval(input("please enter categories from above list"))
    if user2 in categories:
        print(f"you are selected {user1} app and selected {user2} categories ")
        mobile = ["iphone", "samsung", "mi", "oppo"]
        print(mobile)
        user3=eval(input("enter mobile name from above list"))
        if user3 in mobile:
            print(f"you are selected {user3} and please complete payment")
        else:
            print("please selected correct mobile brand, this is invalid mobile name")
    else:
        print("invalid category")
else:
    print("invalid app name")


# 8.wap to give 10% off only who is purchasing in credit card and min 3 product
# should purchase and each product price should be more than 500

pyment_mod=eval(input("please select payment mode(debit card/credit card):-"))
product1=eval(input("please enter price"))
product2=eval(input("please enter price"))
product3=eval(input("please enter price"))


if pyment_mod=="credit card":
    print("you are selected credit card")
    if product1>=500 and product2>=500 and product3>=500:
        print(f"you got 10% discount ")
    else:
        print("sorry,no discount")
else:
    print("on debit card discount is not available")

# 9.wap to perform list operations user should enter only list data type,
# if options 1 pop().options 2 sort() options 3 clear() invalid options,invalid data type

data=eval(input("enter the element"))
if isinstance(data,list):  #(variablename,datatype)
    options=eval(input("Enter the number(1,2,3)"))

    if options==1:
        print(data.pop())

    elif options==2:
        data.sort()
        print(data)

    elif options==3:
       data.clear()
       print(data)
    else:
        print("invalid options")
else:
    print("enter proper element")