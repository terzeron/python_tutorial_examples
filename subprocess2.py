#!/usr/bin/env python

import subprocess

with subprocess.Popen("sort", shell=True, stdin=subprocess.PIPE, stdout=subprocess.PIPE) as p:
    result, error = p.communicate("c\nb\na".encode())
    print(result.decode())

    
