# # 1. Reverse a string

# def reverse_string(s):
#     return s[::-1]

# print(reverse_string("hello"))

# # 2. Check if a string is a palindrome

# def is_palindrome(s):
#     return s == s[::-1]

# print(is_palindrome("racecar"))

# # Another Way for palindrome check

# def string_palindrom(a):
#     b = a[::-1]
#     if (a == b):
#         print("String is palindrom")
#     else:
#         print("String is not a Palindrom")
        
# string_palindrom("mom")

# # 3. Count the number of vowels in a string

# a = "mountain"
# x = ["a","e","i","o","u"]
# count = 0
# for i in a:
#     if i in x:
#         count += 1

# print(count)

x = ["a","e","i","o","u"]

def count_vowels(string):
    count = 0
    for i in string:
        if i in x:
            count += 1
            
    print(count)

count_vowels("mountain")

