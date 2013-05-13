# -*- coding: cp1252 -*-
import random   ## Needed for random question generation
import scoring  ## Needed for, um, scoring.

try:            ## Loading config
    config = scoring.cVars('quizconfig.cfg')
except IOError: ## Creating config
    scoring.createConfig(
                            {
                                "QuestionAmount": 10,
                                "TriesAmount": 5,
                                "ScoreFile": 'scores.txt'
                            },
                            'quizconfig.cfg'
                         )
    config = scoring.cVars('quizconfig.cfg')

scorefile = str(config["ScoreFile"])    ##
numques = int(config["QuestionAmount"]) ## Config variables
numtries = int(config["TriesAmount"])   ##

  
win = 0     ## Dummy
first = 1   ##      variables
score = 0   ##               yeah

if numtries < 1: ## Mimimum number of tries
    numtries = 1

def menu(c1,c2,c3):
    """Menu function. Prints menu and returns choice."""
    print "\nActions:"
    print " 1 -", c1
    print " 2 -", c2
    print " 3 -", c3
    while True:
        choice = raw_input("Choose an action! ")
        if choice == "1":
            return 1
        elif choice == "2":
            return 2
        elif choice == "3":
            return 3
        else:
            print "That is not a valid action."

wmsg = [ ## Setting randomly chosen win messages
    "Correct!",
    "That was pretty cool, yo!",
    "Nicely done, that's right!",
    "Wouldn't you know? Correct!",
    "That is quite correct, old chap.",
    "Mm-hmm. That's one good right answer.",
    "YEAH! RRRRRIGHT!",
    ]

lmsg = [ ## Setting randomly chosen lose messages
    "Incorrect.",
    "Nope, incorrect.",
    "You're out of luck.",
    "No dice!",
    "Nah, that's not the answer.",
    "Wrong. Come on, you can do better next question!"
    ]

ques = [ ## List of questions. Every question is represented by a list where the
         ## first entry is the question, and the other ones are possible
         ## answers (all lower-case).
    ["Badger badger badger badger?", "mushroom", "mushroom mushroom", "mushroom, mushroom"],
    ["Who was the first Swede in space?" ,"christer fuglesang", "fuglesang"],
    ["What do penguins eat?", "fish"],
    ["What color is spinach?", "the same as grass", "green"],
    ["What does Mulle Meck mostly construct?", "boats", "cars"],
    ["Who finishes the lemonade?", "skolldir", "skölldir"],
    ["What is gravel?", "rock", "rocks", "stone", "stones"],
    ["Who lives deep in the jungle?", "a partner", "partner"],
    ["Who plays with the animals, yet sits in the cage?", "the cool trazan apansson", "balla trazan apansson"],
    ["What is sand?", "rock", "stone", "rocks", "stone"],
    ["Do you know what the best is?", "toys from br"],
    ["What are trolls known as nowadays?", "rock", "stone", "rocks", "stones"],
    ["Gandalf _______?", "the gray", "the white"],
    ["What is love?", "baby don't hurt me", "baby, don't hurt me"],
    ["What are rocks?", "rocks", "rock", "stone", "stones"],
    ["What is Gandalf usually called?", "gandalf"],
    ["Is Gandalf late?", "a wizard is never late, nor early", "a wizard is never late nor early", "a wizard is never late", "no"],
    ["Where does Goran Lerback probably live?", "in sweden", "sweden"],
    ["Write a tree that represents Sweden.", "a tree that represents sweden"],
    ["Why are giraffes' legs so long?", "to reach the ground"],
    ["What should not be thrown in glass houses?", "rock", "rocks", "stone", "stones"],
    ["Which root crop is the laziest?", "couch potato", "the couch potato"],
    ]

if numques > len(ques): ## Makes sure you con't get more questions than there are
    numques = len(ques)
orqs = ques[:]

def check(qa):      ## Code to check if the given answer is right or not
    question = qa[0]## List entry to be question
    answer = qa[1]  ## List entry to be answer
    useranswer = raw_input(question+'\n')       ## Variable to store the given answer
    if str.lower(lcs(useranswer)) in qa[1:]:    ## Checking match
        wmc = random.randint(0, len(wmsg) - 1)
        print wmsg[wmc]
        return True ## Correct returns true, and you can guess what the else does.
    else:
        return False

def ucs(st):
    """Turns Swedish letters to upper case."""
    s = st.replace("å", "Å")
    s = s.replace("ä", "Ä")
    s = s.replace("ö", "Ö")
    return s
    
def lcs(st):
    """Turns Swedish letters to lower case."""
    s = st.replace("Å", "å")
    s = s.replace("Ä", "ä")
    s = s.replace("Ö", "Ö")
    return s

def showq():
    """Shows a list of questions if the player has won at least once."""
    if win == 1: ## Win check!
        index = 0
        while index < len(ques):
            qa = ques[index]
            print "\nQuestion", str(ques. index(ques[index]) + 1)+":", qa[0]
            print "Answer:", str.upper(ucs(qa[1]))
            index = index + 1
    else:
        print "\nDon't cheat!"

def play(questions):
    """Main function."""
    global score    ## Plan ahead next time, Samuel.
    global consc    ##
    global conscmax ##
    if len(questions) == 0:
        print "No questions are present." ## If questions list is empty
        return
    index = 0
    right = 0
    while index < len(questions): ## Didn't know about enumerate() when I wrote this.
        tries = numtries
        trycount = 0
        lq = 0
        while trycount < tries: ## Gives you a specific amount of tries
            if check(questions[index]):
                right = right + 1
                consc += 1      ## Counts consecutive right answers
                if consc > conscmax:
                    conscmax = consc ## Your best streak will give points
                ## Worth mentioning:
                ## This is some of the worst scoring I've ever seen.
                ## Why did I do this?
                score += 1000 / (trycount + 1) + consc * 75
                index = index + 1
                trycount = tries
                lq = 1
            else:
                consc = 0 ## Resets consecutive right answers
                trycount = trycount + 1 ## The more tries you use, the less points you get
                score -= trycount * 10
                if trycount < tries: 
                    print tries - trycount, "tries left."
                else:
                    ## Subtracts from score (for some reason) and prints a random lose message
                    score -= trycount * 100
                    lmc = random.randint(0, len(lmsg) - 1)
                    print lmsg[lmc], "Correct was:", str.upper(ucs((questions)[index][1]))+"."
        if lq == 0: ## Should have used a boolean for this
            index = index + 1 ## Didn't know a whole lot of syntax
    if numtries == 1:
        nt = 1
    else:
        nt = numtries / 2
    score += (right * 150) / (nt)
    print "\nYou got", str(right * 100 / len(questions)) +\
          "% right out of", len(questions), "questions, for a total of %d points!" % score
    if conscmax > 1:
        print "A streak of %d - impressive!" % conscmax ## Tried out % formatting
    try:
        if score > scoring.highScore(scorefile):
            print "\n---  New high score!  ---"
    except IOError:
        xexex = open(scorefile, 'w') 
        xexex.close()
        if score > scoring.highScore(scorefile):
            print "\n---  New high score!  ---"
    scoring.saveScore(score, scorefile)
    print "\nCurrent high score is", str(scoring.highScore(scorefile)) + "."
choice = 0
while choice != 3: ## Main loop
    choice = menu("Play","Question and answer list","Quit")
    if choice == 1:
        consc = 0
        conscmax = 0
        score = 0
        ques = orqs[0:len(orqs)]
        random.shuffle(ques)
        del ques[numques:len(ques)]
        play(ques)
        win = 1
    elif choice == 2:
        showq()
