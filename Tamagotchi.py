import datetime
import time
import random
import os
import sys
import ast
import msvcrt

bowel = 0
clean = 0
hunger = 1
resting = 0
sick = 0
weak = 0
fitnessBar = 10
illnessCounter = 0
sicknessCounter = 0
bowelTimer = 0
cleanTimer = 0
mealTimer = 0

now = datetime.datetime.now()
checkHr = int(now.strftime("%H"))

msgDict = {"A": "Eat", "B": "Poop", "C": "Exercise", "D": "Sleep", "E": "Medication", "F": "Quit"}
msg2 = "Invalid input"
msg3 = "Do you want to play again? Y/N: "

foodDict = {1: "That tasted good!", 2:"Delicious!", 3:"Yummy!"}
exerciseDict = {1: "One! Two! One! Two!", 2:"Ready! Go!", 3:"Yaaaaaaaah!"}

acceptableInputs2 = "YNyn"



def initialize():
    global bowel, character, clean, hunger, resting, sick, weak, fitnessBar, illnessCounter, incomingData, sicknessCounter, bowelTimer, cleanTimer, mealTimer, msgDict
    if checkHr >= 22 or checkHr <= 8:
        while True:
            sleepAnimation()
            if msvcrt.kbhit():
                ch = msvcrt.getch()
                if ord(ch) >= 0:
                    quit()
    print("Welcome to Tamagotchi!")
    incomingData = "None"
    while incomingData not in acceptableInputs2:
        incomingData = input("Do you want to load from a save file? Y/N: ")
        while incomingData not in acceptableInputs2:
            print(msg2)
            incomingData = input("Do you want to load from a save file? Y/N: ")
        if incomingData == "Y" or incomingData == "y":
            character = input("Please enter the name of your character: ")
            while os.access(f"{character}.txt", os.F_OK) != 1:
                print(msg2)
                character = input("Please enter the name of your character: ")
            f = open(f"{character}.txt", "r")
            try:
                bowel = int(f.readline())
                clean = int(f.readline())
                hunger = int(f.readline())
                resting = int(f.readline())
                sick = int(f.readline())
                weak = int(f.readline())
                fitnessBar = float(f.readline())
                illnessCounter = int(f.readline())
                sicknessCounter = int(f.readline())
                bowelTimer = int(f.readline())
                cleanTimer = int(f.readline())
                mealTimer = int(f.readline())
                msgDict = ast.literal_eval(f.readline())
            except:
                print("File corrupted")

            f.close()
            print("Welcome back!")
        else:
            character = input("Please input a name for your character: ")
            print(f"{character}, that's a great name!")
            f = open(f"{character}.txt", "w")
            time.sleep(3)
            f.close()
        os.system('cls')

def save():
    global bowel, clean, hunger, resting, sick, weak, fitnessBar, illnessCounter, sicknessCounter, bowelTimer, cleanTimer, mealTimer
    f = open(f"{character}.txt", "w")
    f.writelines([str(bowel), "\n", str(clean), "\n", str(hunger), "\n", str(resting), "\n", str(sick), "\n", str(weak), "\n", str(fitnessBar), "\n", str(illnessCounter), "\n", str(sicknessCounter), "\n", str(bowelTimer), "\n", str(cleanTimer), "\n", str(mealTimer), "\n", str(msgDict)])
    f.close()
    quit()

def death():
    os.system('cls')
    printFace(21)
    print(f"Gameover, {character} has died.")
    os.remove(f"{character}.txt")
    time.sleep(1)
    incomingData = "None"
    while incomingData not in acceptableInputs2:
        incomingData = input(msg3)
        if incomingData not in acceptableInputs2:
            print(msg2)
        else:
            if incomingData == "Y" or incomingData == "y":
                os.system('cls')
                os.system("python Tamagotchi.py")
            else:
                sys.exit()

def fitness():
    global illnessCounter, sick, weak
    if fitnessBar <= 1:
        weak = 1
        illnessCounter += 1
    if illnessCounter >= 3:
        sick = 1

def sickness():
    global sicknessCounter, sick
    if sick == 1:
        sicknessCounter += 1
        if sicknessCounter >= 3:
            death()

def printText():
    for key, value in msgDict.items():
        print(f"{key}: {value}")

