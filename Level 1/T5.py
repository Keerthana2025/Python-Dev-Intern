// CHECK PALINDROME

def is_palindrome(s):
    return s == s[::-1]

text = input("Enter a string: ")

if is_palindrome(text):
    print("It is a palindrome")
else:
    print("It is not a palindrome")
