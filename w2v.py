import gensim

# model = gensim.models.Word2Vec.load('/Users/MohammadReza/Desktop/Uni/Programs/AI_HW2/FinalModel')#, encoding = 'utf-8')
# model = gensim.models.Word2Vec.load_word2vec_format('/Users/MohammadReza/Desktop/Uni/Programs/AI_HW2/FinalModel')
# model = gensim.models.KeyedVectors.load_word2vec_format('/Users/MohammadReza/Desktop/Uni/Programs/AI_HW2/FinalModel')

# print(model['مرد'])
# print(model['زن'])
# print(model['سوکابلیت'])
# print(model.similarity('دست', 'پا'))
# print(model.similarity('شتر', 'چین'))
# # print(model.doesnt_match('درخت', 'بشقاب', 'شاخه', 'برگ'))
# print(model.doesnt_match("دست پا موز گوش".split()))


class Line2Vector:
    def __init__(self):
        self.w2v = gensim.models.KeyedVectors.load_word2vec_format(
            '/Users/MohammadReza/Desktop/Uni/Programs/AI_HW2/FinalModel')

    def get_vector(self, line):
        cnt = 0
        res = [0 for i in range(100)]
        for word in line:
            try:
                tmp = self.w2v[word]
                res += tmp
            except KeyError:
                pass

        if cnt != 0:
            res /= cnt

        return res

