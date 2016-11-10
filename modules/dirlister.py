#!/usr/bin/python2.7

import os

def run(**args):

    print "[*] In dirlister module."
    files = os.dirlister(".")

    return str(files)
