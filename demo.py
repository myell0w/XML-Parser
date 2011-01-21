#!/usr/bin/python
# -*- coding: utf-8 -*-
# "cool demo"(tm) presentation tool
# 2011-01-21 <thp.io>

import glob
import os
import sys
import time
import random

UP = '\033[A'

class color:
    RED = '\033[91m'
    GREEN = '\033[92m'
    BLUE = '\033[94m'
    ENDC = '\033[0m'

    @classmethod
    def red(cls, s):
        return cls.RED + s + cls.ENDC

    @classmethod
    def green(cls, s):
        return cls.GREEN + s + cls.ENDC

    @classmethod
    def blue(cls, s):
        return cls.BLUE + s + cls.ENDC

def box(s, c=lambda x: x):
    print '┎' + '─'*78 + '┒'
    print '┃ ' + c('%-76s'%s) + ' ┃'
    print '┖' + '─'*78 + '┚'

def faketyping(s):
    for c in s:
        sys.stdout.write(c)
        sys.stdout.flush()
        time.sleep(random.uniform(.01, .02))

files = sorted(glob.glob('input/*.xml'))

for idx, file in enumerate(files):
    os.system('clear')
    box(file + ' (%d/%d)' % (idx+1, len(files)),
        color.red if 'invalid' in file else color.green)
    print open(file).read()
    cmd = 'gs -sinputFilename=%s parser.ps' % file
    sys.stdout.write('$ ')
    sys.stdout.flush()
    raw_input()
    sys.stdout.write(UP+'$ ')
    faketyping(color.blue(cmd) + '\n')
    os.system(cmd)

os.system('clear')
box('Command line argument handling', color.red)
print """
    What if we don't specify %s?

/checkCLIParams {
    1 dict begin
        %% SE: [list of parameters] --
        /requireParameters {
            {
                dup systemdict exch known not {
                    (Missing parameter: -d) print =
                    quit
                } if
            } forall
        } def

        %% List all required parameters here
        [
            (inputFilename)
        ] requireParameters
    end
} def


""" % (color.blue('-dinputFilename=...'),)

cmd = 'gs parser.ps'
sys.stdout.write('$ ')
sys.stdout.flush()
raw_input()
sys.stdout.write(UP+'$ ')
faketyping(color.blue(cmd) + '\n')
os.system(cmd)

raw_input()

os.system('clear')
faketyping("""




                      %s



                        %s



""" % (color.red('End of parser.ps demonstration :)'),
       color.green('Thank you for your attention!')))


try:
    while True:
        raw_input()
except:
    pass

