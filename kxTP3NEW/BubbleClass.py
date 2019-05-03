import random
import speech_recognition as sr
import hearWords
import music
import numpy
from tkinter import *
from PIL import ImageTk, Image
import vocab

class Bubble():
    # define bubble
    def __init__(self,cx,cy,r,color,direction,word):
        # a bubble has a position, size, color and a word in it
        self.cx = cx
        self.cy = cy
        self.r = r
        self.color = color
        self.direction = direction
        self.word = word

    # cite from my own homework5,15112
    def draw(self, canvas):
        # draw the bubbles on canvas
        canvas.create_oval(self.cx-self.r,self.cy-self.r,self.cx+self.r, self.cy+self.r, fill= self.color, outline = "")
        canvas.create_text(self.cx,self.cy,text = self.word,fill="saddle brown", font="Comic\ Sans\ MS 28 bold")

# Graphic function

def generateWords():
    # this function provide a pool of words that can make senteces, and randomly choose from them
    wordPool = (["i", "can", "play", "football"],
                ["they", "usually", "eat", "dinner", "together"])
    word = random.choice(wordPool)
    return word

def init(data):
    data.score = 0
    data.bubbles = []
    data.words = generateWords()
    data.time = 0
    # different modes
    data.introMode = True
    data.speakMode = False
    data.sortMode = False
    # speaking mode attribute
    data.hearMessage = ""
    data.heardWord = ""
    data.speakingInstruction = ""
    # button position
    data.sortx1, data.sorty1, data.sortx2, data.sorty2 \
        = data.width * 0.1, data.height * 0.75, data.width * 0.2, data.height * 0.85
    data.homex1, data.homey1, data.homex2, data.homey2 \
        = data.width * 0.8, data.height * 0.75, data.width * 0.9, data.height * 0.85
    data.level1x1, data.level1y1, data.level1x2, data.level1y2 \
    = data.width * 0.35, data.height * 0.75, data.width * 0.45, data.height * 0.85
    data.level2x1, data.level2y1, data.level2x2, data.level2y2 \
    = data.width * 0.55, data.height * 0.75, data.width * 0.65, data.height * 0.85
    # sorting mode attribute
    data.level = 1


# CONTROLLER

def timerFired(data):
    if data.speakMode == True:
        if data.time % 5 == 0:
            putBubble(data)
        data.time += 1
        for bubble in reversed(data.bubbles):
            if bubble.word == data.heardWord:
                data.bubbles = []
        if data.time % 8 == 0:
            checkIfHeard(data)

def recognizeWords():
    # besides the data.speakingInstruction, this function is cited from the python speech recognition module
    r = sr.Recognizer()
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
    # besides the data.speakingInstruction, this function is cited from the python speech recognition module
    # this function record what is heard
    r = sr.Recognizer()
    with sr.Microphone() as source:
        data.speakingInstruction = "Say a word in the bubble!"
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
    if spoken == None:
        data.hearMessage = "We didn't hear what you say, try again!"
        #data.speakingInstruction = ""
    elif spoken in data.words:
        data.hearMessage = "You spoke '%s' correctly!" % spoken
        #data.speakingInstruction = ""
        data.heardWord = spoken
        data.words.remove(spoken)
        checkIfEnd1(data)
        data.score += 3
    else:
        data.hearMessage = "Did you said '%s'? \n Try again by saying words in the bubble!" % spoken
        #data.speakingInstruction = ""

def checkIfEnd1(data):
    if len(data.words) == 0:
        data.speakMode = False
        data.sortMode = True

def putBubble(data):
    # this function places bubble in the data, borrow the idea from my own homework 5- OOPY animation.
    for i in range(len(data.words)):
        speedLow, speedHigh = 8,12
        cx =  (1/(len(data.words)+1))*data.width * (i+1)
        cy = 0.25 * data.height
        r = random.randint(30,60)
        # the color codes cited from the website http://www.science.smith.edu/dftwiki/index.php/Color_Charts_for_TKinter
        color = random.choice(["floral white", "old lace", "lemon chiffon", "mint cream", "misty rose", \
                               "lavender blush", "azure", "alice blue", "lavender","pink", "light yellow",\
                               "light salmon", "salmon", "thistle1"])
        direction = random.choice([[0, 1], [0, -1], [1, 1], [1, -1], [1, 0], [-1, 0], [-1, -1], [-1, 1]])
        speed = random.randint(speedLow,speedHigh)
        bubble = Bubble(cx,cy,r,color,direction,data.words[i])
        data.bubbles.append(bubble)