def printFace(faceNo):
    face = []
    if faceNo == 1:
        face = face1
    elif faceNo == 2:
        face = face2
    elif faceNo == 3:
        face = face3
    elif faceNo == 4:
        face = face4
    elif faceNo == 5:
        face = face5
    elif faceNo == 6:
        face = face6
    elif faceNo == 7:
        face = face7
    elif faceNo == 8:
        face = face8
    elif faceNo == 9:
        face = face9
    elif faceNo == 10:
        face = face10
    elif faceNo == 11:
        face = face11
    elif faceNo == 12:
        face = face12
    elif faceNo == 13:
        face = face13
    elif faceNo == 14:
        face = face14
    elif faceNo == 15:
        face = face15
    elif faceNo == 16:
        face = face16
    elif faceNo == 17:
        face = face17
    elif faceNo == 18:
        face = face18
    elif faceNo == 19:
        face = face19
    elif faceNo == 20:
        face = face20
    elif faceNo == 21:
        face = face21
    elif faceNo == 22:
        face = face22
    elif faceNo == 23:
        face = face23
    elif faceNo == 24:
        face = face24
    elif faceNo == 25:
        face = face25
    elif faceNo == 26:
        face = face26
    elif faceNo == 27:
        face = face27
    elif faceNo == 28:
        face = face28
    elif faceNo == 29:
        face = face29
    elif faceNo == 30:
        face = face30
    for r in face:
        for c in r:
            if c == 1:
                print("\u2592\u2592", end = "")
            elif c == 2:
                print("\u2593\u2593", end = "")
            elif c == 0:
                print("  ", end="")
        print("")

def eatingAnimation():
    printFace(6)
    print("Nom nom nom")
    time.sleep(0.5)
    os.system('cls')

    printFace(7)
    print("Nom nom nom")
    time.sleep(0.5)
    os.system('cls')

    printFace(8)
    print("Nom nom nom")
    time.sleep(0.5)
    os.system('cls')

    printFace(9)
    print("Nom nom nom")
    time.sleep(0.5)
    os.system('cls')

    printFace(10)
    print("Nom nom nom")
    time.sleep(0.5)
    os.system('cls')

def medingAnimation():
    printFace(14)
    print("Nom nom nom")
    time.sleep(0.5)
    os.system('cls')

    printFace(15)
    print("Nom nom nom")
    time.sleep(0.5)
    os.system('cls')

    printFace(16)
    print("Nom nom nom")
    time.sleep(0.5)
    os.system('cls')

    printFace(17)
    print("Nom nom nom")
    time.sleep(0.5)
    os.system('cls')

    printFace(10)
    print("Nom nom nom")
    time.sleep(0.5)
    os.system('cls')

def fatAnimation():
    printFace(3)
    print("Urghhh, I'm stuff'd")
    time.sleep(0.5)
    os.system('cls')

    printFace(4)
    print("Urghhh, I'm stuff'd")
    time.sleep(0.5)
    os.system('cls')

def exerciseAnimation():
    word = random.randint(1, 3)

    printFace(18)
    print(exerciseDict[word])
    time.sleep(0.6)
    os.system('cls')

    printFace(19)
    print(exerciseDict[word])
    time.sleep(0.3)
    os.system('cls')

    printFace(20)
    print(exerciseDict[word])
    time.sleep(0.6)
    os.system('cls')

    printFace(19)
    print(exerciseDict[word])
    time.sleep(0.3)
    os.system('cls')

def washAnimation():
    printFace(22)
    print("Brush brush brush")
    time.sleep(0.3)
    os.system('cls')

    printFace(23)
    print("Brush brush brush")
    time.sleep(0.3)
    os.system('cls')

    printFace(24)
    print("Brush brush brush")
    time.sleep(0.3)
    os.system('cls')

    printFace(25)
    print("Brush brush brush")
    time.sleep(0.3)
    os.system('cls')

    printFace(24)
    print("Brush brush brush")
    time.sleep(0.3)
    os.system('cls')

    printFace(23)
    print("Brush brush brush")
    time.sleep(0.3)
    os.system('cls')

def sleepAnimation():
    printFace(28)
    print("Tamagotchi is asleep right now! Come back at 0800am")
    print("Press any button to exit")
    time.sleep(0.3)
    os.system('cls')

    printFace(29)
    print("Tamagotchi is asleep right now! Come back at 0800am")
    print("Press any button to exit")
    time.sleep(0.3)
    os.system('cls')

    printFace(30)
    print("Tamagotchi is asleep right now! Come back at 0800am")
    print("Press any button to exit")
    time.sleep(0.3)
    os.system('cls')

