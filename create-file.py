import os
import argparse

parser = argparse.ArgumentParser()
parser.add_argument("FILE", help="where to put file")
args = parser.parse_args()

file = args.FILE

string = '''

\\input{../preamble.tex}

\\title{Class Code: \\
        Class Name}
\\author{Einar Balan}
\\date{}

\\begin{document}

\\maketitle
\\tableofcontents

\\end{document}
'''

with open(file, "w") as f:
    f.write(string)

