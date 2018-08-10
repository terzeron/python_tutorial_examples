#!/usr/bin/env python

import subprocess

with subprocess.Popen("ls", shell=True, stdout=subprocess.PIPE) as p:
    result, error = p.communicate()
    print(result.decode())
