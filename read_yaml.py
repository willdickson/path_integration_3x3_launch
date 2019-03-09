from __future__ import print_function
import sys
import yaml

filename = sys.argv[1]

with open(filename,'r') as f:
    data = yaml.load(f)

print(data)
