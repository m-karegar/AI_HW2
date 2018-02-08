import gensim
from sklearn.feature_extraction.text import CountVectorizer
from sklearn.feature_extraction.text import TfidfTransformer, TfidfVectorizer
from collections import defaultdict

import math
import time
import operator

class Line2Vector:
    def __init__(self, data):
        self.w2v = gensim.models.KeyedVectors.load_word2vec_format(
            '/Users/MohammadReza/Desktop/Uni/Programs/AI_HW2/FinalModel')
        # self.lines = open('/Users/MohammadReza/Desktop/Uni/Programs/AI_HW2/rem_stop_word.txt').readlines()[:2500]
        total = min(5000, len(data))
        self.lines = data[:total]

        self.unique_lines_count()

        self.ccc = 0

    def unique_lines_count(self):
        self.docFreq = dict()

        lineNumber = 0
        for line in self.lines:
            for word in line.split():
                if word in self.docFreq:
                    if self.docFreq[word][-1] != lineNumber:
                        self.docFreq[word].append(lineNumber)
                else:
                    self.docFreq[word] = [lineNumber]
            lineNumber += 1

        logn = math.log(len(self.lines))
        n = len(self.lines)
        for word in self.docFreq:
            # self.docFreq[word] = len(self.docFreq[word])
            # self.docFreq[word] = float(logn / (1 + len(self.docFreq[word])))
            self.docFreq[word] = float(math.log(n / (1 + len(self.docFreq[word]))))

        self.finalTfidf = dict()
        for line in self.lines:
            lineWithWords = line.split()
            lineLength = len(lineWithWords)
            for word in lineWithWords:
                self.finalTfidf[(line, word)] = (float(lineWithWords.count(word) / lineLength) * self.docFreq[word])
        """
        cnt = 0
        tmp = sorted(self.finalTfidf.items(), key=lambda x:x[1], reverse=False)
        for x in tmp:
            print(x)
            # print(l + ' ' + w + ' ' + str(self.finalTfidf[(l, w)]))
            cnt += 1
            if cnt > 15:
                break
        """

    def get_vector(self, line):
        cnt = 0
        res = [0 for i in range(100)]
        for word in line.split():
            try:
                tmp = self.w2v[word]
                # if (line, word) not in self.finalTfidf:
                #     self.ccc += 1

                # tmp = self.w2v[word] * self.finalTfidf[(line, word)]
                # tfidf = self.finalTfidf[(line, word)]
                for i in range(len(res)):
                    # res[i] += (tmp[i] * tfidf)
                    res[i] += tmp[i]
                # res += tmp
                cnt += 1
                # cnt += tfidf
            except KeyError:
                pass

        if cnt != 0:
            for i in range(len(res)):
                res[i] = float(res[i] / cnt)

        return res

