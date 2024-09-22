'''Write a program that takes a string and returns the most frequent character in it'''

#Input string is given
input_string="Mississippa"

#Initializing an empty dictionary to add the count of each letters in the word
mp={}

#iterate each character to get the count of each letter
for char in input_string:
    #to check if char is present in dictionary
    if char in mp:
        mp[char]+=1
    else:
        mp[char]=1


#to find max value

freq_char=max(mp,key=mp.get)

#printing the result
print("The most frequent character from the given string is:",freq_char)


