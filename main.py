from hazm import *
from PersianStemmer import PersianStemmer


class custom_normalizer:
    def __init__(self, stop_word_address):
        self.stop_word_arr = []
        f = open(stop_word_address, "r", encoding="utf-8")
        self.stop_word_arr = self.extract_lines(f.read())
        self.ps = PersianStemmer()

    def normalize(self, line):
#         words = line.split(' ')
        words = word_tokenize(line)
        new_line = ""
        for word in words:
            new_line += self.ps.run(word) + " "
        temp_arr = new_line.split(' ')
        final_arr = []
        for string in temp_arr:
            if not string in self.stop_word_arr:
                final_arr.append(string)
        return final_arr

    def extract_lines(self, string):
        lines = []
        current_str = ""
        for i in range(len(string)):
            if string[i] is '\n':
                lines.append(current_str)
                current_str = ""
            else:
                current_str += string[i]
        return lines

cn = custom_normalizer("Persian_Stop_Words.txt")
print(cn.normalize(" به گزارش ایران خبر، خودروی ون حامل ماموران انتظامی و یک متهم دستگیر شده در ۱۰ کیلومتری اردستان دچار حادثه شد که یک پلیس جان خود را از دست داد و دو مامور انتظامی از ۹ مصدوم حادثه به سبب شدت جراحات با اورژانس هوایی به اصفهان و بقیه به بیمارستان شهید بهشتی اردستان منتقل شدند."))
