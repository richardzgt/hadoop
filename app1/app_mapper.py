#!/usr/bin/env python

import sys
import re

reg_time_uid = re.compile(r'(\d{8}\s\d{4}).+\[(.+@.+\w)\s-\s')

for line in sys.stdin:
    value = reg_time_uid.match(line)
    if value is None:
        continue
    Time,Uid = value.groups()
    Time = Time.replace(' ','_')
    print "%s\t%s" % ('_'.join([Time,Uid]),1)

