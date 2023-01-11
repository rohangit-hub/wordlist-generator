from string import *
from itertools import product


print("\n***************************************************************" )

minChar = int(input("\nEnter Minimum length of the password -->  "))

maxChar = int(input("\nEnter Maximum length of the password -->  "))

print("\n***************************************************************\n" )

# "ascii_letter" for lower and uppercase letters
# "ascii_digits" for digits
# "ascii_punctuation" for specal charecters

value = ascii_letters + digits + punctuation

for i in range(minChar, maxChar+1):
    for j in product(value, repeat=i):
        word = "".join(j)
        p = open("WordList_generator.txt","a")
        p.write(word)
        p.write("\n")

print("Wordlist has been genereted to the current folder with the name \"WordList_generator.txt\" \n" )