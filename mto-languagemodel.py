from nltk import tokenize
from nltk.probability import FreqDist
from nltk.corpus import stopwords

file = open('headlinesPrepped.txt')

sentences = []

#sorry about this, been doing a lot of perl lately
englishStopWords = stopwords.words('English')

def good(token):
    global englishStopWords
    return token.isalnum() and token not in englishStopWords

print 'prepping...'
for line in file:
    tokenized = tokenize.sent_tokenize(line[:-1])
    for i in range(0,len(tokenized)):
        if len(tokenized[i]) == 1:
            sentences[-1] += tokenized[i]
        else:
            sentences.append(tokenized[i].lower())



allTokens = []

pw = tokenize.punkt.PunktWordTokenizer()

for sent in sentences:
    allTokens += pw.tokenize(sent)

print 'getting frequencies'
trigramFreqs = FreqDist("%s %s %s" % (allTokens[i], allTokens[i+1], allTokens[i+2]) for i in range(0,len(allTokens)-2) if (good(allTokens[i]) and good(allTokens[i+1])))
bigramFreqs = FreqDist("%s %s" % (allTokens[i], allTokens[i+1]) for i in range(0,len(allTokens)-1) if good(allTokens[i]) )
unigramFreqs = FreqDist(token for token in allTokens if good(token))

print "\tuni\tbi\ttri"

univals = unigramFreqs.items()
bivals = bigramFreqs.items()
trivals = trigramFreqs.items()

for i in range(0,100):
    print "%3d\t%s\t%s\t%s" % (i, univals[i][0], bivals[i][0], trivals[i][0])