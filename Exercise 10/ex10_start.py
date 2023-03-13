# Get the directory name
import sys
import os

if sys.platform == 'win32':
    hdir = os.environ['HOMEPATH']
else:
    hdir = os.environ['HOME']

## ORIGINAL SOLUTION
##hdir = os.getcwd()
print(hdir)

## Construct a portable wildcard pattern

pattern = os.path.join(hdir, '*')
print(pattern)

# TODO: Use the glob.glob() function to obtain the list of filenames

import glob

files = glob.glob(pattern)

for file in files:
    print(file)

# TODO: use os.path.getsize to find each file's size

filesize = os.path.getsize(hdir)
print(filesize)

for file in files:
    print(os.path.getsize(file))

## NEED TO ITERATE THROUGH THE FILES TO FIND EACH FILE SIZE, NOT SURE IF THIS IS A FOR LOOP OR AN IF STATEMENT ##

# TODO: Add a test to only display files that do not have a size of zero

## ORIGINAL SOLUTION
##if os.path.getsize(file) > 0:
##print(file)

if os.path.getsize(hdir) !=0:
    print(file)

# TODO: Remove the leading directory name(s) from each filename before you print it -
# using os.path.basename()

## ORIGINAL SOLUTION
##filename = os.path.basename(hdir)
##print(filename)

for file in files:
    print(os.path.basename(file))