#!/usr/bin/python
__author__ = 'cannon'

combos = {}

order = 3
order_word = "strings are the best strings I think string"

for i in range(0, len(order_word) - order + 1):
    partial = order_word[i:i + (order - 1)]
    next_char = order_word[i + order - 1]
    if partial not in combos.keys():
        combos[partial] = {next_char: 1}
    elif next_char in combos[partial].keys():
        combos[partial][next_char] += 1
    else:
        combos[partial][next_char] = 1

print combos