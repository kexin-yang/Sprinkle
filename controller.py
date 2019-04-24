import random
from BubbleClass import *

def mousePressed(event,data):
    if data.introMode == True:
        if event.y> (0.5*data.height - 150) and event.y <(0.5*data.height + 150) \
                and event.x <(0.5*data.width + 200) and event.x >(0.5*data.width - 200):
            data.introMode = False
            data.speakMode = True
def keyPressed(event,data):
    pass
def timerFired(data):
    if data.speakMode == True:
        if data.time % 5 == 0:
            print("time to put")
            putBubble(data)
        checkIfHeard(data)
        data.time += 1
        for bubble in reversed(data.bubbles):
            if bubble.word == data.heardWord:
                data.bubbles = []

        # if data.time % 8 == 0:
        #     checkIfHeard(data)

def recognizeWords():
    r = sr.Recognizer()
    # line24-29,36-37 cited from internet, speech recognition module
    with sr.Microphone() as source:
        print("Say something");
        audio = r.listen(source)
        print("Time Over")
    try:
        spoken = r.recognize_google(audio).lower()
        return spoken
    except:
        pass;

def listen(data):
    # this function record what is heard
    r = sr.Recognizer()
    with sr.Microphone() as source:
        data.speakingInstruction = "Say a word in the bubble!"
        print("speakingInstruction",data.speakingInstruction)
        audio = r.listen(source)
        data.speakingInstruction = "wait"
    try:
        spoken = r.recognize_google(audio).lower()
        return spoken
    except:
        pass

def checkIfHeard(data):
    # this function check if we hear any words in the bubble
    data.speakingInstruction = "Say a word in the bubble!"
    spoken = hearWords.recognizeWords()
    print("spoken",spoken)
    if spoken == None:
        data.hearMessage = "We didn't hear what you say, try again!"
        #data.speakingInstruction = ""
        print(data.hearMessage)
    elif spoken in data.words:
        data.hearMessage = "You spoke '%s' correctly!" % spoken
        #data.speakingInstruction = ""
        data.heardWord = spoken
        data.words.remove(spoken)
        print(data.words)
        bubbleBurst(data)
    else:
        data.hearMessage = "Did you said '%s'? \n Try again by saying words in the bubble!" % spoken
        #data.speakingInstruction = ""
        print(data.hearMessage)

def bubbleBurst(data):
    pass

def putBubble(data):
    print("??")
    # this function places bubble in the data
    for i in range(len(data.words)):
        print(i)
        speedLow, speedHigh = 8,12
        cx =  (1/(len(data.words)+1))*data.width * (i+1)
        cy = 0.25 * data.height
        r = 30
        #!! r can change later
        color = random.choice(["cyan","pink","yellow","green","gold","white"])
        #!! can change later
        direction = random.choice([[0, 1], [0, -1], [1, 1], [1, -1], [1, 0], [-1, 0], [-1, -1], [-1, 1]])
        speed = random.randint(speedLow,speedHigh)
        bubble = Bubble(cx,cy,r,color,direction,data.words[i])
        data.bubbles.append(bubble)
        print("bubb",data.bubbles)