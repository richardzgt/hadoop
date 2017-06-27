#!/usr/bin/env python

import sys

current_word = None
current_count = 0
word = None

for line in sys.stdin:
    word,count = line.split('\t')
    # word : '20150928_1259_05983961801@ecplive.com'
    word2 = word
    word = word[0:13]

    if current_word == word:
        current_count += 1
    else:
        if current_word:
            print '%s\t%s' % (current_word,current_count)
        current_count = 1
        current_word = word

if current_word == word:
    print '%s\t%s' % (current_word,current_count)




