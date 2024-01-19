#!/usr/bin/python3
import sys
import os
txt = "and that piece of art is useful - Dora Korpar, 2015-10-19\n"
sys.stderr.write(txt)
sys.stderr.flush()
os._exit(1)
