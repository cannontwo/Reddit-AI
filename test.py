#!/usr/bin/python
__author__ = 'cannon'

import string
import os
import random
import json

already_processed = []
if os.path.isfile("already_processed.json"):
    with open("already_processed.json", "r") as read_file:
        already_processed = json.loads(read_file.read())

titles = {}

files = [f for f in os.listdir('.') if os.path.isfile(f)]
for f in files:
    if f.endswith(".txt"):
        with open(f, "r") as read_file:
            for line in read_file:
                params = string.rsplit(line, ":")
                if params[1] not in already_processed:
                    titles[params[1]] = params[0]
                    already_processed.append(params[1])

with open("already_processed.json", "w") as write_file:
    write_file.write(json.dumps(already_processed))

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

if os.path.isfile("frequencies.json"):
    with open("frequencies.json", "r") as read_file:
        chars = json.loads(read_file.read())

if len(titles_data) > 0:
    for title_data in titles_data:
        n += 1
        word_sum += title_data[0]
        char_sum += title_data[1]
        for char in title_data[2]:
            if char not in chars:
                chars[char] = 1
            else:
                chars[char] += 1

    word_avg = word_sum / n
    char_avg = char_sum / n

    print "Word length Average: %s" % word_avg
    print "Character length Average: %s" % char_avg

with open("frequencies.json", "w") as write_file:
    write_file.write(json.dumps(chars))

probs = {}

total = sum(chars.values())

for char in chars.keys():
    probs[char] = float(chars.get(char)) / float(total)

print sorted(probs.items(), key=lambda x: x[1], reverse=True)

return_string = ""
for x in range(0, 40):
    r, s = random.random(), 0
    for key, value in probs.iteritems():
        s += value
        if s >= r:
            return_string += key
            break

print return_string
