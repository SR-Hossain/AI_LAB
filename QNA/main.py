
def translated_word(word):
    word = word.lower()
    return word

knowledge = open('knowledge.txt').read().split('. ')
mainCount = dict()
for (rowNumber, line) in enumerate(knowledge):
    for word in line.split(' '):
        if word not in mainCount:
            mainCount[translated_word(word)] = list()
        mainCount[translated_word(word)].append(rowNumber)
print(mainCount)
knowledge.append('As an AI model, I can\'t answer that...')



def maxElementOf(q):
    cnt = dict()
    maxIndex = -1
    maxRecursion = 0
    for x in q:
        cnt[x] = cnt.get(x, 0)+1
        if cnt[x] > maxRecursion:
            maxRecursion = cnt[x]
            maxIndex = x
    return maxIndex
while True:
    q = list() 
    for x in input().replace('?', '').split(' '):
        if x!='is':
            q += mainCount.get(x, [])
    print(knowledge[maxElementOf(q)])
    

