from hazm import *

reader = open('/Users/MohammadReza/Desktop/Uni/Semester 5/AI/HWs/2/train.content', 'r')
writer = open('rem_stop_word.txt', 'w')

stop_words = ['از', 'و', 'به', 'که', 'تا', 'در', 'با', 'را', 'هر', 'یا', '،', '.', ':', '؛', ')', '(', '«', '»', 'ی']
normalizer = Normalizer()

cnt = 0

for line in reader:
    if cnt < 100:
        norm_line = normalizer.normalize(line)
        lst = word_tokenize(norm_line)
        # for word in line.split():
        for word in lst:
            if word not in stop_words:
                writer.write(Stemmer().stem(word) + ' ')
        writer.write('\n')
    cnt += 1

reader.close()
writer.close()
