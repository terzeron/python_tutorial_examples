#!/usr/bin/env python

import sys
import os

sys.path.append(os.path.dirname(os.path.abspath(os.path.dirname(__file__))))

from dir2 import c
c.hello()
