import random

# Graphic function
from tkinter import *
def generateWords():
    # this function provide a pool of words that can make senteces, and randomly choose from them
    wordPool = (["he","really","likes","apples"],["i","can","play","football"],["they","usually","eat","dinner","together"])
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
    data.speakingInstruction = "Say a word in the bubble!"
    data.nextx1, data.nexty1, data.nextx2, data.nexty2 \
        = data.width * 0.05,data.height * 0.85, data.width * 0.15, data.height * 0.95
    # sorting mode attribute
