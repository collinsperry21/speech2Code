import Listen as l


def writeFile(filename):


    #   Currently a conditional to make sure we aren't messing with our own files. Destroy this later
    if filename == "main.py" or filename == "functions.py" or filename == "listen.py" or filename == "write.py":
        print("CRITICAL ERROR. ATTEMPTING TO OVERWRITE SOURCE CODE. EXITING...")
        exit(1)
    # if not empty then replace whole file with everything inside file buffer







    # Write Loop
    while 1:
        file = open(filename, "a+")

        print("Current file looks like:")
        print(file.read())


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

        if text == "string" or text == "strength":
            print("Enter the contents of your string")
            text = l.listen()

            file.write("print(" + "\"" + text + "\"" + ")")
            print("String has been written...")
            file.write("\n")

        if text == "while loop" or text == "guadalupe":
            #


            print("Enter the conditional of the while loop")
            text = l.listen()
            if(text.find("less than")):
                print("We found it1!!!!!")
            parsedText = find_operator(text)
            print(parsedText)
            file.write( "while " + parsedText + ":" + "\n")
            while 1:
                # print, variable, assignment x=7 x= ,
                print("Entering the body of the while loop, say 'exit while loop' to break out of loop")
                print("1 - variable declaration/assignment")
                print("2 - print within the while loop")

                text = l.listen()

                print(text)

                if text == "exit while loop":
                    print("Exiting while loop....")
                    break

                if(text == "won" or text == "one" or text == "1"):
                    print("State your declaration/assignment")
                    text = l.listen()
                    bodyText = find_operator(text)
                    print("Variable has been written")

                    file.write("\t" + bodyText + "\n")

                if(text == "two" or text == "to" or text == "too" or text == "2"):
                    print("Are you printing a string or a variable?")
                    print("To exit print say 'exit print'")


                    while(1):
                        text = l.listen()
                        print("Audio Heard: " + text)
                        if text == "string":
                            print("Enter the contents of your string")
                            text = l.listen()
                            file.write("\t" + "print(" + "\"" + text + "\"" + ")" + "\n")
                            print("String has been written...")
                        if text == "variable":
                            print("Enter the contents of your variable")
                            text = l.listen()
                            file.write("\t" + "print("  + text + ")" + "\n")
                            print("Variable has been written...")
                        if text == "exit print":
                            print("Exiting print....")
                            break



    file.close()
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
        print("Please enter a valid file line in the file you wish to edit. (1-", count, ")")
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
    if(edited_line.find("equals") != -1):
        edited_line = edited_line.replace("equals", "=")
        print("test1")
    if(edited_line.find("plus") != -1):
        edited_line = edited_line.replace("plus", "+")
        print("test2")
    if(edited_line.find("minus") != -1):
        edited_line = edited_line.replace("minus", "-")
        print("test3")
    if(edited_line.find("asterisk") != -1 or edited_line.find("astrix") != -1) or edited_line.find("asterix") != -1:
        edited_line = edited_line.replace("asterisk", "*")
        edited_line = edited_line.replace("astrix", "*")
        edited_line = edited_line.replace("asterix", "*")
        print("test4")
    if(edited_line.find("divided") != -1):
        edited_line == edited_line.replace("divided", "/")
        print("test5")
    if (edited_line.find("modulus") != -1):
        edited_line == edited_line.replace("modulus", "%")
        print("test6")
    if(edited_line.find("greater than") != -1 and (edited_line.find("or equal to") == -1)):
        edited_line = edited_line.replace("greater than", ">")
        print("test7")
    if ( (edited_line.find("lesson") != -1 or edited_line.find("less than")) and (edited_line.find("or equal to") == -1)):
        edited_line = edited_line.replace("less than", "<")
        edited_line = edited_line.replace("lesson", "<")
        print("test8")
    if(edited_line.find("equal to") != -1 and (edited_line.find("greater than") == -1) and (edited_line.find("less than") == -1) ):
        edited_line = edited_line.replace("equal to", "=")
        print("test9")
    if (edited_line.find("less than or equal to") != -1):
        edited_line = edited_line.replace("less than or equal to", "<=")
        print("test10")
    if (edited_line.find("greater than or equal to") != -1):
        edited_line = edited_line.replace("greater than or equal to", ">=")
        print("test11")
    if (edited_line.find("not equal") != -1 and (edited_line.find("to") == -1)):
        edited_line = edited_line.replace("not equal", "!=")
        print("test12")
    if (edited_line.find("not equal to") != -1):
        edited_line = edited_line.replace("not equal to", "!=")
        print("test13")
    return edited_line


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



