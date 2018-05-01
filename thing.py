from functools import reduce

f = open('pg583.txt', 'rU')
s = f.read()
s = s.replace(",", "").replace(".", "").replace("?", "").replace("!", "").replace(":", "").replace(";", "")

split = s.split(' ')

def singleFreq(book, word):
    #return book.count(" " + word + " ")
    book = book.split()
    return len([w for w in book if w == word])
    
def totalFreq(book, words):
    return reduce(lambda i, x: i + x, [singleFreq(book, word) for word in words])

def mostFreq(book):
    return reduce((lambda x, y: x if singleFreq(book, x) > singleFreq(book, y) else y), book.split(" "))

print("singleFreq(s, 'Marian') " + str(singleFreq(s, "Marian")))
print("totalFreq(s, ['Marian', 'Laura']) " + str(totalFreq(s, ["Marian", "Laura"])))
#print("singleFreq(s, 'Marian') " + str(singleFreq(s, "Marian")))
