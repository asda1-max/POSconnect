
def overflowManager(word,maximum_line_length,newSentence,wordGroup, configMax):
    while len(word) > configMax:
        newSentence.append(word[:configMax])
        word = word[configMax:]

    if len(word) > 0:
        wordGroup.append(word)
        maximum_line_length = configMax - len(word)
    
    return wordGroup, maximum_line_length, newSentence  


def groupingManager(word, maximum_line_length, wordGroup):
    if len(word) <= maximum_line_length:
        wordGroup.append(word)
        maximum_line_length -= len(word)
        return wordGroup, maximum_line_length  
    else:
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


    return str("\n".join(newSentence))
    
