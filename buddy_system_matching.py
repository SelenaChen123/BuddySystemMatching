# --------------------------------------------------------------------
# DON'T CHANGE! This is the main code of the program.
# --------------------------------------------------------------------

import copy

def printMenu():
    print("--------------------------------------------------------\n")
    print("Welcome to the NCSU CUSA Buddy System Matching program!\n")
    print("--------------------------------------------------------\n")

    print("This program uses the following data to compute matches:\n")
    print("\t1) Number of matches")
    print("\t2) Number of choices")
    print("\t3) Names of the bigs")
    print("\t4) Names of the littles")
    print("\t5) Final choices of the bigs")
    print("\t6) Final choices of the littles\n")

    print("Here are the rules you must follow:\n")
    print("\t1) Names must be consistently spelled")
    print("\t2) Names must be consistently capitalized")
    print("\t2) Numbers must be typed as digits")
    print("\t2) Numbers must be typed as digits")
    print("\t3) None of the inputs must be empty\n")

    print("Make sure you've read all of the information ready\n")
    print("and have read all of the rules!")

    print("--------------------------------------------------------\n")

def getNumNames():
    n = int(input("Enter the number of matches: "))
    print()
    return n

def getNumChoices():
    c = int(input("Enter the number of choices: "))
    print()
    return c

def choicesExist():
    print("Did you type in the choices of the bigs and littles")
    exist = input("in the code already? (Y/N): ")

    if (exist.upper() == "Y"):
        print()

        return True
    elif (exist.upper() == "N"):
        print()

        return False
    else:
        raise Exception()

def getNames(n):
    names = ["" for i in range(2 * n)]

    for i in range(n):
        print("Enter name of big", i+1, end=": ")
        currentName = input()

        if (currentName == ""):
            raise Exception()

        names[i] = currentName

    print()

    for i in range(n):
        print("Enter name of little", i+1, end=": ")
        currentName = input()

        if (currentName == ""):
            raise Exception()

        names[i+n] = currentName

    print()

    return names

def getBigChoices(c, names):
    n = int(len(names) / 2)
    bigChoices = {}

    for i in range(n):
        bigChoiceString = ""
        for j in range(c):
            print("Enter", names[i], end="'s ")

            if (j+1 == 1):
                print(j+1, end="st choice: ")
            elif (j+1 == 2):
                print(j+1, end="nd choice: ")
            elif (j+1 == 3):
                print(j+1, end="rd choice: ")
            else:
                print(j+1, end="th choice: ")

            currentChoice = input()

            if (len(currentChoice) == 0):
                raise Exception()

            bigChoiceString += currentChoice

            if (j != c):
                bigChoiceString += " "

        bigChoices[names[i]] = bigChoiceString.split()
    
        print()

    return bigChoices

def getLittleChoices(c, names):
    n = int(len(names) / 2)
    littleChoices = {}

    for i in range(n):
        littleChoiceString = ""
        for j in range(c):
            print("Enter", names[i+n], end="'s ")

            if (j+1 == 1):
                print(j+1, end="st choice: ")
            elif (j+1 == 2):
                print(j+1, end="nd choice: ")
            elif (j+1 == 3):
                print(j+1, end="rd choice: ")
            else:
                print(j+1, end="th choice: ")

            currentChoice = input()

            if (currentChoice == ""):
                raise Exception()

            littleChoiceString += currentChoice

            if (j != c):
                littleChoiceString += " "

        littleChoices[names[i+n]] = littleChoiceString.split()
    
        print()

    return littleChoices

def bigMatchmaker(bigChoices, littleChoices):
    freeBigs = sorted(bigChoices.keys())[:]
    matched  = {}
    bigChoices2 = copy.deepcopy(bigChoices)
    littleChoices2 = copy.deepcopy(littleChoices)

    while freeBigs:
        currentBig = freeBigs.pop(0)
        bigList = bigChoices2[currentBig]
        currentLittle = bigList.pop(0)
        potentialBig = matched.get(currentLittle)

        if not potentialBig:
            matched[currentLittle] = currentBig
            print("%s\t\t%s" % (currentBig, currentLittle))
        else:
            littleList = littleChoices2[currentLittle]

            if littleList.index(potentialBig) > littleList.index(currentBig):
                matched[currentLittle] = currentBig

                if bigChoices2[potentialBig]:
                    freeBigs.append(potentialBig)
            else:
                if bigList:
                    freeBigs.append(currentBig)
    print()

    return matched

def littleMatchmaker(bigChoices, littleChoices):
    freeLittles = sorted(littleChoices.keys())[:]
    matched  = {}
    bigChoices2 = copy.deepcopy(bigChoices)
    littleChoices2 = copy.deepcopy(littleChoices)

    while freeLittles:
        currentLittle = freeLittles.pop(0)
        littleList = littleChoices2[currentLittle]
        currentBig = littleList.pop(0)
        potentialLittle = matched.get(currentBig)

        if not potentialLittle:
            matched[currentBig] = currentLittle
        else:
            bigList = bigChoices2[currentBig]

            if bigList.index(potentialLittle) > bigList.index(currentLittle):
                matched[currentBig] = currentLittle

                if littleChoices2[potentialLittle]:
                    freeLittles.append(potentialLittle)
            else:
                if littleList:
                    freeLittles.append(currentLittle)
    
    for currentLittle, currentBig in matched.items():
        print(currentLittle, "\t\t\t", currentBig)

    print()

    return matched

def printMatches(bigChoices, littleChoices):
    print("Here are the matches!\n")

    print("--------------------------------------------------------\n")

    print("Prioritizing Littles")
    print("--------------------\n")
    littleMatchmaker(bigChoices, littleChoices)
    print("Prioritizing Bigs")
    print("-----------------\n")
    bigMatchmaker(bigChoices, littleChoices)

    print("--------------------------------------------------------")

# --------------------------------------------------------------------
# CHANGE THIS! Only change this if you don't want to be prompted.
# --------------------------------------------------------------------

bigChoices = {
    "big1":
        ["little1","little2"],
    "big2":
        ["little2","litle1"]
}

littleChoices = {
    "little1":
        ["big2","big1"],
    "little2":
        ["big1","big2"]
}

# --------------------------------------------------------------------
# DON'T CHANGE! This runs the program and prints out the matches.
# --------------------------------------------------------------------

printMenu()

try:
    if (choicesExist() == False):
        n = getNumNames()
        c = getNumChoices()
        names = getNames(n)
        bigChoices = getBigChoices(c, names)
        littleChoices = getLittleChoices(c, names)

    printMatches(bigChoices, littleChoices)
except:
    print("\nERROR! Please read the instructions and try again.")