import os
import sys
from subprocess import run
import glob

ignored_patterns = []
with open('.gitignore') as gitignore:
    for line in gitignore:
        ignored_patterns.append(line.strip())

for pattern in ignored_patterns:
    for file in glob.glob(pattern):
        print(file)
        run(['git', 'rm', '--cached', '--', file], shell=True,
            cwd=os.path.dirname(os.path.realpath(__file__)) )
        #git.remove(file, )