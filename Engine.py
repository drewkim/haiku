__author__ = 'Drew'

import random

dict = open('dict', 'r')
pronDict = {}
sylDict = {}

def numSyl(pron):
    count = 0
    for a in pron:
        if a.isdigit():
            count += 1
    return count

for line in dict:
    pronDict[line[:line.find(' ')]] = line[line.find(' ')+2:line.find('\n')]
    num = numSyl(pronDict[line[:line.find(' ')]])
    if num in sylDict:
        sylDict[num] += [line[:line.find(' ')]]
    else:
        sylDict[num] = [line[:line.find(' ')]]

successors = {}
prev = 'hello'
themeGen = open('themeGen', 'r+')
for line in themeGen:
    wordlist = line.split()
    for word in wordlist:
        if prev in successors:
            if word in successors[prev]:
                successors[prev][word] += 1
            else:
                successors[prev][word] = 1
        else:
            successors[prev] = {word:1}
        prev = word

def makeHaiku(theme):
    line1 = theme + ' '
    line2 = ''
    line3 = ''
    syl1 = numSyl(pronDict[theme.upper()])
    syl2 = 0
    syl3 = 0
    word = theme
    while syl1 < 5:
        freq = []
        for w in list(successors[word].keys()):
            for i in range(0, successors[word][w]):
                freq += [w]
        newWord = random.choice(freq)
        while (newWord.upper() not in pronDict) or (numSyl(pronDict[newWord.upper()]) > 5-syl1):
            newWord = random.choice(freq)
        line1 += newWord + ' '
        syl1 += numSyl(pronDict[newWord.upper()])
        word = newWord
    while syl2 < 7:
        freq = []
        for w in list(successors[word].keys()):
            for i in range(0, successors[word][w]):
                freq += [w]
        newWord = random.choice(freq)
        while (newWord.upper() not in pronDict) or (numSyl(pronDict[newWord.upper()]) > 7-syl2):
            newWord = random.choice(freq)
        line2 += newWord + ' '
        syl2 += numSyl(pronDict[newWord.upper()])
        word = newWord
    while syl3 < 5:
        freq = []
        for w in list(successors[word].keys()):
            for i in range(0, successors[word][w]):
                freq += [w]
        newWord = random.choice(freq)
        while (newWord.upper() not in pronDict) or (numSyl(pronDict[newWord.upper()]) > 5-syl3):
            newWord = random.choice(freq)
        line3 += newWord + ' '
        syl3 += numSyl(pronDict[newWord.upper()])
        word = newWord
    return line1 + '\n' + line2 + '\n' + line3

theme = input('Enter theme:')
while (theme.upper() not in pronDict) or (numSyl(pronDict[theme.upper()]) > 5):
    theme = input('Enter theme:')

print(makeHaiku(theme))

