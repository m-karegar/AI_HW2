from normalizer import normalize
from sklearn.externals import joblib
from w2v import Line2Vector
from sklearn import metrics

modelAddress = input('Enter model address: ')
testAddress = input('Enter test data address: ')
targetAddress = input('Enter target address: ')

normalize(testAddress)

test = open(testAddress + '_rem_stop_word.txt', 'r').readlines()
target = open(targetAddress, 'r').readlines()

converter = Line2Vector(test)

vectorTestData = []

for i in range(len(target)):
    target[i] = int(target[i])

for line in test:
    vectorTestData.append(converter.get_vector(line))

testData = vectorTestData

clf = joblib.load('model')

predicted = clf.predict(testData)

print(metrics.classification_report(target, predicted))

f = open('predicted.txt', 'w')
for item in predicted:
    f.write(str(item) + '\n')
f.close()
