from __future__ import absolute_import, division, print_function
#for words encoding
import codecs
#regex
import glob

import multiprocessing
import os
import pprint
#regular expressions
import re
import nltk
#word to vec

all_words = ""

txt_files = glob.glob("*.txt")
#print(txt_files)

# with open('story.txt', "w") as story:
#     for item in txt_files:
#         with open(item) as single_file:
#             for line in single_file:
#                 print(line)
#                 story.write(line)

# print(story)

all_str = '.'.join([open(f).read() for f in glob.glob('*txt')])
print(all_str)