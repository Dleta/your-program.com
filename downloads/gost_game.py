#Alpha

import time
from random import randint 


print ("Ghost game" )
brave = True
score = 0 


while brave: 
    ghost_door = randint (1,3)
    print  ("There are three doors in front of you ...")
    print  ("ther's a ghost behind one of them")
    print ("What door do you want open")
    door = input ("1, 2 or 3? ")
    door_num = int(door)

    if door_num > 0 and door_num < 4:
        if door_num == ghost_door:
            print ("GHOST")
            brave = False
        else:
            print ("No ghost")
            print ("you are one room further.")
            score = score + 1 
            print ("run away!")
    else:
        print ("please choose a correct answer")
        print ("or press alt + F4")
        print ("Sponsored by your-program.com")
       
print ("Game over! Your points:", score )
input()