#=======================================================================================================================
# sort page

def drawIntroScene(canvas,data):
    if data.introMode == True:
        # draw background
        canvas.create_rectangle(0, 0, data.width, data.height, fill="light yellow")

        # img = ImageTk.PhotoImage(Image.open('pictures/fourKids.gif').resize(25,25))
        # img1 = PhotoImage(file='pictures/skySand.gif')
        # # img = img.subsample(2, 2)
        # canvas.create_image(0.5 * data.width, 500, image=img1)
        # label1 = Label(image=img1)
        # label1.image = img1
        # label1.pack()


        img = PhotoImage(file='pictures/twoGirls.gif')
        # img = img.subsample(2, 2)
        canvas.create_image(0.5 * data.width, 500, image=img)
        label = Label(image=img)
        label.image = img
        label.pack()


        # img = PhotoImage(file='pictures/fourKids.gif')
        # img = img.subsample(2,2)
        # canvas.create_image(0.5*data.width, 500,  image=img)
        # label = Label(image=img)
        # label.image = img
        # label.pack()

        canvas.create_text(data.width * 0.5, 0.1 * data.height,
                           fill="salmon", font="Comic\ Sans\ MS 36 bold",
                           text="Welcome to Sprinkle! \nThis is a game for teaching early literacy!")

        def drawSpeakButton():
            canvas.create_rectangle(data.sortx1, data.sorty1, data.sortx2, data.sorty2, fill="light yellow",
                                    outline="chocolate3")
            canvas.create_text(data.width * 0.15, 0.8 * data.height,
                               fill="salmon", font="Comic\ Sans\ MS 20 bold", text="SPEAK\n GAME")

        def drawSortButton():
            canvas.create_rectangle(data.homex1, data.homey1, data.homex2, data.homey2, fill="mint cream",
                                    outline="chocolate")
            canvas.create_text(data.width * 0.85, 0.8 * data.height,
                               fill="salmon", font="Comic\ Sans\ MS 20 bold", text="SORT\nGAME")
        # draw start button
        drawSpeakButton()
        drawSortButton()
def drawSpeakScene(canvas,data):
    def drawSortButton(canvas,data):
        canvas.create_rectangle(data.sortx1, data.sorty1, data.sortx2, data.sorty2, fill="light yellow", \
                                outline = "chocolate3")
        canvas.create_text(data.width * 0.15, 0.8 * data.height,
                           fill="salmon", font="Comic\ Sans\ MS 20 bold", text="SORT\n GAME")
    def drawHomeButton(canvas,data):
        canvas.create_rectangle(data.homex1, data.homey1, data.homex2, data.homey2, fill="mint cream", \
                                outline = "chocolate")
        canvas.create_text(data.width * 0.85, 0.8 * data.height,
                           fill="salmon", font="Comic\ Sans\ MS 20 bold", text="HOME")

    if data.speakMode == True:
        canvas.create_rectangle(0, 0, data.width, data.height, fill="lavender blush")
        img = PhotoImage(file='pictures/onegirl.gif')
        img = img.subsample(5, 5)
        canvas.create_image(0.2 * data.width, 500, image=img)
        label = Label(image=img)
        label.image = img
        label.pack()
        for bubble in data.bubbles:
            bubble.draw(canvas)
        canvas.create_text(data.width / 2, data.height-20, anchor="n", fill="yellow",
                           font="Arial 24 bold", text="Score: " + str(data.score))
        canvas.create_text(data.width * 0.5, 0.42 * data.height,
                           fill="saddle brown", font="Comic\ Sans\ MS 40 bold", text=data.speakingInstruction)
        canvas.create_text(data.width*0.5, 0.6 * data.height,
                           fill="NavajoWhite4", font="Comic\ Sans\ MS 30 bold", text=data.hearMessage)
        # draw HOME button
        drawHomeButton(canvas,data)

def drawSortScene(canvas,data):
    if data.sortMode == True:
        sortMode(canvas,data)

def drawTextbox(canvas,data):
    if data.textBoxFlag == False:
        e1 = Entry(canvas, width=50, bg="white", foreground="brown")
        canvas.create_window(300, 450, window=e1, height=80, width=300)
        data.textBoxFlag = True

