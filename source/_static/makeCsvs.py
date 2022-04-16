#!/bin/python3
import os
import sys


def escape(s):
    ret = s.translate(str.maketrans({"\\": "\\\\", "\n":  ""}))
    return ret

if len(sys.argv) == 1:
    print("Usage {} <input-file>".format(sys.argv[0]))
    sys.exit()

input = open(sys.argv[1], "r")
lines = input.readlines()

list = []
for line in lines:
    list.append(":math:`{0}`,{1}\n".format(line.rstrip(),escape(line)))


f_name, f_ext = os.path.splitext(sys.argv[1])
output = open(f_name+".csv", "w")
output.writelines(list)

    