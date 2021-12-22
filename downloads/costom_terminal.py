# Delta

import os
import platform

##########################################################################
# variables
##########################################################################
# comand line
posibleComands = ["help", "exit", "play", "clear temp", "clear", "lol"]
exit = False
x = -1
# only for comand posibleComands[2] (tic tac toe)
position = [1, 2, 3, 4, 5, 6, 7, 8, 9,]
winner = "a"
turn_tic_tac_toe = "X"


##########################################################################
# functions
##########################################################################


# check if input is valid
def isvalid(comandInput):

  if comandInput == " ":
    return False
  elif comandInput == "":
    return False
  else:
    return True

# check if comand exist and return comand id
def checkComand(x):
  x=0

  if comandInput in posibleComands:
    while x <= len(posibleComands):
        if comandInput == posibleComands[x]:
          return x
        else:
          x = x + 1
  else:
    x = -1
    return x

# execute the comand
def executeComand(x):
  if x == 0:
    comand0()
  elif x == 1:
    comand1()
  elif x == 2:
    comand2()

  elif x == 3:
    comand3()

  elif x == 4:
    comand4()

  elif x == 5:
    comand5()

  elif x == 6:
    comand6()




# what get's executed by the comands

def comand0():
  a = 0
  print("here's all the comands you can execute:\n")

  while a < len(posibleComands):
    print(posibleComands[a])
    a = a + 1
  print("\n")
  
def comand1():
    global exit
    exit = True

def comand2():
  global winner
  global turn_tic_tac_toe
  osClear()
  while winner == "a":
    if  winner == "a":
      turn_tic_tac_toe = "X"
      ZugSpieler()
      checkForWinner()
      if  winner == "a":
        turn_tic_tac_toe = "O"
        ZugSpieler()
        checkForWinner()
    else:
          print("bye")
  winner = "a"

def comand3():
  try:
    os.system("rd %temp% /s /q")
    os.system("md %temp%")
    print("\nTEMP CLEARED\n")
  except:
    print(EOFError())

# other functions
def osClear():
  if (platform.system() == 'Windows'):
    os.system("cls")
  else:
    os.system("clear")

def comand4():
  osClear()

def comand5():
  times = input("how many times: ")
  times = int(times)
  while x > 1:
    print("lol  lol")
    print("lol")
    times = x - 1


def struktur():
    print("\n")
    print(str(position[0]) + "  ¦ " + str(position[1]) + " ¦ " + str(position[2]))
    print("------------")
    print(str(position[3]) + "  ¦ " + str(position[4]) + " ¦ " + str(position[5]))
    print("------------")
    print(str(position[6]) + "  ¦ " + str(position[7]) + " ¦ " + str(position[8]))
    print("\n")

def ZugSpieler():
    struktur()
    zugX = input("Spieler " + turn_tic_tac_toe + " wähle ein Feld aus: ")

    if zugX == "1":
        if position[0] == "X" or position[0] == "o":
            print("this fild's alrady taken!")
        else:
            position[0] = turn_tic_tac_toe

    
    elif zugX == "2":
        if position[1] == "X" or position[1] == "o":
            print("this fild's alrady taken!")
        else:
            position[1] = turn_tic_tac_toe
            
    elif zugX == "3":
        if position[2] == "X" or position[2] == "O":
            print("this fild's alrady taken!")
        else:
            position[2] = turn_tic_tac_toe

    elif zugX == "4":
        if position[3] == "X" or position[3] == "O":
            print("this fild's alrady taken!")
        else:
            position[3] = turn_tic_tac_toe

    elif zugX == "5":
        if position[4] == "X" or position[4] == "O":
            print("this fild's alrady taken!")
        else:
            position[4] = turn_tic_tac_toe

    elif zugX == "6":
        if position[5] == "X" or position[5] == "O":
            print("this fild's alrady taken!")
        else:
            position[5] = turn_tic_tac_toe

    elif zugX == "7":
        if position[6] == "X" or position[6] == "O":
            print("this fild's alrady taken!")
        else:
            position[6] = turn_tic_tac_toe
    elif zugX == "8":
        if position[7] == "X" or position[7] == "O":
            print("this fild's alrady taken!")
        else:
            position[7] = turn_tic_tac_toe

    elif zugX == "9":
        if position[8] == "X" or position[8] == "O":
            print("this fild's alrady taken!")
        else:
            position[8] = turn_tic_tac_toe

    else:
        print("only numbers 1-9!")
        ZugSpieler()

    osClear()


def checkForWinner():
    global winner
    winner = winner
    gameFinished = False
    if position[0] == turn_tic_tac_toe and position[4] == turn_tic_tac_toe and position[8] == turn_tic_tac_toe:
        gameFinished =True
        
    elif position[2] == turn_tic_tac_toe and position[5] == turn_tic_tac_toe and position[8] == turn_tic_tac_toe:
        gameFinished =True

    elif position[0] == turn_tic_tac_toe and position[3] == turn_tic_tac_toe and position[6] == turn_tic_tac_toe:
        gameFinished =True

    elif position[0] == turn_tic_tac_toe and position[1] == turn_tic_tac_toe and position[2] == turn_tic_tac_toe:
        gameFinished =True

    elif position[3] == turn_tic_tac_toe and position[4] == turn_tic_tac_toe and position[5] == turn_tic_tac_toe:
        gameFinished =True

    elif position[6] == turn_tic_tac_toe and position[7] == turn_tic_tac_toe and position[8] == turn_tic_tac_toe:
        gameFinished =True

    elif position[1] == turn_tic_tac_toe and position[4] == turn_tic_tac_toe and position[7] == turn_tic_tac_toe:
        gameFinished =True

    elif position[2] == turn_tic_tac_toe and position[4] == turn_tic_tac_toe and position[6] == turn_tic_tac_toe:
        gameFinished =True

    if gameFinished:
        print("\n" + turn_tic_tac_toe + " WINS!!! ")
        print("\n")
        struktur()
        winner = "f"
        return False
    else:
        return True



##########################################################################
# runs at start
##########################################################################


os.system("color 0A")
osClear()
while exit == False:

  comandInput = input("- ")

  if isvalid(comandInput) == True:
    if checkComand(x) != -1:
      x = checkComand(x)
      executeComand(x)
    else:
      print("\nunknown comand please try again\n")

  else:
    print("\nunknown comand please try again\n")
