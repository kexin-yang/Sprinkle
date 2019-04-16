# 考虑把上面的函数写到bubble class 里，并且判断是否和应该有的单词一样，如果有的话，list里面东西-1，没有的话展示错在哪


import speech_recognition as sr

def call():
    result = recognizeWords()
    #print(result)
    #print(result, type(result))
    if result == None:
        message = "We didn't hear what you say, try again!"
        print(message)
        return message
    elif result[0] == True:
        message = "You spoke %s correctly!" %result[1]
        print(message)
        return message
    else:
        message = "Did you said '%s'? Try again by saying words in the bubble!"%result
        print(message)
        return message

def recognizeWords():
    #word = ["apple","i","really","like"]
    r = sr.Recognizer()
    # cited from internet(line24-29,36-37)
    with sr.Microphone() as source:
        print("Say something");
        audio = r.listen(source)
        print("Time Over")
    try:
        spoken = r.recognize_google(audio).lower()
        return spoken
    except:
        pass;

recognizeWords()