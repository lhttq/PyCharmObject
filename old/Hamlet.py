#CalhamletV1.py
def getText():
    txt = open("H:\文档\Hamle.txt").read()
    txt = txt.lower()
    for ch in '|"#$%^&()_+{}[]\\*,;><@!`:':
        txt = txt.replace(ch," ")
    return txt


hamletText = getText()
words = hamletTxt.split()
counts = {}
for word in words:
    counts[word] = counts.get(word,0) + 1
    items = list(counts.items())
    #items.sort(key=lambda X:X[1], reverse+True)
    for i in range(10):
        word,count = items[i]
        print("{0:<10}{1:>5}".format(word,count))
