import sys, random, math

#  TODO:
#   - Make constants configurable
#   - Ensure configurable constants have proper limits set
#   - Final test

# Constants
CLEARSCREEN_LINES = 300
NGG_MAXNUMBER = 100
NGG_MAXGUESSES = 10
NGG_HEATHINT = True
NGG_VERYCLOSEHINT = False
NGG_VERYCLOSEHINTPERCENTAGE = 0.1
CAB_NUMBERSIZE = 4
CAB_MAXGUESSES = 10

# Main function
def __MAIN():
    global CLEARSCREEN_LINES
    global NGG_MAXNUMBER
    global NGG_MAXGUESSES
    global NGG_HEATHINT
    global NGG_VERYCLOSEHINT
    global NGG_VERYCLOSEHINTPERCENTAGE
    global CAB_NUMBERSIZE
    global CAB_MAXGUESSES
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
            print("\nA number between 1 and", NGG_MAXNUMBER, "has been played. Can you guess it?")
            guessesLeft = NGG_MAXGUESSES
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
                        if NGG_HEATHINT:
                            print("\n  Your guess is too", "low! " if userGuess < correctGuess else "high! ", end = "")
                        else:
                            print("\n  Incorrect guess! ", end = "")
                        if NGG_VERYCLOSEHINT and math.fabs(userGuess - correctGuess) <= correctGuess * NGG_VERYCLOSEHINTPERCENTAGE:
                            print(f"Your guess is within {NGG_VERYCLOSEHINTPERCENTAGE * 100:.1f}% of the correct guess.")
                        print()
            if hasGuessed:
                print("\nYou correctly guessed the number! Correct guess:", correctGuess)
                print("Guesses used:", guessCount, "of", NGG_MAXGUESSES if NGG_MAXGUESSES != -1 else "infinite")
            else:
                print("\nYou didn't guess correctly! Correct guess:", correctGuess)
                print("Total guesses:", NGG_MAXGUESSES)
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
                print("Guesses used:", guessCount, "of", NGG_MAXGUESSES if NGG_MAXGUESSES != -1 else "infinite")
            else:
                print("\nYou didn't guess correctly! Correct guess:", correctString)
                print("Total guesses:", NGG_MAXGUESSES)
            print("------------------------")
        elif userChoice == 3:
            clearscreen()
            print("\nProgram configuration\nConfigurable Values:")
            print("  1. NGG: Maximum Number To Guess =", NGG_MAXNUMBER, "(default 100)")
            print("  2. NGG: Maximum Number Of Guesses =", NGG_MAXGUESSES, "(default 10)")
            print("  3. NGG: Heat Hint =", NGG_HEATHINT, "(default True)")
            print("  4. NGG: Proximity Hint =", NGG_VERYCLOSEHINT, "(default False)")
            print(f"  5. NGG: Proximity Hint Percentage = {NGG_VERYCLOSEHINTPERCENTAGE*100:.1f}%", "(default 10.0%, max 90.0%)")
            print("  6. CAB: Maximum Number Size =", CAB_NUMBERSIZE, "(default 4, max 10)")
            print("  7. CAB: Maximum Number Of Guesses =", CAB_MAXGUESSES, "(default 10)")
            userInput = input("\nEnter the value to change: ")
            userChoice = -1
            if userInput.isdigit():
                userChoice = int(userInput)
            else:
                userInput = userInput
                if findany(userInput, "1", "to") != -1 and "guesses" not in userInput and "cab" not in userInput:
                    userChoice = 1
                elif findany(userInput, "2", "of", "guesses") != -1 and "cab" not in userInput:
                    userChoice = 2
                elif findany(userInput, "3", "heat") != -1 and "cab" not in userInput:
                    userChoice = 3
                elif findany(userInput, "4", "proximity") != -1 and "percentage" not in userInput and "cab" not in userInput:
                    userChoice = 4
                elif findany(userInput, "5", "proximity", "percentage") != -1 and "cab" not in userInput:
                    userChoice = 5
                elif findany(userInput, "6", "size") != -1 and "ngg" not in userInput:
                    userChoice = 6
                elif findany(userInput, "7", "guesses") != -1 and "ngg" not in userInput:
                    userChoice = 7
            if userChoice <= 0 or userChoice > 7:
                print("\nInvalid input!\n")
            else:
                userInput = input("Enter new value: ")
                userInput = userInput.lower()
                if userChoice == 1:
                    if userInput.isdigit():
                        NGG_MAXNUMBER = int(userInput)
                        NGG_MAXNUMBER = 2 if NGG_MAXNUMBER < 2 else NGG_MAXNUMBER
                        print("\nNew value:", NGG_MAXNUMBER, '\n')
                    else:
                        print("\nInvalid input!\n")
                elif userChoice == 2:
                    if userInput.isdigit():
                        NGG_MAXGUESSES = int(userInput)
                        NGG_MAXGUESSES = 1 if NGG_MAXGUESSES < 1 else NGG_MAXGUESSES
                        print("\nNew value:", NGG_MAXGUESSES, '\n')
                    else:
                        print("\nInvalid input!\n")
                elif userChoice == 3:
                    if userInput.isdigit():
                        NGG_HEATHINT = int(userInput) != 0
                        print("\nNew value:", NGG_HEATHINT, '\n')
                    elif "true" in userInput or "false" in userInput:
                        NGG_HEATHINT = "true" in userInput
                        print("\nNew value:", NGG_HEATHINT, '\n')
                    else:
                        print("\nInvalid input!\n")
                elif userChoice == 4:
                    if userInput.isdigit():
                        NGG_VERYCLOSEHINT = int(userInput) != 0
                        print("\nNew value:", NGG_VERYCLOSEHINT, '\n')
                    elif "true" in userInput or "false" in userInput:
                        NGG_VERYCLOSEHINT = "true" in userInput
                        print("\nNew value:", NGG_VERYCLOSEHINT, '\n')
                    else:
                        print("\nInvalid input!\n")
                elif userChoice == 5:
                    if len(userInput) >= 1:
                        NGG_VERYCLOSEHINTPERCENTAGE = sstod(userInput)
                        NGG_VERYCLOSEHINTPERCENTAGE = max(min(NGG_VERYCLOSEHINTPERCENTAGE/100.0,1.0),0.0)
                        print("\nNew value:", NGG_VERYCLOSEHINTPERCENTAGE, '\n')
                    else:
                        print("\nInvalid input!\n")
                elif userChoice == 6:
                    if userInput.isdigit():
                        CAB_NUMBERSIZE = int(userInput)
                        CAB_NUMBERSIZE = 1 if CAB_NUMBERSIZE < 1 else CAB_NUMBERSIZE
                        print("\nNew value:", CAB_NUMBERSIZE, '\n')
                    else:
                        print("\nInvalid input!\n")
                elif userChoice == 7:
                    if userInput.isdigit():
                        CAB_MAXGUESSES = int(userInput)
                        CAB_MAXGUESSES = 1 if CAB_MAXGUESSES < 1 else CAB_MAXGUESSES
                        print("\nNew value:", CAB_MAXGUESSES, '\n')
                    else:
                        print("\nInvalid input!\n")
                else:
                    print("\nInvalid input!\n")



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