def redrawAll(canvas,data):
    if data.sortMode == True:
        sortMode(canvas, data)
    if data.introMode == True:
        drawIntroScene(canvas, data)
    if data.speakMode == True:
        drawSpeakScene(canvas,data)

#################################################################
# part of the run function is cited from course note
# specifically, in the redrawAllWrapper, timerFiredWrapper and
# class Struct there are some codes borrowed from class notes
#################################################################

def sortMode(canvas,data):
    # I learn how to play music from this website https://stackoverflow.com/questions/307305/play-a-sound-with-python
    def playMusic():
        music.playMusic3()
    e1 = Entry(canvas, width=50, bg="white", foreground="brown")
    canvas.create_window(500,450, window = e1,height= 80, width=300)
    canvas.create_rectangle(0, 0, data.width, data.height, fill="old lace")
    canvas.create_rectangle(0.5* data.width - 230, 0.5* data.height - 50,0.5* data.width + 230,0.5* data.height + 150,
                            fill="misty rose", outline = "")

    canvas.create_text(data.width, data.height / 7, fill="salmon", anchor = "e", font="Comic\ Sans\ MS 20 bold",\
                       text="Be creative! \nWe are checking the grammar, \nnot the plausibility:) ")
    # img = PhotoImage(file='pictures/twoGirls.gif')
    # #img = img.subsample(2, 2)
    # canvas.create_image(0.5 * data.width, 500, image=img)
    # label = Label(image=img)
    # label.image = img
    # label.pack()

    img = PhotoImage(file='pictures/fourKids.gif')
    img = img.subsample(3, 3)
    canvas.create_image(0.5 * data.width, 270, image=img)
    label = Label(image=img)
    label.image = img
    label.pack()


    canvas.create_text(data.width / 3, data.height / 7, fill="saddle brown", font="Comic\ Sans\ MS 26 bold",\
                       text="Please use the following words \nto make a grammatical sentence! \nType it in the box and click OK to check!")
    def drawSpeakButton():
        canvas.create_rectangle(data.sortx1, data.sorty1, data.sortx2, data.sorty2, fill="light yellow",\
                                outline = "chocolate3")
        canvas.create_text(data.width * 0.15, 0.8 * data.height,
                           fill="salmon", font="Comic\ Sans\ MS 20 bold", text="SPEAK\n GAME")
    def drawHomeButton():
        canvas.create_rectangle(data.homex1, data.homey1, data.homex2, data.homey2, fill="mint cream", \
                                outline = "chocolate")
        canvas.create_text(data.width * 0.85, 0.8 * data.height,
                           fill="salmon", font="Comic\ Sans\ MS 20 bold", text="HOME")
    def drawLevel1Button():
        canvas.create_rectangle(data.level1x1, data.level1y1, data.level1x2, data.level1y2 , fill="mint cream",\
                                outline = "chocolate")
        canvas.create_text(data.width * 0.4, 0.8 * data.height,
                           fill="salmon", font="Comic\ Sans\ MS 20 bold", text="Level1")
    def drawLevel2Button():
        canvas.create_rectangle(data.level2x1, data.level2y1, data.level2x2, data.level2y2 , \
                                fill="mint cream", outline = "chocolate")
        canvas.create_text(data.width * 0.6, 0.8 * data.height,
                           fill="salmon", font="Comic\ Sans\ MS 20 bold", text="Level2")
    drawHomeButton()
    drawLevel1Button()
    drawLevel2Button()

    def displayWords():
        if data.level == 1:
            words = vocab.generateSentence(1)
            canvas.create_text(data.width / 2, data.height / 2, anchor="s", fill="chocolate",
                       font="Comic\ Sans\ MS 26 bold", text='         '.join(words))
        if data.level == 2:
            words = vocab.generateSentence(2)
            newWords = list(words)
            for i in range(len(words)):
                if words[i] in vocab.pp1:
                    id = vocab.pp1.index(words[i])
                    newWords.remove(words[i])
                    newWords.append(vocab.pp2[id])
            canvas.create_text(data.width / 2, data.height / 2, anchor="s", fill="chocolate",
                       font="Comic\ Sans\ MS 20 bold", text='         '.join(newWords))
    def sortCheck():
        nonlocal canvas
        # the code about creating textbox and button have some reference from
        # https://www.python-course.eu/tkinter_entry_widgets.php (the line below)
        txt = e1.get()
        if data.level == 1:
            if vocab.checkGrammar(txt):
                data.score+=5
                canvas.after(100,sortMode(canvas, data))

        if data.level == 2:
            lst = txt.split()
            newPP = lst[-3]+lst[-2]+lst[-1]
            lst.pop()
            lst.pop()
            lst.pop()
            lst.append(newPP)
            newTxt = " ".join(lst)
            if vocab.checkGrammar(newTxt):
                data.score += 10
                canvas.after(100, sortMode(canvas,data))
    canvas.create_text(data.width / 2, data.height - 100, anchor="s", fill="salmon",
                       font="Arial 24 bold", text="Score: " + str(data.score))
    displayWords()
    checkButton = Button(canvas, text = 'OK', command=sortCheck)
    buttonWindow = canvas.create_window(450,530,window = checkButton)
    # the below button can play music
    musicButton = Button(canvas, text='Gimme some music!', command=playMusic)
    buttonWindow = canvas.create_window(550, 530, window=musicButton)

