# Python program to translate 
# speech to text

import Functions as f
import os as o
import Listen as l
import Write as w

filepath = str(o.path.abspath(o.getcwd()))

#Kill any previous start files

if o.path.exists("start.py"):
    o.remove("start.py")

#Create a base working space
openfile = open("start.py", "w+")
o.chmod("start.py", 0o700)
openfile.close()
#openfile.write("#This file will self-destruct everytime speech2Code is launched\n")
#openfile.write("#Open/Create a file using \"open file\" \n")
currentfile = openfile.name
#print(currentfile)


print("\nWelcome to speech2Code!")
print("Say <HELP> if this is your first time or need a refresher on the functionality.")
print("If not, happy coding !\n")
print("~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")

# Loop infinitely for user to
# speak
while 1:

    # Current status output
    print("\n~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~Main Menu~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")
    print("Current working file: ", currentfile)
    print("Current working directory: ", o.getcwd())
    print("Waiting for voice input...")
    # use the microphone as source for input.
    MyText = l.listen()

    # Voice command to stop running.
    if MyText == "end speech to code" or MyText == "and speech to code":
        print("Exiting speech2code...")
        break

#   Helper Function
    if MyText == 'help':
        print("Launching <help>...")
        f.helper(currentfile)
        continue

#   Variable Assignment Function
    #if MyText == 'variable':
     #   print("Entering variable assignment...")
      #  varString = f.variableDeclaration(currentfile)
       # print("Wrote to ", openfile.name, " ", varString)

#   Open File Function
    if MyText == "open file":
        if currentfile != "start.py":
            print("Close current file before opening another")
            print("Currently in ", currentfile)
            continue
        print("Entering <open file>...")
        currentfile = f.openFile()

#   Comment Function
    if MyText == "write" or MyText == "right" or MyText == "rite" or MyText == "bright":
        if currentfile == "start.py":
            print("Warning!")
            print("You are writing to start.py and this will be deleted on speech2Code's next launch")
            print("Consider opening another file using <open file> from the menu")
        print("Entering write for current file... ", currentfile)
        w.writeFile(currentfile)

    if MyText == "read" or MyText == "reed":
        print(openfile.name)
        print("Reading File...")
        print(openfile.read())
        continue

    if (MyText == "run file"):
        f.runFile(currentfile)



    if (MyText == "edit file" or MyText == "pedophile"):
        w.editFile(currentfile)

    if (MyText == "switch file"):
        print("Enter the already created file you wish to switch too")
        MyText = l.listen()
        MyText = MyText + ".py"
        currentfile = MyText

    #    would like to be able to make variables camelcase
#    Ode to Tristan
    capital = 'capital'
    if capital in MyText:
        someText = MyText.split(" ")
        print(someText)
        capIndex = someText.index(capital)
        print(capIndex)
        capString = someText[capIndex+1].capitalize()
        someText[capIndex+1] = capString
        someText.remove(capital)
        print("after upper: ")
        #someText.remove("")
        print(someText)
        MyText = "".join(someText)
        print(MyText)
#   Resume Useful code
    print("Finished Parsing: < " + MyText, " >")

#consider commenting this out in the furture as we close it immediately
openfile.close()
