import re


def palindrome(userInput):
        cleanedString = re.sub('[^a-zåäö]+', '', userInput)
        newString = ""
        length = len(cleanedString)
        number = length - 1
        x = 0
        print("Testing: " + cleanedString)
        for x in range(length):
            newString += cleanedString[number]
            number = number - 1
            if cleanedString[x] != newString[x]:
                print("False")
                return 0
            x += 1
        if cleanedString == newString:
            print("True")
            return 1


def ui():
    while True:
        userInput = input("Choose mode: (I)nteractive, (R)ead from file or (E)xit.").lower()
        if userInput == "i":
            typeinput()
        elif userInput == "e":
            break
        elif userInput == "r":
            read()
        else:
            print("ERROR! Option not yet implemented, choose from (I)nteractive, (R)ead or (E)xit")


def read():
    filepath = input("Please type the file path:")
    file = open (filepath, "r")
    filetostring = file.read().replace('\n', ' ')
    stringlist = filetostring.split()
    parseinput(stringlist, filetostring)



def typeinput():
    while True:
        userInput = input("Tell me something or type E to exit to main menu:").lower()
        if userInput == 'e':
            break
        stringlist = userInput.split()
        parseinput(stringlist, userInput)


def parseinput(stringlist, userInput ):
    counter=0
    x = 0
    for x in range(len(stringlist)):
        counter += palindrome(stringlist[x])
        x += 1
    if len(stringlist) > 1:
        counter += palindrome(userInput)
    print("Total number of palindromes: " + str(counter))
ui()
