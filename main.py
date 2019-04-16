import hearWords
import BubbleClass
BubbleClass.runBubbles()

# helper functions

def distance(x1,y1,x2,y2):
    # define the distance between two points (x1,y1), (x2,y2)
    return ((abs(x1-x2))**2 +(abs(y1-y2))**2)**0.5
# need to solve:
    # have speech recognition to be constantly listening
    #  auto generate words in the words list
    # get to the next scene, give a set of new words

#Some Features I want implemented later:
    # want bubble to bounce off each other
    # want the r to be in according to the length of the words
    # do we want it to move up and down, or straight down, think about whether we want to give them limited time to speak out the words.
    # once we speak it, it shrink a little, until it is small enough, to practice speaking it for several times. (for hard words)
    # the effect of words drifting to a bucket or where it feel collected.
    # When done with the last word, should tell them they can start next step.
    # make UI more pretty by changing bg color, bubble color, adding pictures.
    # get ready to speak, 3,2,1?
    # Speak a sentence?
    # learner can choose whether they want to sort or continue speaking.







