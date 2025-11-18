import sys, random, math

#  TODO:
#   - Make constants configurable
#   - Ensure configurable constants have proper limits set
#   - Final test

# Constants
CLEARSCREEN_LINES = 300
NNG_MAXNUMBER = 100
NNG_MAXGUESSES = 10
NNG_HEATHINT = True
NNG_VERYCLOSEHINT = False
NNG_VERYCLOSEHINTPERCENTAGE = 0.1

CAB_NUMBERSIZE = 4
CAB_MAXGUESSES = 10

# Main function
def __MAIN():
    clearscreen()
    readResult = readConfigFromFile()
    if readResult == -1:
        print("Could not load configurations from file!")
    elif readResult == 1:
        print("A new configuration file has been created.")
    print("-= Number Game Program =-\n")
    while True:
        print("Enter an option:")
        print("  1. Play Number-Guessing Game")
        print("  2. Play Cows and Bulls")
        print("  3. Configure Games")
        print("  4. Exit")
        userInput = input("> ")
        userChoice = -1
        if userInput.isdigit():
            userChoice = int(userInput)
        else:
            if findany(userInput, "guess", "1"):
                userChoice = 1
            elif findany(userInput, "cow", "and", "bull", "2"):
                userChoice = 2
            elif findany(userInput, "configure", "games", "3"):
                userChoice = 3
            elif findany(userInput, "exit", "stop", "4"):
                userChoice = 4
        if userChoice == 1:
            clearscreen()
            print("\nA number between 1 and", NNG_MAXNUMBER, "has been played. Can you guess it?")
            guessesLeft = NNG_MAXGUESSES
            guessCount = 0
            hasGuessed = False
            correctGuess = random.randint(1, 100)
            while True:
                print("  You have", guessesLeft, "guesses" if guessesLeft != 1 else "guess", "left.\n  Enter your guess: ", end="")
                userGuess = sstoui(input())
                if userGuess == correctGuess:
                    hasGuessed = True
                    break
                else:
                    guessesLeft -= 1
                    guessCount += 1
                    if guessesLeft == 0:
                        break
                    else:
                        if NNG_HEATHINT:
                            print("\n  Your guess is too", "low! " if userGuess < correctGuess else "high! ", end = "")
                        else:
                            print("\n  Incorrect guess! ", end = "")
                        if NNG_VERYCLOSEHINT and math.fabs(userGuess - correctGuess) <= correctGuess * NNG_VERYCLOSEHINTPERCENTAGE:
                            print(f"Your guess is within {NNG_VERYCLOSEHINTPERCENTAGE*100:.0f}% of the correct guess.")
                        print()
            if hasGuessed:
                print("\nYou correctly guessed the number! Correct guess:", correctGuess)
                print("Guesses used:", guessCount, "of", NNG_MAXGUESSES if NNG_MAXGUESSES != -1 else "infinite")
            else:
                print("\nYou didn't guess correctly! Correct guess:", correctGuess)
                print("Total guesses:", NNG_MAXGUESSES)
            print("------------------------")
        elif userChoice == 2:
            clearscreen()
            numberSequence = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
            random.shuffle(numberSequence)
            correctSequence = numberSequence[:CAB_NUMBERSIZE]
            guessesLeft = CAB_MAXGUESSES
            hasGuessed = False
            guessCount = 0
            print(f"\nA {CAB_NUMBERSIZE}-digit code has been generated with no repeating digits.\nCan you guess it given only correctly placed digits (bulls)\nand correctly guessed but incorrectly placed digits (cows)?")
            while True:
                print("  You have", guessesLeft, "guesses" if guessesLeft != 1 else "guess", "left.\n  Enter your guess: ", end="")
                userGuess = input()
                guessList = []
                for i in range(len(userGuess)):
                    if userGuess[i].isdigit():
                        guessList.append(int(userGuess[i]))
                if guessList == correctSequence:
                    hasGuessed = True
                    break
                else:
                    guessesLeft -= 1
                    guessCount += 1
                    if guessesLeft == 0:
                        break
                    else:
                        if len(guessList) == CAB_NUMBERSIZE and userGuess.isdigit():
                            bulls, cows = 0, 0
                            for i in range(len(guessList)):
                                if guessList[i] == correctSequence[i]:
                                    bulls += 1
                                elif guessList[i] in correctSequence:
                                    cows += 1
                            print(" ", bulls, "bulls," if bulls != 1 else "bull,", cows, "cows.\n" if cows != 1 else "cow.\n")
                        else:
                            print("  Invalid input!\n")
            correctString = ""
            for i in range(len(correctSequence)):
                correctString += str(correctSequence[i])
            if hasGuessed:
                print("\nYou correctly guessed the code! Correct code:", correctString)
                print("Guesses used:", guessCount, "of", NNG_MAXGUESSES if NNG_MAXGUESSES != -1 else "infinite")
            else:
                print("\nYou didn't guess correctly! Correct guess:", correctString)
                print("Total guesses:", NNG_MAXGUESSES)
            print("------------------------")
        elif userChoice == 3:
            pass
        elif userChoice == 4:
            writeResult = writeConfigToFile()
            if writeResult < -1:
                print("Could not save configurations to file!")
            clearscreen()
            print("Exiting...")
            break
        else:
            clearscreen()
            print("Invalid input!\n")
    return 0

