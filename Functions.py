import Listen as l


def variableDeclaration(filename):
    currentline = len(filename.splitlines()) + 1
    print("You are writing to line#:", currentline)
    print("Please say your variable name: <varName>")
    tempvar = l.listen()
    print("Variable Name: <inputVariable>", tempvar)
    print("Value: <inputValue>")
    tempVal = l.listen()
    print("Value: ", tempVal)
    return tempvar + " = " + tempVal


def comment(filename):
    while 1:
        currentline = len(filename.splitlines())+1
        print("You are commenting to line#:", currentline)
        print("")
        commentstring = l.listen()
        filename.write("# "+commentstring+"\n")
        print("Would you like to make another line of comments? (Say <yes> / <no>)")
        choice = l.listen()
        if choice == "yes":
             comment(filename)
        elif choice == "no":
             break
        else:
            print("Unable to process request. Input heard: ", choice)
            continue


def helper(filename):
    tempfile = filename
    filename.close()
    theFile = open('HelpText.txt', "r")
    print(theFile.read())
    print("Say exit to return to the main menu")
    tempfile.open()


def openFile():
    print("Say File Name to open: <inputFileName>")
    fileString = l.listen() + ".py"
    fileString.replace(" ", "")
    returnFile = open(fileString,"w+")
    return returnFile.name


def startCheck(filename):
    if filename == "start.py":
        return 1
    return 0

def exitMenu(exit):
    if exit == "exit":
        return 1
    return 0