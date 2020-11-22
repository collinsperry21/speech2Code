import Listen as l


def writeFile(filename):

    # Write Loop
    while 1:
        file = open(filename, "a+")
        print("Current file looks like: \n")
        print(file.read())
        print("What would you like to write?")
        print("Waiting for input...")
        text = l.listen()

        if text == "exit right" or text == "exit write":
            print("Exiting write...")
            file.close()
            break

        if text == "comment" or text == "common" or text == "comments":
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
            file.write("print(" + "\"" + text + "\"" + ")" )
            print("String has been written too...")
            file.write("\n")

        if text == "for loop" or text == "orally":
            print("Entering For Loop...")
            file.close()
            forLoop(filename)


        file.close()
        print("Finished parsing text: " + text)



def forLoop(filename):
    print("\n ")
    print("Give a variable name to iterate on")
    varName = l.listen()
    print("variable given =", varName)
    print("Give a # of times to run this loop")
    rangeNum = l.listen()
    temp = change_to_number(rangeNum)
    forString = "for " + varName + " in range(1," + temp + ")"
    file = open(filename, "a+")
    file.write(forString)
    print("Say the option you would like to do")
    options = "Options are: \n Variable \n Print string \n print variable \n Exit For Loop"
    print(options)
    option1 = l.listen()
    printstr = ""
    counter = 0
    while (option1 != "exit for loop"):
        if (counter > 0):
            print(options)
            option1 = l.listen()
        if (option1 == "variable"):
            print("entered variable")
            printstr += "\t" + variableDeclaration(filename) + "\n"
        if (option1 == "print string"):
            print("say what you want printed")
            print1 = l.listen()
            printstr += "\tprint(" + "\"" + print1 + "\"" + ")" + "\n"
        if (option1 == "print variable"):
            print("say which variable you want printed \n")
            print1 = l.listen()
            printstr += "\tprint(" + print1 + ")" + "\n"
        if (option1 == "exit for loop"):
            print("Exiting the For Loop")
        counter += 1

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
    lineNumber = l.listen()
    print("INPUT HEARD: " + lineNumber)
    lineNumber1 = int(change_to_number(lineNumber))
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
    string_list[lineNumber1-1] = newLine
    print("Line has been edited...")


    for i in range (len(string_list)):
        myString = string_list[i]
        print(myString)
        my_file.write(myString)
        my_file.write("\n")
    my_file.close()

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

