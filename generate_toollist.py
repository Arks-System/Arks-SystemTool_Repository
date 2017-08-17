#!/usr/bin/env python3

import os
import sys
import hashlib
from stat import *

BASEDIR=os.path.dirname(os.path.realpath(__file__))
REPO="%s/" % (os.path.join(BASEDIR, "repository"))
INGORE=["toollist.txt", "versions.txt"]

def hash_md5(file):
    BLOCKS = 65536
    hasher = hashlib.md5()
    with open(file, 'rb') as afile:
        buf = afile.read(BLOCKS)
        while (len(buf) > 0):
            hasher.update(buf)
            buf = afile.read(BLOCKS)
    return (hasher.hexdigest().upper())

if __name__ == "__main__":
    for root, dirs, files in os.walk(REPO):
        for e in INGORE:
            if (e in files):
                files.remove(e)
        for f in files:
            path = os.path.join(root.replace(REPO, ""), f)
            h = hash_md5(os.path.join(root, f))
            size = os.stat(os.path.join(root, f))[ST_SIZE]
            print("%s\t%s\t%d" % (path, h, size))
