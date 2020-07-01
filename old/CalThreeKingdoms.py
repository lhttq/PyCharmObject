#三国演义人名统计
import jieba
txt = open("F:\lht\Desktop\三国演义.txt","r",encoding ="utf-8").read()
words = jieba.lcut(txt)
counts = {}
for word in words:
    if len(word) == 1: #排除单个字符的分词效果
        continue
    else:
        counts[word] = counts.get(word,0) + 1
items = list(counts.items())
items.sort(key=lambda x:x[1],reverse=True)
for i in range(19):
    word ,count = items[i]
    print("{0:<10}{1:>5}".format(word,count))
