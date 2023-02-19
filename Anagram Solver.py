words3 = []
words4 = []
words5 = []
words6 = []
words7 = []

wordCookies = input("What letters have you been given... ")

def anagramCheck(word, checkWord):
    for letter in word:
        if letter in checkWord:
            checkWord = checkWord.replace(letter, '', 1)
        else:
            return 0
    return 1

f = open('English Words.txt', 'r')

for line in f:
    line = line.strip()
    if anagramCheck(line, wordCookies):
        line = line.upper()# changes word to uppercase
        if len(line) == 3:
            words3.append(line)
        if len(line) == 4:
            words4.append(line)
        if len(line) == 5:
            words5.append(line)
        if len(line) == 6:
            words6.append(line)
        if len(line) == 7:
            words7.append(line)

words3.sort()
words4.sort()
words5.sort()
words6.sort()
words7.sort()

for i in range(len(words3)):
    print (words3[i])
            
for i in range(len(words4)):
    print (words4[i])

for i in range(len(words5)):
    print (words5[i])

for i in range(len(words6)):
    print (words6[i])

for i in range(len(words7)):
    print (words7[i])









