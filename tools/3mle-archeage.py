#!/usr/bin/python3
import sys
import os
import argparse
import re

parser = argparse.ArgumentParser()

parser.add_argument('--nooctave', action="store_true", help="Skip octave fix")
parser.add_argument('--novolume', action="store_true", help="Skip volume fix")
parser.add_argument('-f','--infile', required=True, type=str, help='MLE file to\
        read in')

args = parser.parse_args()
# Tool to convert songs made in 3MLE or imported
# into 3MLE from a MIDI file for use in Archeage.

# What needs to be done
# If there are any instances of "l" being used, a new track must default back
# to "l4" unless it starts with an "l" setting.

octaves = {"o1": "o2",
           "o2": "o3",
           "o3": "o4",
           "o4": "o5",
           "o5": "o6",
           "o6": "o7",
           "o7": "o8"}

volumes = {"v0": "v0",
           "v1": "v9",
           "v2": "v18",
           "v3": "v26",
           "v4": "v35",
           "v5": "v43",
           "v6": "v51",
           "v7": "v60",
           "v8": "v68",
           "v9": "v76",
           "v10": "v85",
           "v11": "v93",
           "v12": "v101",
           "v13": "v110",
           "v14": "v118",
           "v15": "v127"}

def strstr(strng, replace):
    buf, i = [], 0
    while i < len(strng):
        for s, r in replace.items():
            if strng[i:len(s)+i] == s:
                buf.append(r)
                i += len(s)
                break
        else:
            buf.append(strng[i])
            i += 1
    return ''.join(buf)

def fix_length(content):
    print("length")

def fix_n_notes(strng):
    notes = ["c","c+","d","d+","e","f","f+","g","g+","a","a+","b"]
    buf, curoctave, i = [], 4, 0
    while i < len(strng):
        if strng[i] == "<":
            curoctave -= 1
        if strng[i] == ">":
            curoctave += 1
        if strng[i] == ",":
            curoctave=4
        if strng[i] == "o":
            curoctave = int(strng[i+1])
        if strng[i] == "n":
            nbuf = []
            inc=1
            if strng[i+2].isdigit():
                if strng[i+3].isdigit():
                    nbuf.extend((strng[i+1],strng[i+2],strng[i+3]))
                    inc+=2
                else:
                    nbuf.extend((strng[i+1],strng[i+2]))
                    inc+=1
                nbuf = ''.join(nbuf)
            else:
                nbuf.append(strng[i+1])
            nbuf = int(nbuf)
            text_note = notes[nbuf %12]
            note_octave = nbuf//12
            note_shift = abs(note_octave - curoctave)
            upshift = ">" * note_shift
            downshift = "<" * note_shift
            if curoctave > note_octave:
                buf.append(downshift)
                buf.append(text_note)
                buf.append(upshift)
            else:
                buf.append(upshift)
                buf.append(text_note)
                buf.append(downshift)
            i+=inc
        else:
            buf.append(strng[i])
        i+=1
    return ''.join(buf)

mle = args.infile

if not os.path.exists(mle):
    print("Error: File " + mle + " does not exist")
    sys.exit()

with open(mle) as myfile:
    content = myfile.read()

    content = content.strip("MML@") # Remove MML header

    # Use a transform to fix the octaves
    if content.find("o") and not args.nooctave:
            content = strstr(content, octaves)

    # Use a transform to fix the volumes
    if content.find("v") and not args.novolume:
            content = strstr(content, volumes)

    if content.find("n"):
        newcontent = fix_n_notes(content)

    if content.find("l"):
        fix_length(content)

print(content)
print(newcontent)
