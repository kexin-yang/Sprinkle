import speech_recognition as sr

def call(data):
    result = recognizeWords()
    #print(result)
    #print(result, type(result))
    if result == None:
        data.message = "We didn't hear what you say, try again!"
        print(message)
    elif result[0] == True:
        data.message = "You spoke %s correctly!" %result[1]
        print(datamessage)
    else:
        data.message = "Did you said '%s'? Try again by saying words in the bubble!"%result
        print("Did you said '%s'? Try again by saying words in the bubble!"%result)

def recognizeWords():
    word = ["apple","I","really","like"]
    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("Say something");
        audio = r.listen(source)
        print("Time Over")
    try:
        spoken = r.recognize_google(audio).lower()
        if spoken in word:
            print("Awesome, you spoke one word correctly!")
            return (True,spoken)
        #print(type(spoken))
        return spoken
        print("TEXT:" + r.recognize_google(audio));
    except:
        pass;

