from string import *
from itertools import product
import sys

if(sys.argv[0] and (sys.argv[1] and sys.argv[2]) ):
    print("\n***************************************************************" )
    minChar = int(sys.argv[1])
    maxChar = int(sys.argv[2])
   
    # "ascii_letter" for lower and uppercase letters
    # "ascii_digits" for digits
    #"ascii_punctuation" for specal charecters

    value = ascii_letters + digits + punctuation

    for i in range(minChar, maxChar+1):
        for j in product(value, repeat=i):
            word = "".join(j)
            p = open("WordList_ByTerminal.txt","a")
            p.write(word)
            p.write("\n")

    print("Wordlist has been genereted to the current folder with the name \"WordList_ByTerminal.txt\" " )
    print("\n***************************************************************" )

     
elif(sys.argv[1] == ("--help" or "-h")):
    print("\n***************************************************************" )
    print("\nEnter the command into this format --> ")
    print("\npython fileNane.py <min length> <max length> ")
    print("\n ex.>> python fileNane.py 4 8 \n")

else:
    print("\n***************************************************************" )
    print("\nEnter the command into this format --> ")
    print("\npython fileNane.py <min length> <max length> ")
    print("\n ex.>> python fileNane.py 4 8 \n")






