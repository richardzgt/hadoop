#!/usr/bin/env python

import sys
import re

for line in sys.stdin:
    key,value = line.strip().split('\t')
    print  '%s_%s' % (key,value)       


