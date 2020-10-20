import speech_recognition as sr
import Listen as l
import re
filename = ""







#to be able to correct input things inside a print statement like print(x)
def print_in_file():
    print("Is the thing you want to print a string?")
    isitString = l.listen()
    print(isitString)
    # if it is a string it needs to have double quotes.
    if (isitString == "yes"):
        print("Enter your string to be printed.")
        print_text = l.listen()
        # print("hello")
        print_text = "\n" + "print(\"" + print_text + "\")"
        f = open(filename, "a")
        f.write(print_text)


    # if its not a string it should not have double quotes.
    if (isitString == "no"):
        print("Enter your non-string to be printed.")
        print_text = l.listen()
        f = open(filename, "a")
        print_text = "\n" + "print(" + print_text + ")"
        f.write(print_text)





#Must call this first.
def openFile():
    r = sr.Recognizer()
    mic_list = sr.Microphone.list_microphone_names
    global filename
# Exception handling to handle
# exceptions at the runt
    try:
    # use the microphone as source for input.
        with sr.Microphone() as source2:
            print("Say your filename")
            # wait for a second to let the recognizer
            # the surrounding noise level
            MyText = l.listen()
            MyText = re.sub(r"\s+", "", MyText, flags=re.UNICODE)
            MyText1 = MyText + ".py"
            f = open(MyText1, "w")
            filename = MyText1
            print("File " + MyText1 + " has been created.")
            return MyText1

    except sr.RequestError as e:
        print("Could not request results; {0}".format(e))

    except sr.UnknownValueError:
        print("unknown error occured")




def variableDeclaration():
    try:
        r = sr.Recognizer()
        # use the microphone as source for input.
        with sr.Microphone() as source:

            # wait for a second to let the recognizer
            # the surrounding noise level
            r.adjust_for_ambient_noise(source, duration=0.2)
            print("Variable Name: <input name> ")

            # listens for the user's input
            audio2 = r.listen(source)

            # Using google to recognize audio
            varText = r.recognize_google(audio2)
            tempvar = varText.lower()
            print("Variable Name: ", tempvar)
            r.adjust_for_ambient_noise(source, duration=0.2)
            print("Value: <input value>")


            audio3 = r.listen(source)


            # Using google to recognize audio
            tempVal = r.recognize_google(audio3)
            tempVal = tempVal.lower()
            print("Value: ", tempVal)
            printText = "\n" + tempvar + " = " + tempVal
            f = open(filename, "a")
            f.write(printText)

    except sr.RequestError as e:
        print("Could not request results; {0}".format(e))

    except sr.UnknownValueError:
        print("unknown error occured")
    return tempvar + " = " + tempVal