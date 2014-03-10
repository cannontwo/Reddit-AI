__author__ = 'cannon'

import string
import os
import operator

titles = {}

files = [f for f in os.listdir('.') if os.path.isfile(f)]
for f in files:
    if f.endswith(".txt"):
        with open(f, "r") as read_file:
            for line in read_file:
                params = string.rsplit(line, ":")
                titles[params[1]] = params[0]

titles_data = []

for title in titles.values():
    list_rep = string.rsplit(title)
    word_length = len(list_rep)

    local_chars = list(title)

    titles_data.append((word_length, len(local_chars), local_chars))

n = 0
word_sum = 0
char_sum = 0

chars = {}

for title_data in titles_data:
    n += 1
    word_sum += title_data[0]
    char_sum += title_data[1]
    for char in title_data[2]:
        if char is not ' ':
            if char not in chars:
                chars[char] = 1
            else:
                chars[char] += 1

word_avg = word_sum / n
char_avg = char_sum / n

print "Word length Average: %s" % word_avg
print "Character length Average: %s" % char_avg
print sorted(chars.items(), key=lambda x: x[1], reverse=True)
print sorted(chars, key=chars.get, reverse=True)