# Safely converts string to an integer
def sstoi(inputString):
    resultInt = 0
    isNegative = False
    if '-' in inputString:
        isNegative = True
    for i in range(len(inputString)):
        if inputString[i].isdigit():
            resultInt *= 10
            resultInt += int(inputString[i])
    return -resultInt if isNegative else resultInt

# Safely converts string to an unsigned integer
def sstoui(inputString):
    resultUnsignedInt = 0
    for i in range(len(inputString)):
        if inputString[i].isdigit():
            resultUnsignedInt *= 10
            resultUnsignedInt += int(inputString[i])
    return resultUnsignedInt

# Safely converts string to a double (float)
def sstod(inputString):
    resultDouble = 0.0
    isDecimal, isNegative, currentDecimalPlace = False, False, 1
    if '-' in inputString:
        isNegative = True
    for i in range(len(inputString)):
        if inputString[i] == ".":
            isDecimal = True
        if inputString[i].isdigit():
            if not isDecimal:
                resultDouble *= 10
                resultDouble += float(inputString[i])
            else:
                resultDouble += float(inputString[i]) / (10**currentDecimalPlace)
                currentDecimalPlace += 1
    return -resultDouble if isNegative else resultDouble

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
            global NGG_MAXNUMBER
            global NGG_MAXGUESSES
            global NGG_HEATHINT
            global NGG_VERYCLOSEHINT
            global NGG_VERYCLOSEHINTPERCENTAGE
            global CAB_NUMBERSIZE
            global CAB_MAXGUESSES
            try:
                CLEARSCREEN_LINES = int(configLines[0])
                NGG_MAXNUMBER = int(configLines[1])
                NGG_MAXGUESSES = int(configLines[2])
                NGG_HEATHINT = configLines[3] == "True"
                NGG_VERYCLOSEHINT = configLines[4] == "True"
                NGG_VERYCLOSEHINTPERCENTAGE = float(configLines[5])
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
    configFile.write(str(NGG_MAXNUMBER) + "\n")
    configFile.write(str(NGG_MAXGUESSES) + "\n")
    configFile.write(str(NGG_HEATHINT) + "\n")
    configFile.write(str(NGG_VERYCLOSEHINT) + "\n")
    configFile.write(str(NGG_VERYCLOSEHINTPERCENTAGE) + "\n")
    configFile.write(str(CAB_NUMBERSIZE) + "\n")
    configFile.write(str(CAB_MAXGUESSES))
    configFile.close()
    return 0

sys.exit(__MAIN())