# -*- coding: cp1252 -*-
def saveScore(score, filename):
    """Appends 'score' variable with current time to file 'filename'."""
    import time
    import sys
    scorefile = open(filename, "a")
    wr = str(score) + " points - " + time.asctime(time.localtime(time.time())) + "\n"
    scorefile.write(wr)
    scorefile.close()

def showScores(filename):
    """Prints the scores file 'filename' as-is."""
    scorefile = open(filename, "r")
    print scorefile.read()
    scorefile.close()

def highScore(filename):
    """Checks scores file 'filename' generated by saveScore() and returns highest score to date."""
    scorelist = []
    hs = None
    scorefile = open(filename, "r")
    for line in scorefile:
        scorelist.append(line.strip())
    for sco in scorelist:
        if int(sco[:sco.index(' ')]) > hs:
            hs = int(sco[:sco.index(' ')])
    scorefile.close()
    return hs

def cVars(confile):
    """Returns a dictionary with the keys and values specified in a separate config file."""
    configs = open(confile, 'r')
    cf = {}
    for line in configs:
        key, value = line.split("=")
        cf[key.strip()] = value.strip()
    configs.close()
    return cf

def createConfig(defdict, filename):
    """Creates a config file 'filename' based on dictionary 'defdict'."""
    confile = open(filename, 'w') ##vpmgo�e
    for key in defdict.keys():
        confile.write(str(key) + "\t\t=\t" + str(defdict[key]) + "\n")
    confile.close()
    lineSort(filename)

def lineSort(filename):
    """Sorts the lines in file 'filename' alphabetically."""
    sortfile = open(filename, 'r')
    lines = sortfile.read().split('\n')
    nonempty = [line.rstrip() for line in lines if line.strip()]
    nonempty.sort()
    sortfile.close()
    sortfile = open(filename, 'w')
    sortfile.write('\n'.join(nonempty) + '\n')
    sortfile.close()