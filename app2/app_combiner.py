#!/usr/bin/env python

import sys

current_key = None
current_value = None

for line in sys.stdin:
    key,value = line.strip().split('\t')

    if current_key == key:
        if current_value != value:
            print '%s\t%s' % (current_key,current_value)
            current_value = value
        else:
            pass
    else:
        if current_key:
            print '%s\t%s' % (current_key,current_value)
        current_key = key
        current_value = value

if current_key:
    print '%s\t%s' % (current_key,current_value)