def runBubbles(width=1000, height=800):
    def redrawAllWrapper(canvas, data):
        canvas.delete(ALL)
        canvas.create_rectangle(0, 0, data.width, data.height,
                                fill='white', width=0)
        redrawAll(canvas, data)
        canvas.update()

    def mousePressedWrapper(event, canvas, data):
        if data.introMode == True:
            # back to sort page
            if event.y > data.homey1 and event.y < data.homey2 \
                    and event.x < data.homex2 and event.x > data.homex1:
                data.introMode = False
                data.speakMode = False
                data.sortMode = True
            # go to speak page
            if event.y > data.sorty1 and event.y < data.sorty2 \
                    and event.x < data.sortx2 and event.x > data.sortx1:
                data.introMode = False
                data.speakMode = True
                data.sortMode = False
                runBubbles()
            redrawAll(canvas,data)
        if data.sortMode == True:
            # back to intro page
            if event.y > data.homey1 and event.y < data.homey2 \
                    and event.x < data.homex2 and event.x > data.homex1:
                data.introMode = True
                data.speakMode = False
                data.sortMode = False
            # go to speak page
            if event.y > data.sorty1 and event.y < data.sorty2 \
                    and event.x < data.sortx2 and event.x > data.sortx1:
                data.introMode = False
                data.speakMode = True
                data.sortMode = False
                runBubbles()
            if event.y > data.level1y1 and event.y < data.level1y2 \
                    and event.x < data.level1x2 and event.x > data.level1x1:
                data.level = 1
                canvas.after(100, sortMode(canvas, data))
            if event.y > data.level2y1 and event.y < data.level2y2 \
                    and event.x < data.level2x2 and event.x > data.level2x1:
                data.level = 2
                canvas.after(100, sortMode(canvas, data))
        if data.speakMode == True:
            # back to intro page
            if event.y > data.homey1 and event.y < data.homey2 \
                    and event.x < data.homex2 and event.x > data.homex1:
                data.introMode = True
                data.speakMode = False
                data.sortMode = False
            # go to sort page
            if event.y > data.sorty1 and event.y < data.sorty2 \
                    and event.x < data.sortx2 and event.x > data.sortx1:
                data.introMode = False
                data.speakMode = False
                data.sortMode = True

    def timerFiredWrapper(canvas, data):
        if data.speakMode == True:
            timerFired(data)
            redrawAllWrapper(canvas, data)
            # pause, then call timerFired again
        canvas.after(data.timerDelay, timerFiredWrapper, canvas, data)
            # Set up data and call init

# below codes are cited from class notes

    class Struct(object): pass
    data = Struct()
    data.width = width
    data.height = height
    data.timerDelay = 100 # milliseconds
    global root
    root = Tk()
    init(data)
    # create the root and the canvas
    canvas = Canvas(root, width=data.width, height=data.height)
    canvas.configure(bd=0, highlightthickness=0)
    canvas.pack()
    redrawAllWrapper(canvas, data)
    # set up events
    root.bind("<Button-1>", lambda event:
                            mousePressedWrapper(event, canvas, data))
    # root.bind("<Key>", lambda event:
    #                         keyPressedWrapper(event, canvas, data))
    if data.sortMode == True:
        sortMode(canvas,data)

    timerFiredWrapper(canvas, data)
    # and launch the app
    root.mainloop() # blocks until window is closed
    print("bye!")