def idleAnimation():
    if clean == 1:
        printFace(12)
        printText()
        time.sleep(1)
        os.system('cls')

        printFace(13)
        printText()
        time.sleep(1)
        os.system('cls')

    elif sick == 1:
        printFace(5)
        printText()
        time.sleep(1)
        os.system('cls')

    elif checkHr >= 21:
        printFace(27)
        printText()
        time.sleep(1)
        os.system('cls')

        printFace(28)
        printText()
        time.sleep(1)
        os.system('cls')
    else:
        if fitnessBar >= 7:
            printFace(1)
            printText()
            time.sleep(0.3)
            os.system('cls')

            printFace(2)
            printText()
            time.sleep(0.3)
            os.system('cls')

        elif fitnessBar < 7:
            printFace(3)
            printText()
            time.sleep(0.6)
            os.system('cls')

            printFace(4)
            printText()
            time.sleep(0.6)
            os.system('cls')

initialize()

while True:
    idleAnimation()

    # Scheduled events
    if checkHr >= 22:
        hunger = 1
        fitnessBar -= 5
        save()
    if checkHr >= 22:
        hunger = 1
        fitnessBar -= 5
        save()
    if (mealTimer - checkHr) > 3 and hunger == 0:
        hunger = 1
    if (mealTimer - checkHr) > 10 and hunger == 0:
        death()
    if (bowelTimer - checkHr) > 3 and bowel == 1:
        bowel = 0
        clean = 1
        msgDict["B"] = "Clean"
        cleanTimer = checkHr
    if (cleanTimer - checkHr) > 2 and clean == 1:
        death()

    # Input handler
    if msvcrt.kbhit():
        ch = msvcrt.getch()
        # a - Eat
        if ord(ch) == 97:
            fitnessBar -= 2
            eatingAnimation()
            eatingAnimation()
            if hunger == 0:
                fitnessBar -= 2
                printFace(11)
                print("Urghhh, I'm too full!")
                time.sleep(3)
                os.system('cls')
                if bowel == 0:
                    bowel = 1
                    bowelTimer = checkHr
            else:
                hunger = 0
                bowel = 1
                printFace(1)
                print(foodDict[random.randint(1, 3)])
                time.sleep(3)
                os.system('cls')
            mealTimer = checkHr
        # b - Poop / Clean
        if ord(ch) == 98:
            fitnessBar += 0.5
            if bowel == 1:
                bowel = 0
                clean = 1
                msgDict["B"] = "Clean"
                cleanTimer = checkHr
                printFace(3)
                print(". . .", end = " ")
                time.sleep(1)
                print(". . .", end = " ")
                time.sleep(1)
                print(". . .",)
                time.sleep(1)
                os.system('cls')
            elif msgDict["B"] == "Poop":
                printFace(4)
                print("But I don't wanna go!")
                time.sleep(3)
                os.system('cls')
            else:
                clean = 0
                msgDict["B"] = "Poop"
                washAnimation()
                washAnimation()
                washAnimation()
                printFace(1)
                print("I'm all clean now!")
                time.sleep(3)
                os.system('cls')
        # c - Exercise
        if ord(ch) == 99:
            fitnessBar += 5
            exerciseAnimation()
            exerciseAnimation()
            exerciseAnimation()
        # d - Sleep
        if ord(ch) == 100:
            if checkHr >= 20 and checkHr <= 22:
                resting = 1
            else:
                printFace(3)
                print("It's too early! I don't wanna sleep!")
                time.sleep(3)
                os.system('cls')
        # e - Medication
        if ord(ch) == 101:
            if sick == 1:
                sicknessCounter = 0
                illnessCounter = 0
                sick = 0
                medingAnimation()
                printFace(1)
                print("I feeling much better now!")
                time.sleep(3)
                fitnessBar = 3
                os.system('cls')
            else:
                printFace(3)
                print("But I'm not sick!")
                time.sleep(3)
                os.system('cls')
        # f - Quit
        if ord(ch) == 102:
            save()

        fitness()
        sickness()

    while msvcrt.kbhit():
        msvcrt.getch()