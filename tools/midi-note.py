#!/usr/bin/python3
import sys

notes = ["c","c+","d","d+","e","f","f+","g","g+","a","a+","b"]

n = str(sys.argv[1])
print(n + ": " + notes[int(n.strip("n")) % 12])
