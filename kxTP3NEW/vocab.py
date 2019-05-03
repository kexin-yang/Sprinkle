import nltk
import random

def addS(lst):
    lst = list(lst)
    for i in range(len(lst)):
        lst[i] = lst[i] + "s"
    # print(lst)
    return lst

sentenceType = ["SVO"]
singPronoun = ["i","she","he","it"]
pluPronoun = ["they","we","you"]
beVerbPreS = ["is","am"]
beVerbPreP = ["are"]
animals = ['alligator', 'ant', 'bear', 'bee', 'bird', 'camel', 'cat', 'cheetah', 'chicken', 'chimpanzee', 'cow',\
           'crocodile', 'deer', 'dog', 'dolphin', 'duck', 'eagle', 'elephant', 'fish', 'fly', 'fox', 'frog', 'giraffe',\
           'goat', 'goldfish', 'hamster', 'hippopotamus', 'horse', 'kangaroo', 'kitten', 'leopard', 'lion', 'lizard', \
           'lobster', 'monkey', 'octopus', 'ostrich', 'otter', 'owl', 'oyster', 'panda', 'parrot', 'pelican', 'pig',\
           'pigeon', 'porcupine', 'puppy', 'rabbit', 'rat', 'reindeer', 'rhinoceros', 'rooster', 'scorpion', 'seal',\
           'shark', 'sheep', 'shrimp', 'snail', 'snake', 'sparrow', 'spider', 'squid', 'squirrel', 'swan',\
           'tiger', 'toad', 'tortoise', 'turtle', 'vulture', 'walrus', 'weasel', 'whale', 'wolf', 'zebra']
fruits = ['almonds', 'apple', 'apricot', 'avocado', 'banana', 'blackberry', 'cherry', 'chestnuts', 'coconuts',\
          'date', 'fig', 'grapefruit', 'grapes', 'hazelnuts', 'lemon', 'lime', 'mango', 'walnuts', 'melon', 'mulberry',\
          'orange', 'peach', 'peanuts', 'pear', 'pineapple', 'plum', 'pomegranate', 'watermelon', 'raspberry', \
          'watermelon', 'strawberry', 'tangerine', 'walnuts', 'watermelon']
ballGame = ['baseball', 'basketball', "soccer", 'football', 'golf', 'handball', \
            'rugby', 'soccer', 'squash', 'tennis', 'volleyball']
drink = ['beer' 'Coke', 'champagne', 'cider', 'coffee', 'gin', \
         'juice', 'lemonade', 'liqueur', 'milkshake', \
         'red wine', 'rum', 'soda', 'tea', 'vodka',\
         'water', 'whisky', 'wine']
food = ['bacon', 'beef', 'beef steak', 'sausage', 'cheese', 'cheeseburger', \
        'chicken', 'dessert', 'gnocchi', 'ham', 'hamburger', 'lamb', 'lasagne', 'liver', 'macaroni', \
        'mashed potatoes', 'mayonnaise', 'meatballs', 'noodles',\
        'omelet', 'pasta', 'pizza', 'pork', 'ravioli', 'ribs', 'roastbeef', 'salad', \
        'salami', 'eggs', 'soup', 'spaghetti', 'steak', 'stew', 'turkey', 'veal', 'vegetables']
emotionVerbPl = ["love", "like", "dislike", "hate", "adore", "prefer", "want", "need", "desire"]
emotionVerbSg = addS(emotionVerbPl)
pp1 = ["onthedesk", "intheroom", "alongtheriver", "alongthehighway","underthetree","underthebridge",\
      "bythelake","withsomefriends", "withasmile","inthesky", "intheforest", "ontheground", "onthesea", \
      "ontheboat", "atthemoment", "atthecorner", "aroundthecorner" ]
pp2 = ["on      the     desk", "in      the     room", "along       the     river", "along      the     highway",\
       "under       the     tree","under        the     bridge",\
      "by       the     lake","with     some        friends", "with     a       smile","in      the     sky", \
       "in      the     forest", "on        the     ground", "on        the     sea", \
      "on       the     boat", "at      the     moment", "at        the     corner", "around        the     corner" ]
adjective = ["adorable", "adventurous", "agreeable", "alive", "amused", "angry", "annoying", "attractive", "awful", \
             "bad","beautiful", "bored", "busy","calm", "cheerful", "charming", "clever", "clumsy", "colorful", "crazy",\
             "cute", "dangerous", "delightful", "elegant", "fancy","famous", "friendly","frantic", "funny"\
             "gentle", "good", "gorgeous", "graceful", "handsome", "happy", "helpful", "hilarious", "hungry", "innocent"\
             "joyous", "kind", "lazy", "lovely", "naughty", "nice", "poor", "rich", "scary", "selfish", "shy", \
             "silly", "strange", "stupid", "tired", "witty"]
