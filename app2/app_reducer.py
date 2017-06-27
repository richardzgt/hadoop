#!/usr/bin/env python

import sys

current_key = None
current_value = None
current_count = 0

for line in sys.stdin:
    key,value = line.strip().split('\t')
    # word : '20150928_1259 05983961801@ecplive.com'

    if current_key == key :
        if current_value != value:
            current_count += 1
            current_value = value
        else:
            pass
    else:
        if current_key:
            print '%s\t%s' % (current_key,current_count)
        current_count = 1
        current_key = key
        current_value = value

if current_key:
    print '%s\t%s' % (current_key,current_count)




