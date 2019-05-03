import nltk
import numpy
# cited from python nltk module https://www.nltk.org

pool1 = [["i", "like", "apples"], ["chocolate", "tastes", "good"], ["elephants", "are", "huge"]]
pool2 = [["i", "ride", "a", "bike", "everyday"], ["he", "often", "party", "on", "weekend"]]



grammar1 = nltk.CFG.fromstring("""
S -> NP VP
VP -> V NP | V NP PP | V Adj
PP -> P NP
V -> "saw" | "ate" | "walked" |"like"| "tastes" | "are" 
NP -> "John" | "Mary" | "Bob" | "apples" | "chocolate" | "elephants" | "i" | Det N | Det N PP
Adj -> "good" | "huge"
Det -> "a" | "an" | "the" | "my"
N -> "man" | "dog" | "cat" | "telescope" | "park" | "chococlate"
P -> "in" | "on" | "by" | "with"
""")

def check(txt):
    sent = txt.split()
    rd_parser = nltk.RecursiveDescentParser(grammar1)
    print("111")
    try:
        print("222")
        for tree in rd_parser.parse(sent):
            print("333")
            print(tree)
            return True
    except:
        print("444")
        pass

print(check("i like apples"))
