from w2v import Line2Vector

converter = Line2Vector()

vectorSentences = []

trainData = open('/Users/MohammadReza/Desktop/Uni/Programs/AI_HW2/rem_stop_word.txt')

cnt = 0
for line in trainData:
    vectorSentences.append(converter.get_vector(line))
    # print(line)
    # print(vectorSentences[cnt])
    # cnt += 1
    # if cnt > 3:
    #     break

# print(vectorSentences[0])