det = ["a","an","the","my"]
p = ["in", "on", "by", "with"]

# on a higher level
singSub = [singPronoun,animals]
pluSub = [pluPronoun]
eatable = [fruits,drink,food]
verbS = [emotionVerbSg]
verbPl = [emotionVerbPl]

#highest level, simplist SVO
sub = [singSub,pluSub]
verb = [verbS,verbPl]
obj = [animals, fruits, ballGame,drink,food]

def parsePhrase(str):
    # this function parse the propositional phrases into a list of single words, for the purpose of \
    # generating words in a phrase
    phraseWords = str.split()
    return phraseWords

def extendGrammarString(lst):
    # this function turn words in the word pool into CFG grammar string
    result = ""
    for i in range(len(lst)-1):
        result += "\'"
        result += lst[i]
        result += "\'"
        result += " | "
    result += "\'"
    result += lst[-1]
    result += "\'"
    return result

def generateMyGrammar():
    # this function generate my grammar, with some reference to https://www.nltk.org/book/ch08.html
    result = ""
    result += "S -> NP VP\nVP -> V NP | V NP PP | V Adj\nPP -> P NP\nV -> "
    # adding the verbs in the grammar
    result += extendGrammarString(emotionVerbPl)
    result += " | "
    result += extendGrammarString(emotionVerbSg)
    #adding Noun Phrases (NP)
    result += "\nNP -> N | Det N | Det N PP | "
    result += extendGrammarString(singPronoun)
    result += " | "
    result += extendGrammarString(pluPronoun)
    result += "\n"
    # adding adj
    result += "Adj -> "
    result += extendGrammarString(adjective)
    # adding Det
    result += "\nDet -> "
    result += extendGrammarString(det)
    # adding noun (N)
    result +="\nN -> "
    result += extendGrammarString(ballGame)
    result += " | "
    result += extendGrammarString(food)
    result += " | "
    result += extendGrammarString(drink)
    result += " | "
    result += extendGrammarString(animals)
    result += " | "
    result += extendGrammarString(fruits)
    # adding P
    result += "\nP -> "
    result += extendGrammarString(p)
    # adding propostional phrases (PP)
    result += "\nPP -> "
    result += extendGrammarString(pp1)
    return result

generateMyGrammar()



def checkGrammar(txt):
    # this grammar checking function is adapted from https://www.nltk.org/book/ch08.html
    grammarStr = generateMyGrammar()
    grammar2 = nltk.CFG.fromstring(grammarStr)
    # below cited from python nltk module https://www.nltk.org/book/ch08.html
    sent = txt.split()
    rd_parser = nltk.RecursiveDescentParser(grammar2)
    try:
        for tree in rd_parser.parse(sent):
            print(tree)
            return True
    except:
        pass

def getAll(lst):
    if isinstance(lst[0],str):
        return lst
    else:
        all = []
        for entry in lst:
            all.extend(getAll(entry))
        return all

def get(str):
    b = str.split("\n")

def sentenceLevel1():
    pool = []
    localSubject = sampleWord(sub)
    pool.append(localSubject)
    if localSubject in getAll(singSub) and localSubject is not "i":
        localVerb = sampleWord(verbS)
    else:
        localVerb = sampleWord(verbPl)
    pool.append(localVerb)
    localObj = sampleWord(obj)
    pool.append(localObj)
    # sentence = localSubject+ " " + localVerb+ " " + localObj
    random.shuffle(pool)
    return pool


def sentenceLevel2():
    pool = []
    localSubject = sampleWord(sub)
    pool.append(localSubject)
    if localSubject in getAll(singSub):
        localVerb = sampleWord(verbS)
    else:
        localVerb = sampleWord(verbPl)
    pool.append(localVerb)
    localObj = sampleWord(obj)
    pool.append(localObj)
    localPP = sampleWord(pp1)
    pool.append(localPP)
    random.shuffle(pool)
    return pool



def generateSentence(level):
    if level == 1:
        # most basic SVO
        pool = sentenceLevel1()
        return pool
    if level == 2:
        # SVO + PP(prepositional phrase)
        pool = sentenceLevel2()
        return pool

def sampleWord(lst):
    while True:
        lst = random.choice(lst)
        if isinstance(lst,str): break
    return lst

