def add_dots(word):
    newWord = ""
    length = len(word)
    count = 1
    for letter in word:
        if length == count:
            newWord += letter
        else:
            newWord += letter + "."
        count+=1
    return newWord
    
def remove_dots(word):
    newWord = ""
    for letter in word:
        if letter != ".":
            newWord += letter
    return newWord