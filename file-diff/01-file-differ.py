#!/usr/bin/python


import difflib
text1 = """ text1: 
This module provides classer and functions for comparing sequences.
including HTML and context and unified diffs.
difflib dociment v7.4
add string
"""
text1_lines = text1.splitlines()
text2 = """text2:
This module provides classes and runctions for Comparing sequences.
including HTMl and context and unified diffs.
difflib document v7.5
"""

text2_lines = text2.splitlines()
d = difflib.HtmlDiff()
print d.make_file(text1_lines,text2_lines)
