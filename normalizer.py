from hazm import *
from PersianStemmer import PersianStemmer


def normalize(address):
    # reader = open('/Users/MohammadReza/Desktop/Uni/Semester 5/AI/HWs/2/train.content', 'r')
    reader = open(address, 'r')
    writer = open(address + '_rem_stop_word.txt', 'w')

    stop_words = open('Persian_Stop_Words.txt', 'r').read().splitlines()

    ps = PersianStemmer()

    # cnt = 0

    for line in reader:
        lst = word_tokenize(line)
        for word in lst:
            if word not in stop_words:
                writer.write(ps.run(word) + ' ')
        writer.write('\n')
    # cnt += 1

    reader.close()
    writer.close()
