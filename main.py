# Problem 2: Even the shortest path able to be determine, passengers are still facing
# daily problem due to the long waiting time. The unusual and unexpected condition during
# the journey such as unexpected traffic congestion, unexpected delay, randomness in passengers’
# demands and weather changes need to be considered before making suggestion.
import re
from matplotlib import pyplot as plt
# import numpy as np
# import plotly
# import plotly.graph_objects as go
# import plotly.offline as pyo
# import plotly.express as px
alltotal=0
array = []
arrayNegative = []
kira = 0
frequency = {}
link= ['gdex1.txt','gdex2.txt','gdex3.txt','articlePosLaju1.txt','articlePosLaju2.txt','articlePosLaju3.txt','citylink1.txt','citylink2.txt','citylink3.txt','articleJ&T1.txt','articleJ&T2.txt','articleJ&T3.txt','articleDHL1.txt','articleDHL2.txt','articleDHL3.txt']
allaverage=[]
allsentiment=[]
distancevalue=[0.8,0.4,0.6,0.6,0.8,0.8,0.4,0.6,0.2,0.2,0.2,1,1,1,0.4]
#0.56969697,0.284848485,0.427272727,0.349444444,0.465925926,0.465925926,0.184993836,0.277490754,0.121034137
gdexprob=[]
posprob=[]
cityprob=[]
jtprob=[]
dhlprob=[]
finalcounter=0
#'gdex1.txt','gdex2.txt','gdex3.txt','articlePosLaju1.txt','articlePosLaju2.txt','articlePosLaju3.txt','citylink1.txt','citylink2.txt','citylink3.txt','articleJ&T1.txt','articleJ&T2.txt','articleJ&T3.txt','articleDHL1.txt','articleDHL2.txt','articleDHL3.txt'

#'articleDHL1','articleDHL2','articleDHL3
for i in range(len(link)):
    f = open(link[i], encoding ="utf8")
    article = f.read()
    f.close()

    print(article)
    # ni method utk cari all the word frequency dalam file tu
    #document_text = open('articlePosLaju1.txt', 'r')
    text_string = article.lower()
    match_pattern = re.findall(r'\b[a-z]{3,99}\b', text_string)

    for word in match_pattern:
        count = frequency.get(word, 0)
        frequency[word] = count + 1

    frequency_list = frequency.keys()

    print('')
    print('Word frequency in the article: ')
    print('')
    o = 0
    for words in frequency_list:
        if o == 5:
            print(" ")
            o = 0
        print(words, "=", frequency[words], end=', ')
        o = o + 1

    print('')
    print('              Stop words frequency: ')
    print('')


    def search(word, text):  # using rabin-karp algorithm method untuk cari stop words and frequency dia
        m = len(word)
        n = len(text)

        counter = 0

        for i in range(0, n - m + 1):
            found = True
            for j in range(0, m):
                if word[j] != text[i + j]:
                    found = False
                    break
            if found:
                counter += 1

        if counter == 0:
            print("\"", word, "\"", 'has no match in the article', end=', ')
        else:
            if counter > 1:
                print("\"", word, "\"", 'pop up in the article: ', counter, 'times', end=', ')
            if counter == 1:
                print("\"", word, "\"", 'pop up in the article: ', counter, 'time', end=', ')


    whole_word = article
    pat = 'i me my myself we our ours ourselves you your yours yourself yourselves he him his himself she her hers herself ' \
          'it its itself they them their theirs themselves what which who whom this that these those am is are was were be ' \
          'been being have has had having do does did doing a an the and but if or because as until while of at by for ' \
          'with about against between into through during before after above below to from up down in out on off over ' \
          'under again further then once here there when where why how all any both each few more most other some such no ' \
          'nor not only own same so than too very s t can will just don should now "" "'
    # pat ni list of stopwords
    e = 0
    for stop_words in pat.split():
        if e == 3:
            print("")
            e = 0
        search(stop_words, whole_word)
        e = e + 1
    # ni utk delete stopwords
    resultwords = [word for word in re.split("\W+", whole_word) if word.lower() not in stop_words]
    print('')
    print('The article without stopwords: ')
    print('')
    result = ' '.join(resultwords)

    print(result)
    # positive words file
    f = open('positive_words.txt')
    positive = f.read()
    f.close()
    # negative words file
    f = open('negative_words.txt')
    negative = f.read()
    f.close()

    # KMP string matching algorithm

    counter = 0


    def KMPSearch(pat, txt):
        M = len(pat)
        N = len(txt)

        # create lps[] that will hold the longest prefix suffix
        # values for pattern
        lps = [0] * M
        j = 0  # index for pat[]

        # Preprocess the pattern (calculate lps[] array)
        computeLPSArray(pat, M, lps)

        i = 0  # index for txt[]
        if M == N:
                while i < N:
                    if pat[j] == txt[i]:
                        i += 1
                        j += 1

                    if j == M:
                        # print("Found pattern at index " + str(i - j)+pat)
                        print("Found word =", pat)  ## masukkan counter dkt sini
                        j = lps[j - 1]

                        array.append(pat)

                        # mismatch after j matches
                    elif i < N and pat[j] != txt[i]:
                        # Do not match lps[0..lps[j-1]] characters,
                        # they will match anyway
                        if j != 0:
                            j = lps[j - 1]
                        else:
                            i += 1


    def KMPSearchNegative(pat, txt):
        M = len(pat)
        N = len(txt)

        # create lps[] that will hold the longest prefix suffix
        # values for pattern
        lps = [0] * M
        j = 0  # index for pat[]

        # Preprocess the pattern (calculate lps[] array)

        computeLPSArray(pat, M, lps)

        i = 0  # index for txt[]
        if M == N:
                while i < N:
                    if pat[j] == txt[i]:
                        i += 1
                        j += 1

                    if j == M:
                            print("Found word =", pat)  ## masukkan counter dkt sini
                            j = lps[j - 1]
                            arrayNegative.append(pat)

                        # mismatch after j matches
                    elif i < N and pat[j] != txt[i]:
                        # Do not match lps[0..lps[j-1]] characters,
                        # they will match anyway
                        if j != 0:
                            j = lps[j - 1]
                        else:
                            i += 1


    def computeLPSArray(pat, M, lps):
        len = 0  # length of the previous longest prefix suffix

        lps[0]  # lps[0] is always 0
        i = 1

        # the loop calculates lps[i] for i = 1 to M-1
        while i < M:
            if pat[i] == pat[len]:
                len += 1
                lps[i] = len
                i += 1
            else:
                # This is tricky. Consider the example.
                # AAACAAAA and i = 7. The idea is similar
                # to search step.
                if len != 0:
                    len = lps[len - 1]

                    # Also, note that we do not increment i here
                else:
                    lps[i] = 0
                    i += 1


    print('')
    print('Number of positive words in this article: ')
    print('')
    i = 0
    j = 0

    for pos_word in positive.split():
        for j in whole_word.split():
            KMPSearch(pos_word, j)


    totalPositive = len(array)

    print('Total number of positive word in the article is = ', totalPositive)
    plt.hist(array)
    plt.show()

    i = 0
    j = 0

    ##################negativecounter=0


    print('')
    print('Number of negative words in this article: ')
    print('')
    for neg_word in negative.split():
        for j in whole_word.split():
            KMPSearchNegative(neg_word, j)


    totalNegative = len(arrayNegative)

    print('Total number of negative word in the article is = ', totalNegative)

    print('')
    print('Sentiment of the courier: ')

    if (totalPositive > totalNegative):
        print('The courier has positive sentiment')
        allsentiment.append('Positive')
    elif (totalPositive == totalNegative):
        print('The courier has Neutral sentiment')
        allsentiment.append('Neutral')
    else:
        print('The courier has negative sentiment')
        allsentiment.append('Negative')

    alltotal=totalNegative+totalPositive

    average=totalPositive/alltotal

    plt.hist(arrayNegative)
    plt.show()

    plt.hist(frequency)
    plt.show()
    allaverage.append(average)

    print("The ratio for this article is   =", average)

