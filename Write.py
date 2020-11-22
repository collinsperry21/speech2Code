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

        if text == "if" or text == "elf" or text == "of" or text == "f" or text == "it":
            print("Entering 'if' statement")
            ifString = ifstate(filename)
            file.write(ifString)
            file.write("\n")

        if text == "string":
            print("Enter the contents of your string")
            text = l.listen()
            file.write( "print(" + "\"" + text + "\"" + ")" )
            print("String has been written too...")
            file.write("\n")

        if text == "while loop" or text == "guadalupe":
            print("Enter the conditional of the while loop")
            text = l.listen()
            if (text.find("less than")):
                print("We found it1!!!!!")
            parsedText = find_operator(text)
            print(parsedText)
            file.write("while " + parsedText + ":" + "\n")
            while 1:
                print("Entering the body of the while loop, say 'exit while loop' to break out of loop")
                text = l.listen()
                bodyText = find_operator(text)
                if text == "exit while loop":
                    print("Exiting while loop....")
                    break
                file.write("\t" + bodyText + "\n")



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
    if (tempvar == "why"):
        tempvar = "y"
    if (tempvar == "see"):
        tempvar = "z"
    if (tempvar == "eye"):
        tempvar = "i"
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

def ifstate(filename):
    currentline = len(filename.splitlines())
    print("What kind of 'if' statement would you like to use")
    print("1: if statement\n"
          "2: if-else statement\n")
    print("Say which number you would like")
    option = l.listen()
    #CTNoption = change_to_number(option)

    print("The option selected: ", option)
    if (option == "1" or option == "one" or option == "won" or option == "wan" or option == "on"):
        print("Entering regular 'if' statement")
        print("Please state the conditional you want in the if statement")
        print("You are writing to line#:", currentline)
        tempIf = l.listen()
        condOp = find_operator(tempIf) #if (x > 5)
        print("if ("+ condOp + ") :")
        first = "if (" + condOp + ") :\n"
        print("What would you like to go in the body of the if statement")
        print ("Options are: \n Variable \n Print string \n print variable  \n While Loop \n Exit If Statement")
        option1 = l.listen()
        printstr = ""
        counter = 0
        while(option1 != "exit if statement"):
            if(counter > 0):
                print("Options are: \n Variable \n Print string \n print variable  \n While Loop \n Exit If Statement")
                option1 = l.listen()
            if (option1 == "variable"):
                print("Entering variable creation")
                printstr += "\t" + variableDeclaration(filename) + "\n"
            if(option1 == "print string"):
                print("Say what string you would like to print")
                print1 = l.listen()
                print("Your string is: ", print1)
                printstr += "\tprint(" + "\"" + print1 + "\"" + ")" + "\n"
            if (option1 == "print variable"):
                print("Say which variable you want printed \n")
                print1 = l.listen()
                if (print1 == "why"):
                    print1 = "y"
                print("Your selected variable is: ", print1)
                printstr += "\tprint(" + print1 + ")" + "\n"
            if (option1 == "exit if statement"):
                print("Exiting the if statement")
            counter+=1
        return first + printstr

    elif (option == "2" or option == "two" or option == "to" or option == "too"):
        print("Entering option 2: if-else statement")
        print("Please state the conditional you want in the if-else statement")
        print("You are writing to line#:", currentline)

        tempIf = l.listen()
        condOp = find_operator(tempIf)  # if (x > 5)
        print("if (" + condOp + ") :")
        print("What would you like to have in the body of the 'if' portion")
        first = "if (" + condOp + ") :\n"
        print("Options are: \n Variable \n Print string \n print variable  \n  Exit If Statement")
        option1 = l.listen()
        printstr = ""
        counter = 0
        while (option1 != "exit if statement"):
            if (counter > 0):
                print("Options are: \n Variable \n Print string \n print variable \n Exit If Statement")
                option1 = l.listen()
            if (option1 == "variable"):
                print("entered variable")
                printstr += "\t" + variableDeclaration(filename) + "\n"
            if (option1 == "print string"):
                print("Say what string you would like to print")
                print1 = l.listen()
                print("you said: ", print1)
                printstr += "\tprint(" + "\"" + print1 + "\"" + ")" + "\n"
            if (option1 == "print variable"):
                print("Say which variable you want printed \n")
                print1 = l.listen()
                if (print1 == "why"):
                    print1 = "y"
                print("Your selected variable is: ", print1)
                printstr += "\tprint(" + print1 + ")" + "\n"
            if (option1 == "exit if statement"):
                print("Exiting the if statement")
            counter += 1
        print("Entering the else portion\n Select and option for the body of the 'else' portion")
        print("Options are: \n Variable \n Print string \n print variable  \n Exit If Statement")
        elseop = l.listen()
        elsestr = ""
        counter = 0
        while (elseop != "exit if statement"):
            if (counter > 0):
                print("Options are: \n Variable \n Print string \n print variable  \n Exit If Statement")
                elseop = l.listen()
            if (elseop == "variable"):
                print("entered variable")
                elsestr += "\t" + variableDeclaration(filename) + "\n"
            if (elseop == "print string"):
                print("Say what string you would like to print")
                print1 = l.listen()
                print("you said: ", print1)
                elsestr += "\tprint(" + "\"" + print1 + "\"" + ")" + "\n"
            if (elseop == "print variable"):
                print("Say which variable you want printed \n")
                print1 = l.listen()
                if(print1 == "why"):
                    print1 = "y"
                print("Your selected variable is: ", print1)
                elsestr += "\tprint(" + print1 + ")" + "\n"
            if (elseop == "exit if statement"):
                print("Exiting the if statement")
            counter += 1
        return first + printstr + "else :\n" + elsestr