# Outputs many blank lines to separate old output from new output
def clearscreen():
    outputString = ""
    for i in range(CLEARSCREEN_LINES):
        outputString += '\n'
    print(outputString, end = "")

# Safely converts string to an unsigned integer
def sstoui(inputString):
    resultUnsignedInt = 0
    for i in range(len(inputString)):
        if inputString[i].isdigit():
            resultUnsignedInt *= 10
            resultUnsignedInt += int(inputString[i])
    return resultUnsignedInt

# Checks for any substrings in a target string
def findany(inputString, *strings):
    if len(strings) == 0:
        return -1
    else:
        for i in range(len(strings)):
            if strings[i] in inputString:
                return i
    return -1

# Reads configuration values from the configuration file
def readConfigFromFile():
    configFile = None
    try:
        configFile = open("proj.config", "r")
        configLines = []
        for line in configFile:
            configLines.append(line.strip())
        configFile.close()
        if len(configLines) == 8:
            global CLEARSCREEN_LINES
            global NNG_MAXNUMBER
            global NNG_MAXGUESSES
            global NNG_HEATHINT
            global NNG_VERYCLOSEHINT
            global NNG_VERYCLOSEHINTPERCENTAGE
            global CAB_NUMBERSIZE
            global CAB_MAXGUESSES
            try:
                CLEARSCREEN_LINES = int(configLines[0])
                NNG_MAXNUMBER = int(configLines[1])
                NNG_MAXGUESSES = int(configLines[2])
                NNG_HEATHINT = configLines[3] == "True"
                NNG_VERYCLOSEHINT = configLines[4] == "True"
                NNG_VERYCLOSEHINTPERCENTAGE = float(configLines[5])
                CAB_NUMBERSIZE = int(configLines[6])
                CAB_MAXGUESSES = int(configLines[7])
            except ValueError:
                try:
                    configFile = open("glist.txt", 'w')
                    configFile.write("")
                    configFile.close()
                except PermissionError:
                    pass
                return -1
        else:
            return -1
        return 0
    except FileNotFoundError:
        try:
            configFile = open("glist.txt", 'w')
            configFile.write("")
            configFile.close()
            return 1
        except PermissionError:
            return -1

# Writes configuration values to the configuration file
def writeConfigToFile():
    configFile = None
    try:
        configFile = open("proj.config", 'w')
    except PermissionError:
        return -1
    configFile.write(str(CLEARSCREEN_LINES) + "\n")
    configFile.write(str(NNG_MAXNUMBER) + "\n")
    configFile.write(str(NNG_MAXGUESSES) + "\n")
    configFile.write(str(NNG_HEATHINT) + "\n")
    configFile.write(str(NNG_VERYCLOSEHINT) + "\n")
    configFile.write(str(NNG_VERYCLOSEHINTPERCENTAGE) + "\n")
    configFile.write(str(CAB_NUMBERSIZE) + "\n")
    configFile.write(str(CAB_MAXGUESSES))
    configFile.close()
    return 0

sys.exit(__MAIN())