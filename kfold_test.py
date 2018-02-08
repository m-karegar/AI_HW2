from normalizer import normalize
from w2v import Line2Vector
from sklearn.svm import SVC
from sklearn.model_selection import cross_validate

import random

trainAddress = input('Enter train data address: ')
targetAddress = input('Enter target address: ')

# normalize(trainAddress)

data = open(trainAddress + '_rem_stop_word.txt', 'r').readlines()
target = open(targetAddress, 'r').readlines()

converter = Line2Vector(data)

vectorSentences = []
vectorTestData = []

for i in range(len(target)):
    target[i] = int(target[i])

combined = list(zip(data, target))
random.shuffle(combined)
data[:], target[:] = zip(*combined)

total = min(5000, len(data))

for line in data[:total]:
    vectorSentences.append(converter.get_vector(line))

trainData = vectorSentences[:total]
trainTarget = target[:total]

clf = SVC(kernel='linear')

scoring = ['accuracy', 'precision_macro', 'recall_macro']
scores = cross_validate(clf, trainData, trainTarget, scoring=scoring, cv=5, return_train_score=False)

for scr in scores:
    print(scr + ' ' + str(scores[scr]))
