import speech_recognition as sr


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
            MyText = r.recognize_google(audio2)
            tempvar = MyText.lower()
            print("Variable Name: ", tempvar)
            r.adjust_for_ambient_noise(source, duration=0.2)
            print("Value: <input value>")

            audio3 = r.listen(source)


            # Using google to recognize audio
            tempVal = r.recognize_google(audio3)
            tempVal = tempVal.lower()
            print("Value: ", tempVal)


    except sr.RequestError as e:
        print("Could not request results; {0}".format(e))

    except sr.UnknownValueError:
        print("unknown error occured")
    return tempvar + " = " + tempVal
