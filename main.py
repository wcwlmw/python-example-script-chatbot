#lets you use time
import time
#lets you use random
import random, os, sys, re #lets me use these systems
from time import sleep #lets me use a spicific part of time
thanksMatch = re.compile("thanks", re.IGNORECASE) #hashtag makes it a note and does not affect code. also this means the code ignores capitals.
#prints what is in the ()
print ("hello")
#lets you have computer say something and have you respond. can be used in later
example_1 = input("what is your name? ")
#printing a preveous input
print (example_1+"... nice name")
#sleeps for a certen amout of time
time.sleep(1)
# this is waits for an amount of time between the 2 numbers
time.sleep(random.randint(1,2))
#lets you print a preveous input in the middle of a sentence
input ("how are you %s? " % (example_1))
#how to print preveous inputs at any part of a sentence
print (example_1+(" + ")+example_1+(" = ")+example_1+example_1)
#opens file for player to type in
print('hey, i learned a cool trick, i can read from files')
nex = input('press enter to continue')
print('lemmie make a new file real quick...')
time.sleep(3)
#makes a new file
write = open("write here.txt", "x")
print('there, now type something in it!')
nex = input('press enter when your done!')
#close a file
write.close()
print('now i scan it!, scanning...')
time.sleep(3)
write = open("write here.txt", "r+")
print('you put in')
#read a file
print(write.read())
time.sleep(random.randint(1,3))
print('pretty cool right?')
time.sleep(1)
#delete a file
os.remove("write here.txt")

def how_to_play(i):#this defines a set of instructions that can be used later
  htp = i + "\n"

  for char in htp:
    sleep(.025)
    sys.stdout.write(char)
    sys.stdout.flush()

how_to_play("i can say things slowly")#this calls a define function(Line 44)
time.sleep(1)
print("bye!")
time.sleep(random.randint(1,2))
#close program
quit()