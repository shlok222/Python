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

# x = ["a","e","i","o","u"]

# def count_vowels(string):
#     count = 0
#     for i in string:
#         if i in x:
#             count += 1
            
#     print(count)

# count_vowels("mountain")

# 4. Count the number of words in a string
# string = "I love Python programming"
# x = string.split()

# print(len(x))

# # Another Way for counting the number of words in a string

# def in_words(string):
#     a = string.split()
#     print(len(a))
    
# in_words("I love Python programming")


# 5. Find the longest word in a string

# string = "I love Python programming"
# x = string.split()

# print(max(x, key=len))

# # Another Way for finding the longest word in a string

# def longest_word(string):
#     x = string.split()
#     print(max(x, key=len))

# longest_word("I love Python programming")

# # Another Way for finding the longest word in a string

# def in_words(string):
#   count = 0
#   longest = ""
  
#   words = string.split()
  
#   for word in words:
#       if len(word) > count:
#         count = len(word)
#         longest = word
    
#   print(longest)

# in_words("I love Python programming")

# 6 Remove all spaces from a string

def remove_space(string):
    split = string.split()
    result = "".join(split)
    print(result)
    

remove_space("web 3 is cool")




