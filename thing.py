from functools import reduce

f = open('pg583.txt', 'rU')
s = f.read()
s = s.replace(",", "").replace(".", "").replace("?", "").replace("!", "").replace(":", "").replace(";", "")

split = s.split(' ')

def singleFreq(book, word):
    return book.count(" " + word + " ")

def totalFreq(book, words):
    return reduce(lambda i, x: i + x, [singleFreq(book, word) for word in words])

def mostFreq(book):
    return reduce((lambda x, y: x if singleFreq(book, x) > singleFreq(book, y) else y), book.split(" "))
