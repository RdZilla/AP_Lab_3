# 1. Слова в алфавите {a, b, c}, содержащие подслово вида bxa, где x – произвольная буква алфавита

import re
from art import tprint

tprint('Regular expressions')
pattern = r"b[a-c]a"
string = "bca, abc, baa, bba, cab, ccc, aaa, aba, bab, bcc"

match_object = re.findall(pattern, string)
print(match_object)
