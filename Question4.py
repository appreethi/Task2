'''
Write a python program that takes a string and returns the number of unique characters in it
'''

#input string from the user
input_string=input("Enter a string: ")

#Initialize an empty string to store the result
unique_chars=''

#Iterate through each character from the input string
for char in input_string:
    #check if the character is not present in unique_char
    if char not in unique_chars:
        unique_chars=unique_chars+char

#calculate the number of unique characters
num_unique_chars=len(unique_chars)

#Printing the results
print("Number of unique characters: ",num_unique_chars)

