# Python program to translate 
# speech to text and text to speech 


import speech_recognition as sr
import pyttsx3

# Initialize the recognizer  
r = sr.Recognizer()
mic_list = sr.Microphone.list_microphone_names()
print(mic_list)

# Function to convert text to 
# speech

#def SpeakText(command):
#   Initialize the engine
#   engine = pyttsx3.init()
#   engine.say(command)
#   engine.runAndWait()


# Loop infinitely for user to 
# speak 

while (1):

    # Exception handling to handle 
    # exceptions at the runtime 
    try:

        # use the microphone as source for input. 
        with sr.Microphone() as source2:

            # wait for a second to let the recognizer 
            # the surrounding noise level
            r.adjust_for_ambient_noise(source2, duration=0.2)

            # listens for the user's input  
            audio2 = r.listen(source2)

            # Using google to recognize audio
            MyText = r.recognize_google(audio2)
            MyText = MyText.lower()


            #Voice command to stop running.
            if(MyText == "end speech to text" or MyText ==  "and speech to text"):
                break;

            #gonna need to do some string parsing here
            #variable appleseed equals (or equal) 6
            if (MyText[0:7] == 'variable'):
                MyText = MyText[0:8]

            #would like to be able to make variables camelcase
            capital = 'capital'
            if capital in MyText:
                someText = MyText.split(" ")
                print(someText)
                capIndex = someText.index(capital)
                print(capIndex)
                capString = someText[capIndex+1].capitalize()
                someText[capIndex+1] = capString
                someText.remove("capital")
                print("after upper: ")
                #someText.remove("")
                print(someText)
                MyText =  "".join(someText)
                print(MyText)

            print("Audio heard: " + MyText)
            print("variableParse")

            print("variableParse")

    except sr.RequestError as e:
        print("Could not request results; {0}".format(e))

    except sr.UnknownValueError:
        print("unknown error occured") 
