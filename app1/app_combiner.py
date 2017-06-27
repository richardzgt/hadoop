#!/usr/bin/env python

import sys

curr_key = ''
curr_count = 0

for line in sys.stdin:
    key,count = line.split('\t')

    try:
        count=int(count)
    except ValueError:
        continue

    if curr_key == key:
        curr_count += count
    else:
        if curr_key:
            print '%s\t%s' % (curr_key,curr_count)
        curr_count = count
        curr_key = key

if curr_key == key:
    print '%s\t%s' % (curr_key,curr_count)


