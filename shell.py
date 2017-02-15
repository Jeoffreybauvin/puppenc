#!/usr/bin/env python
import os
import readline
from pprint import pprint

from flask import *
from app.puppenc import app, db

os.environ['PYTHONINSPECT'] = 'True'
