from functools import reduce

f = open('p583.txt', 'rU')
s = f.read()
s = s.replace(",", "").replace(".", "").replace("?", "").replace("!", "").replace(":", "").replace(";", "")

split = s.split(' ')

def singleFreq(book, word):
    return book.count(" " + word + " ")

def totalFreq(book, words):
    return reduce(lambda i, x: i + x, [singleFreq(book, word) for word in words])

def mostFreq(book):
    li = list(set(book.split(' ')))
    return reduce(lambda a, b: a if (a > b) else b, li)
