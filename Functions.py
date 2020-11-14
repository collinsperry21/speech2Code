import Listen as l
import os


def helper(filename):
    tempfile = filename
    #filename.close()
    theFile = open('HelpText.txt', "r")
    print(theFile.read())
    os.startfile('HelpText.txt')
    print("Say exit to return to the main menu")
    BacktoMenu = l.listen()
    if BacktoMenu == "exit help" or "exit hell":
        print("closing help manual and returning to main")
        os.system('TASKKILL /F /IM notepad.exe')
        theFile.close()



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

def runFile(filename):
    print("Running file....")
    # runs the file the user has chosen
    if (len(filename) != 0):
        os.system(filename)


    else:
        print("You cannot run a file prior to creating one, call open file and write some code in it first.")