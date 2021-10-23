import os

position = [1, 2, 3, 4, 5, 6, 7, 8, 9,]
winner = "a"
aktuellerZug = "X"


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
    zugX = input("Spieler " + aktuellerZug + " wähle ein Feld aus: ")

    if zugX == "1":
        if position[0] == "X" or position[0] == "o":
            print("bitte wähle ein freies Feld aus!")
        else:
            position[0] = aktuellerZug

    
    elif zugX == "2":
        if position[1] == "X" or position[1] == "o":
            print("bitte wähle ein freies Feld aus!")
        else:
            position[1] = aktuellerZug
            
    elif zugX == "3":
        if position[2] == "X" or position[2] == "O":
            print("bitte wähle ein freies Feld aus!")
        else:
            position[2] = aktuellerZug

    elif zugX == "4":
        if position[3] == "X" or position[3] == "O":
            print("bitte wähle ein freies Feld aus!")
        else:
            position[3] = aktuellerZug

    elif zugX == "5":
        if position[4] == "X" or position[4] == "O":
            print("bitte wähle ein freies Feld aus!")
        else:
            position[4] = aktuellerZug

    elif zugX == "6":
        if position[5] == "X" or position[5] == "O":
            print("bitte wähle ein freies Feld aus!")
        else:
            position[5] = aktuellerZug

    elif zugX == "7":
        if position[6] == "X" or position[6] == "O":
            print("bitte wähle ein freies Feld aus!")
        else:
            position[6] = aktuellerZug
    elif zugX == "8":
        if position[7] == "X" or position[7] == "O":
            print("bitte wähle ein freies Feld aus!")
        else:
            position[7] = aktuellerZug

    elif zugX == "9":
        if position[8] == "X" or position[8] == "O":
            print("bitte wähle ein freies Feld aus!")
        else:
            position[8] = aktuellerZug

    else:
        print("nur Zahlen!")
        ZugSpieler()
    
    os.system("cls")




def checkForWinner():
    gameFinished = False
    if position[0] == aktuellerZug and position[4] == aktuellerZug and position[8] == aktuellerZug:
        gameFinished =True
        
    elif position[2] == aktuellerZug and position[5] == aktuellerZug and position[8] == aktuellerZug:
        gameFinished =True

    elif position[0] == aktuellerZug and position[3] == aktuellerZug and position[6] == aktuellerZug:
        gameFinished =True

    elif position[0] == aktuellerZug and position[1] == aktuellerZug and position[2] == aktuellerZug:
        gameFinished =True

    elif position[3] == aktuellerZug and position[4] == aktuellerZug and position[5] == aktuellerZug:
        gameFinished =True

    elif position[6] == aktuellerZug and position[7] == aktuellerZug and position[8] == aktuellerZug:
        gameFinished =True

    elif position[1] == aktuellerZug and position[4] == aktuellerZug and position[7] == aktuellerZug:
        gameFinished =True

    elif position[2] == aktuellerZug and position[4] == aktuellerZug and position[6] == aktuellerZug:
        gameFinished =True

    if gameFinished:
        print("\n" + aktuellerZug + " hat Gewonnen!!! ")
        print("\n")
        struktur()
        input()

while winner == "a":
    ZugSpieler()
    checkForWinner()
    aktuellerZug = "O"
    ZugSpieler()
    checkForWinner()
    aktuellerZug = "X"
