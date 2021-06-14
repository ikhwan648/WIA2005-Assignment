import re
from matplotlib import pyplot as plt

class problem2:
    def __init__(self,txtname):
        self._txtname=txtname
        self._average=0

    def solving_Problem2(self):
        alltotal=0
        array = []
        arrayNegative = []
        kira = 0
        frequency = {}
        # i masukkan article tu dalam file, so ni utk baca and print
        f = open(self._txtname, encoding ="utf8")
        article = f.read()
        f.close()

        #print(article)
        # ni method utk cari all the word frequency dalam file tu
        #document_text = open('articlePosLaju1.txt', 'r')
        text_string = article.lower()
        match_pattern = re.findall(r'\b[a-z]{3,99}\b', text_string)

        for word in match_pattern:
            count = frequency.get(word, 0)
            frequency[word] = count + 1

        frequency_list = frequency.keys()

        #print('')
        # print('Word frequency in the article: ')
        # print('')
        # o = 0
        # for words in frequency_list:
        #     if o == 5:
        #         print(" ")
        #         o = 0
        #     print(words, "=", frequency[words], end=', ')
        #     o = o + 1

        #print('')
        # print('              Stop words frequency: ')
        # print('')


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

            # if counter == 0:
            #     print("\"", word, "\"", 'has no match in the article', end=', ')
            # else:
            #     if counter > 1:
            #         print("\"", word, "\"", 'pop up in the article: ', counter, 'times', end=', ')
            #     if counter == 1:
            #         print("\"", word, "\"", 'pop up in the article: ', counter, 'time', end=', ')


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
                #print("")
                e = 0
            search(stop_words, whole_word)
            e = e + 1
        # ni utk delete stopwords
        resultwords = [word for word in re.split("\W+", whole_word) if word.lower() not in stop_words]
        #print('')
        # print('The article without stopwords: ')
        # print('')
        result = ' '.join(resultwords)

        #print(result)
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
        else:
            print('The courier has negative sentiment')

        alltotal=totalNegative+totalPositive

        self._average=totalPositive/alltotal

        plt.hist(arrayNegative)
        plt.show()

        plt.hist(frequency)
        plt.show()

        print("The ration for this article is   =", self._average)

    def get_ration(self):
        return self._average