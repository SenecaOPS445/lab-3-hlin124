#!/usr/bin/env python3
#Author ID: hlin124

import os
import subprocess
p = subprocess.Popen(["df -h | grep /$ | awk '{print $4}'"], stdout=subprocess.PIPE, stdin=subprocess.PIPE, stderr=subprocess.PIPE, shell=True)

def free_space():
    output = p.communicate()
    stdout = output[0].decode('utf-8').strip()
    return stdout

print(free_space())
