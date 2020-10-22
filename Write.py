import Listen as l

def writeFile(filename):

    #   Currently a conditional to make sure we aren't messing with our own files. Destroy this later
    if filename == "main.py" or filename == "functions.py" or filename == "listen.py" or filename == "write.py":
        print("CRITICAL ERROR. ATTEMPTING TO OVERWRITE SOURCE CODE. EXITING...")
        exit(1)
    file = open(filename, "w+")
    print("Current file looks like:")
    print(file.read())
    # Write Loop
    while 1:
        print("What would you like to write?")
        print("Waiting for input...")
        text = l.listen()

        if text == "exit right" or text == "exit write":
            print("Exiting write...")
            file.close()
            break

        if text == "comment" or text == "common" or text =="comments":
            print("Commenting...")
            comment(filename)
        if text == "assign":
            print("Entering assignment...")
            assignString = variableDeclaration(filename)
            file.write(assignString)


def comment(filename):
    while 1:
        currentline = len(filename.splitlines())
        print("You are commenting to line#:", currentline)
        print("")
        commentstring = l.listen()
        filename.write("# " + commentstring + "\n")
        print("Would you like to make another line of comments? (Say <yes> / <no>)")
        choice = l.listen()
        if choice == "yes":
            comment(filename)
        elif choice == "no":
            break
        else:
            print("Unable to process request. Input heard: ", choice)
            continue


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
