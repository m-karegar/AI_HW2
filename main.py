import numpy as np
from w2v import Line2Vector
from sklearn.svm import SVC
from sklearn import metrics
from sklearn.model_selection import cross_val_score
from sklearn.model_selection import cross_validate
from sklearn.metrics import recall_score

import time
import random

startTime = time.time()


# trainAddress = input('Enter train data address:')
# targetAddress = input('Enter target address:')
# testAddress = input('Enter test data address:')
# testTargetAddress = input('Enter test target address (only for evaluation):')

data = open('/Users/MohammadReza/Desktop/Uni/Programs/AI_HW2/rem_stop_word.txt').readlines()
# data = open(trainAddress).readlines()
# target = open(testAddress).readlines()
target = open('/Users/MohammadReza/Desktop/Uni/Programs/AI_HW2/train.label').readlines()
# test = open(testAddress).readlines()
# testTarget = open(testTargetAddress).readlines()

converter = Line2Vector(data)

vectorSentences = []
vectorTestData = []


for i in range(len(target)):
    target[i] = int(target[i])
# for i in range(len(testTarget)):
#     testTarget[i] = int(testTarget[i])


combined = list(zip(data, target))
random.shuffle(combined)
data[:], target[:] = zip(*combined)

# for line in data[:21000]:
total = min(5000, len(data))

for line in data[:total]:
    vectorSentences.append(converter.get_vector(line))

# print('ccc = ' + str(converter.ccc))
# for line in test:
#     vectorTestData.append(converter.get_vector(line))

# print("w2v: " + str(time.time() - startTime))
# startTime = time.time()

trainData = vectorSentences[:int(0.9*total)]
trainTarget = target[:int(0.9*total)]

testData = vectorSentences[int(0.9*total):total]
testTarget = target[int(0.9*total):total]
# testData = vectorTestData


clf = SVC(kernel='linear')
# scores = cross_val_score(clf, trainData, trainTarget, cv=5)

scoring = ['accuracy', 'precision_macro', 'recall_macro']
scores = cross_validate(clf, trainData, trainTarget, scoring=scoring, cv=5)


for scr in scores:
    print(scr + ' ' + str(scores[scr]))

clf2 = SVC().fit(trainData, trainTarget)

predicted = clf2.predict(testData)

print(metrics.classification_report(testTarget, predicted))

f = open('/Users/MohammadReza/Desktop/Uni/Programs/AI_HW2/predicted.txt', 'w')
for item in predicted:
    f.write(str(item) + '\n')
f.close()

# print("the rest: " + str(time.time() - startTime))
