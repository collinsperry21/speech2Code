import Listen as l

def writeFile(filename):

    #   Currently a conditional to make sure we aren't messing with our own files. Destroy this later
    if filename == "main.py" or filename == "functions.py" or filename == "listen.py" or filename == "write.py":
        print("CRITICAL ERROR. ATTEMPTING TO OVERWRITE SOURCE CODE. EXITING...")
        exit(1)
    file = open(filename, "a+")
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

        if text == "variable":
            print("Entering variable...")
            assignString = variableDeclaration(filename)
            file.write(assignString)
            file.write("\n")

        if text == "string":
            print("Enter the contents of your string")
            text = l.listen()
            file.write( "print(" + "\"" + text + "\"" + ")" )
            print("String has been written too...")
            file.write("\n")

        print("Finished parsing text: " + text)


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
    currentline = len(filename.splitlines())
    print("You are writing to line#:", currentline)
    print("Please say your variable name: ")
    tempvar = l.listen()
    print("Variable Name: ", tempvar)
    print("Value: ")
    tempVal = l.listen()
    print("Value: ", tempVal)
    return tempvar + " = " + tempVal





def editFile(filename):
    print("Editing file...." + '\n')
    print("Say the line number of the file you want to edit: ")
    count = len(open(filename).readlines())
    lineNumber1 = l.listen()
    while (1):
        try:
            anInt = int(change_to_number(lineNumber1))
            print("LOOPING")
            if(anInt > 0 and anInt < 999):
                lineNumber1 = anInt
                break
        except ValueError:
            print("Please enter a valid number:")
            lineNumber1 = l.listen()
            continue

    lineNumber1 = int(lineNumber1)
    while( lineNumber1 > count or lineNumber1 < 1 ):
        print("Please enter a valid file line number in the file you wish to edit. (1-n)")
        lineNumber = l.listen()


    my_file1 = open(filename, 'r')
    string_list = my_file1.readlines()
    my_file1.close()
    my_file = open(filename, 'w')
    print(len(string_list))
    print("The line number is: " + str(lineNumber1))
    print(type(lineNumber1))
    print("File Line being edited is: " + string_list[lineNumber1-1])

    print("Resay your edited line: ")
    newLine = l.listen()



    #need to replace "equals" with "="
    newLine = find_operator(newLine)


    string_list[lineNumber1-1] = newLine
    print("Line has been edited...")


    for i in range (len(string_list)):
        myString = string_list[i]
        print(myString)
        my_file.write(myString + "\n")


    my_file.close()


def find_operator(edited_line):
    if(edited_line.find("equals")):
        return edited_line.replace("equals", "=")
    elif(edited_line.find("plus")):
        return edited_line.replace("plus", "+")
    elif(edited_line.find("minus")):
        return edited_line.replace("minus", "-")
    elif(edited_line.find("times")):
        return edited_line.replace("times", "*")
    elif(edited_line.find("divided")):
        return edited_line.replace("divided", "/")
    elif (edited_line.find("modulus")):
        return edited_line.replace("modulus", "%")


def change_to_number(stringy):

    if(stringy == "won" or stringy == "one"):
        return 1

    elif(stringy == "two" or stringy == "too" or stringy == "to"):
        return 2

    elif(stringy == "three" or stringy == "free" ):
        return 3

    elif(stringy == "for" or stringy == "four" or stringy ==  "fore"):
        return 4

    elif(stringy == "five"):
        return 5

    elif(stringy == "six" or stringy == "sex"):
        return 6

    elif(stringy == "seven"):
        return 7

    elif(stringy == "ate" or stringy == "eight"):
        return 8
    elif(stringy == "nine" or stringy == "nein"):
        return 9

    else:
        return stringy



