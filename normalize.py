#!/usr/bin/env python3
import sys
import re

args = sys.argv[1:]
if not args:
    print('Usage: normalize.py <text>', file=sys.stderr)
    sys.exit(1)

text = args[0]
slug = re.sub(r'[^a-z0-9]+', '-', text.lower())
slug = slug.strip('-')
print(slug)
