#!/usr/bin/env python
import os, sys
import readline
from pprint import pprint
from flask import *
from app import puppenc
os.environ['PYTHONINSPECT'] = 'True'

import argparse
parser = argparse.ArgumentParser()
parser.add_argument("setup", help="do the initial setup")
args = parser.parse_args()
if args.setup:
    puppenc.init_db()
    sys.exit()
