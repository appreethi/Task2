'''Write a python program that takes a string and returns True if it is a palindrome,False otherwise'''

#Input string is given
input_string="malayalam"

#Reversing the string using string slicing
reverse_string=input_string[::-1]

#checking if given string is equal to reverse string
if input_string==reverse_string:
    print("True")
else:
    print("False")

