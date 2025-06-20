def count_words(book):
    lines = book.split()
    return len(lines)

def count_letters(book):
    wordCounter = {}
    letterSet = set()
    for letter in book:
        if letter.isalpha():
            letter = letter.lower()
            if letter in letterSet:
                wordCounter[letter] += 1
            else:
                wordCounter[letter] = 1
                letterSet.add(letter)
    return dictToList(wordCounter)
    
def dictToList(dic):
    dicList = [{'char': key, 'num': value} for key, value in dic.items()]
    dicList.sort(reverse=True, key=sort_on)
    return dicList

def sort_on(items):
    return items['num']

def printMessage(lines, list):
    
    print("==========Book Bot==========")
    print("analyzing book....")
    print("---Word Count---")
    print(f"found {lines} total words")
    print("---Character Count---")
    for char in list:
        print(f"the letter {char['char']} was found {char['num']} times")
    print("---End of report---")
