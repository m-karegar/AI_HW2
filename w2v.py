import gensim
import math
import time
import operator


class Line2Vector:
    def __init__(self):
        self.w2v = gensim.models.KeyedVectors.load_word2vec_format(
            '/Users/MohammadReza/Desktop/Uni/Programs/AI_HW2/FinalModel')
        """self.appearance_in_lines = {}
        tmp = time.time()
        self.lines = open('/Users/MohammadReza/Desktop/Uni/Programs/AI_HW2/rem_stop_word.txt').readlines(100000)
        print(len(self.lines))
        self.unique_lines_count()
        print(time.time() - tmp)

    def unique_lines_count(self):
        for line in self.lines:
            for word in line.split():
                if word not in self.appearance_in_lines:
                    self.appearance_in_lines[word] = 0
                    for l in self.lines:
                        if word in l.split():
                            self.appearance_in_lines[word] += 1

        tmp = sorted(self.appearance_in_lines.items(), key=lambda x:x[1], reverse=True)
        cnt = 0
        for w in tmp:
            print(w)
            cnt += 1
            if cnt > 20:
                break

    def idf(self, word):
        return float(math.log(len(self.lines)) / (1 + self.appearance_in_lines[word]))

    def tf(self, word, line):
        return float(line.split.count(word) / len(line.split))

    def tfidf(self, word, line):
        return self.tf(word, line) * self.idf(word)
    """
    def get_vector(self, line):
        cnt = 0
        res = [0 for i in range(100)]
        for word in line:
            try:
                tmp = self.w2v[word]
                res += tmp
                cnt += 1
            except KeyError:
                pass

        if cnt != 0:
            for i in range(len(res)):
                res[i] = float(res[i] / cnt)

        return res

