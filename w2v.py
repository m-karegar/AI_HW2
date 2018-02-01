import gensim

# model = gensim.models.Word2Vec.load('/Users/MohammadReza/Desktop/Uni/Programs/AI_HW2/FinalModel')#, encoding = 'utf-8')
# model = gensim.models.Word2Vec.load_word2vec_format('/Users/MohammadReza/Desktop/Uni/Programs/AI_HW2/FinalModel')
model = gensim.models.KeyedVectors.load_word2vec_format('/Users/MohammadReza/Desktop/Uni/Programs/AI_HW2/FinalModel')

print(model['مرد'])
print(model['زن'])
# print(model.similarity('دست', 'پا'))
# print(model.similarity('شتر', 'چین'))
# # print(model.doesnt_match('درخت', 'بشقاب', 'شاخه', 'برگ'))
# print(model.doesnt_match("دست پا موز گوش".split()))
