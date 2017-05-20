#!/usr/bin/env python

import os
import sys

basedir = os.path.dirname(os.path.realpath(__file__))
sys.path.insert(0, os.path.join(basedir, "src"))

import tankbot_web
tankbot_web.main()
