import Listen as l
import os

def helper(filename):
    #tempfile = filename
    #filename.close()
    theFile = open('HelpText.txt', "r")
    print(theFile.read())
    theFile.close()
    print("Say exit to return to the main menu...")


def openFile():
    print("Say File Name to open: <inputFileName>")
    fileString = l.listen() + ".py"
    if os.path.exists(fileString):
        returnFile = open(fileString, "a")
    else:
        returnFile = open(fileString, "a+")
    return returnFile.name


def exitMenu(exitcode):
    if exitcode == "exit":
        print("Emergency exit.")
        exit(1)

def runFile(filename):
    print("Running file....")
    #runs the file the user has chosen
    if filename != "start.py":
        print("Output from \"", filename, "\"...")
        os.system(filename)
    else:
        print("You cannot run a file prior to creating one, call open file and write some code in it first.")