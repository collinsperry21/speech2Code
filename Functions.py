import Listen as l


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
    returnFile = open(fileString, "w+")
    return returnFile.name


def exitMenu(exit):
    if exit == "exit":
        print("Emergency exit.")
        exit(1)
