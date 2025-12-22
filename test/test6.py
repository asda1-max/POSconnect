
def overflowManager(word,maximum_line_length,newSentence,wordGroup, configMax):
    while len(word) > configMax:
        newSentence.append(word[:configMax])
        word = word[configMax:]
        print(word, len(word))

    if len(word) > 0:
        print("Asdasd",word)
        wordGroup.append(word)
        maximum_line_length = configMax - len(word)
    
    return wordGroup, maximum_line_length, newSentence  


def groupingManager(word, maximum_line_length, wordGroup):
    if len(word) <= maximum_line_length:
        wordGroup.append(word)
        maximum_line_length -= len(word)
        return wordGroup, maximum_line_length  
    else:
        print("checked")
        wordGroup.append(word[:maximum_line_length])
        return wordGroup, 0 

def clearWordGroup(newSentence, wordGroup, configMaxLineLength):
    newSentence.append(" ".join(wordGroup))
    wordGroup.clear()
    return newSentence, wordGroup, configMaxLineLength


def splitter(sentence):
    return sentence.split()

def autoSpacerEndLiner(sentence, maximum_line_length):

    configMaxLineLength = maximum_line_length

    words = splitter(str(sentence))

    wordGroup = []

    newSentence = []

    prevWordlength = 0

    for word in words:
        if len(word) > maximum_line_length:
            newSentence,wordGroup,maximum_line_length = clearWordGroup(newSentence, wordGroup,configMaxLineLength)

        print("processing word : ", word)
        if len(word) > maximum_line_length:
            remainingWord = word[maximum_line_length:]
            if maximum_line_length > 0:
                wordGroup, maximum_line_length = groupingManager(word[:maximum_line_length], maximum_line_length, wordGroup)
                newSentence.append(" ".join(wordGroup))
                wordGroup.clear()
            if len(remainingWord) > 0 :
                wordGroup, maximum_line_length,newSentence = overflowManager(remainingWord,maximum_line_length, newSentence,wordGroup,configMaxLineLength)
                if maximum_line_length <=0:
                    newSentence,wordGroup,maximum_line_length = clearWordGroup(newSentence, wordGroup,  configMaxLineLength)
                    
        else:
            wordGroup, maximum_line_length = groupingManager(word, maximum_line_length, wordGroup)
            if maximum_line_length <=0:
                newSentence,wordGroup,maximum_line_length = clearWordGroup(newSentence, wordGroup,configMaxLineLength)
                


    newSentence.append(" ".join(wordGroup))
    wordGroup.clear()


    print("\n".join(newSentence))
    
autoSpacerEndLiner("Aku percaya padamu meskipun ada kata superpanjangsekalitidakwajardanmelebihibatasbarisyangseharusnyabisaditangani dengan tenang tanpa merusak alur kalimat atau logika pemisahan baris.", 20)