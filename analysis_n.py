#!/usr/bin/python
__author__ = 'cannon'


import string
import os
import random
import sys


def analyze(order):
    already_processed = []

    titles = {}

    files = [f for f in os.listdir('./text') if os.path.isfile("./text/" + f)]
    for f in files:
        if f.endswith(".txt"):
            with open("./text/" + f, "r") as read_file:
                for line in read_file:
                    params = string.rsplit(line, "***")
                    if params[1] not in already_processed:
                        titles[params[1]] = params[0]
                        already_processed.append(params[1])

    titles_data = []

    for title in titles.values():
        list_rep = string.rsplit(title)
        word_length = len(list_rep)

        local_chars = list(title)

        titles_data.append((word_length, len(local_chars), local_chars))

    n = 0
    word_sum = 0
    char_sum = 0

    combos = {}

    if len(titles_data) > 0:
        for title_data in titles_data:
            n += 1
            word_sum += title_data[0]
            char_sum += title_data[1]
            for x in range(0, len(title_data[2]) - 2):
                combo = ""
                for i in range(0, order):
                    combo += str(title_data[2][x+i])
                if combo not in combos:
                    combos[combo] = 1
                else:
                    combos[combo] += 1

        word_avg = word_sum / n
        char_avg = char_sum / n

        print "Word length Average: %s" % word_avg
        print "Character length Average: %s" % char_avg

    probs = {}

    total = sum(combos.values())

    for combo in combos.keys():
        probs[combo] = float(combos.get(combo)) / float(total)

    print sorted(probs.items(), key=lambda x: x[1], reverse=True)

    return_string = ""
    while len(return_string) < 40:
        if len(return_string) > order > 1:
            last_one = return_string[-(order - 1):]
            sub_prob = {}
            for key, value in probs.iteritems():
                if key[:-1] is last_one:
                    sub_prob[key] = value

            sub_prob_total = sum(sub_prob.values())
            r, s = random.random() * sub_prob_total, 0

            for key, value in sub_prob.iteritems():
                s += value
                if s >= r:
                    return_string += key[order - 1]
                    break
        else:
            r, s = random.random(), 0
            for key, value in probs.iteritems():
                s += value
                if s >= r:
                    return_string += key
                    break

    return return_string

if __name__ == "__main__":
    if len(sys.argv) > 1:
        print analyze(int(sys.argv[1]))
    else:
        print analyze(2)
