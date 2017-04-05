#!/usr/bin/env python
import os, sys
import readline
from pprint import pprint
from flask import *
from app import puppenc
import argparse

os.environ['PYTHONINSPECT'] = 'True'
parser = argparse.ArgumentParser()

setup = False
destroy = False

parser.add_argument('--setup', action='store_true')
parser.add_argument('--destroy', action='store_true')

args = parser.parse_args()

if args.setup:
    puppenc.init_db()
    sys.exit()

elif args.destroy:
    puppenc.destroy_db()
    sys.exit()
else:
    print("Nothing to do")
    sys.exit()
