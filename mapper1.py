#!/usr/bin/env python
import sys

# get all lines from stdin
for line in sys.stdin:
    # remove leading and trailing whitespace
    line = line.strip()

    # convert line to lowercase
    line = line.lower()

    # split the line into words; splits on any whitespace
    words = line.split()

    # define the set of stopwords
    stopwords = set(['the','and'])

    # output tuples (word, 1) in tab-delimited format
    for word in words:
        if word not in stopwords:
            print '%s\t%s' % (word, "1")
