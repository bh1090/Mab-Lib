# Mads Libs Generator!!
import sys
import os
from time import sleep
print("Welcome to my Mads-Libs Generator!! Input your desired words(nouns, adjectives, etc) and then witness a story be generated and enjoy!!!")
print("")
print("Please type an exclamation")
exclamation = input()
print("")
print("Please type an adverb")
adverb = input()
print("")
print("Please type an noun")
noun = input()
print("")
print("Please type an adjective")
adjective = input()
print("")

print("Making the awesome story for you", end = '')
import time, sys

def writeText(string, t):
    i = 0
    while i < len(string):
        print(string[i], end = '')
        time.sleep(float(t))
        i += 1
        sys.stdout.flush()

writeText("...", 1)
sleep(1)
print("")
print( str(exclamation) + "! he said " + str(adverb) + " as he jumped into his convertible "+ str(noun) + " and drove off with his " + str(adjective) + " wife.")
sleep(5)
print("")
print("Do you want to try another Mads Libs story???")
print("Please type yes or no")
print("")
k = 0
a = input()
while k == 0:
    if a == "Yes" or a == "yes":
        print ("")
        os.system('clear') 
        break
    elif a == "No" or a == "no":
        print("")
        print("Thanks for playing!")
        print("Play again soon, bye!")
        k += 1
        sys.exit()
    else:
        print("Please type yes or no.")

print("Story: What happens when a unicorn poops???")
sleep(3)
print("")
print("Please type 5 plural nouns")
pluralnoun = input()
pluralnoun1 = input()
pluralnoun2 = input()
pluralnoun3 = input()
pluralnoun4 = input()
print("")
print("Please type 5 adjectives")
adjectivepp = input()
adjective1 = input()
adjective2 = input()
adjective3 = input()
adjective4 = input()
print("")
print("please input a color")
color = input()
print("")
print("Please input 2 nouns")
nounpp  = input()
noun1 = input()
print("")
print("Please input an animal plural noun")
animalnoun  = input()
print("")
print("Please input 2 verbs")
verb = input()
verb1 = input()
print("")
print("Please input an - ed verb")
edverb = input()
print("")
print( "Unicorns aren't like other" + str(pluralnoun) + ";" + " they're" + str(adjectivepp) + "." + " They look like " + str(animalnoun) + "," + " with " + str(pluralnoun1) + " for feet and a " + str(adjective1) + " mane of hair. But unicorns are " + str(color) + " and have a " + str(adjective2) + " " + str(nounpp) + " on their heads. Some " + str(pluralnoun2) + " don't believe unicorns are " + str(adjective3) + " but I belive in them. I would love to " + str(verb) + " a unicorn to faraway " + str(pluralnoun3) + "." + " One thing I've always " + str(edverb) + " about is whether unicorns " + str(verb1) + " rainbows, or is their " + str(noun1) + " " + str(adjective4) + " like any other animals's?")

sleep(5)
print("Thanks for playing my mad-lib generator!")
sleep(2)
print("I hope you had fun,")
sleep(1)
print("Bye!")
sys.exit()