print(allaverage)

a=0
finalcounter=0
sentimentgdex=allaverage[0]*allaverage[1]+allaverage[2]/3
while(finalcounter<=2):
    temp=sentimentgdex*distancevalue[a]
    gdexprob.append(temp)
    a=a+1
    finalcounter=finalcounter+1

finalcounter=3
a = 3
sentimentpos=allaverage[3]*allaverage[4]+allaverage[5]/3
while(finalcounter<=5):
    temp=sentimentpos*distancevalue[a]
    posprob.append(temp)
    a=a+1
    finalcounter=finalcounter+1

finalcounter=6
a = 6
sentimentcity=allaverage[6]*allaverage[7]+allaverage[8]/3
while(finalcounter<=8):
    temp=sentimentcity*distancevalue[a]
    cityprob.append(temp)
    a=a+1
    finalcounter=finalcounter+1

finalcounter=9
a = 9
sentimentJT=allaverage[9]*allaverage[10]+allaverage[11]/3

while(finalcounter<=11):
    temp = sentimentJT * distancevalue[a]
    jtprob.append(temp)
    a=a+1
    finalcounter=finalcounter+1

finalcounter=12
a = 12
sentimentDHL=allaverage[12]*allaverage[13]+allaverage[14]/3
while(finalcounter<=14):
    temp = sentimentDHL * distancevalue[a]
    dhlprob.append(temp)
    a=a+1
    finalcounter=finalcounter+1

print("\n\nTotal Probabability for every route")
print("\nCustomer 1")
print('GDex      =', gdexprob[0])
print('PosLaju      =', posprob[0])
print('CityLink     =', cityprob[0])
print('J&T       =', jtprob[0])
print('DHL          =', dhlprob[0])


print("\nCustomer 2")
print('GDex         =', gdexprob[1])
print('PosLaju      =', posprob[1])
print('CityLink     =', cityprob[1])
print('J&T      =', jtprob[1])
print('DHL       =', dhlprob[1])


print("\nCustomer 3")
print('GDex      =', gdexprob[2])
print('PosLaju      =', posprob[2])
print('CityLink     =', cityprob[2])
print('J&T       =', jtprob[2])
print('DHL       =', dhlprob[2])