def getLastIdxOfCharacter(pattern):
    lastIdx = [0 for i in range(128)]
    for i in range (0,128):
        lastIdx[i]=0
    for i in range (0,len(pattern)):
        lastIdx[ord(pattern[i])] = i
    return lastIdx

def boyermoore(text,pattern):
    lastIdx = getLastIdxOfCharacter(pattern)
    textlen = len(text)
    patternlen = len(pattern)

    positionInText = patternlen - 1
    if (positionInText > textlen-1):
        return -1
    else:
        positionInPattern = positionInText
        while (positionInText <= textlen-1):
            if (ord(pattern[positionInPattern]) == ord(text[positionInText])):
                if (positionInPattern==0):
                    return positionInText
                else:
                    positionInText -= 1
                    positionInPattern -= 1
            else:
                lo = lastIdx[ord(text[positionInText])]
                if (positionInPattern < lo+1):
                    positionInText += patternlen - positionInPattern
                else:
                    positionInText += patternlen - (lo+1)
                positionInPattern = patternlen-1
    return -1

        