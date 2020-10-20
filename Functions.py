import speech_recognition as sr


filename = ""

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
            r.adjust_for_ambient_noise(source2, duration=0.2)

            # listens for the user's input
            audio2 = r.listen(source2)

            # Using google to recognize audio
            MyText = r.recognize_google(audio2)
            MyText = MyText.lower()
            "".join(MyText.split())
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
            printText = tempvar + " = " + tempVal
            f = open(filename, "a")
            f.write(printText)

    except sr.RequestError as e:
        print("Could not request results; {0}".format(e))

    except sr.UnknownValueError:
        print("unknown error occured")
    return tempvar + " = " + tempVal