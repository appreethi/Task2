'''
Write a python program that takes a string and returns a new string with all the vowels removed
'''
#input string from the user
input_string=input("Enter a string: ")

#Define the vowels to be removed
vowel_string="AEIOUaeiou"

#Initialize an empty string to store the result
result=''

#Iterate through each character from the given string 
for char in input_string:
    #checking if the character is not a vowel
    if char not in vowel_string:
        result=result+char

#Printing the results
print("String with vowels removed: ",result)
