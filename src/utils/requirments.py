#!/usr/bin/env python
# encoding: UTF-8

 
import os
import subprocess

"""
Check for requirments.
"""
def do_check(requirment):
  try:
    # Pipe output to the file path of the null device, for silence.
    # i.e '/dev/null' for POSIX, 'nul' for Windows
    null = open(os.devnull,"w")
    subprocess.Popen(requirment, stdout=null, stderr=null)
    null.close()
    return True

  except OSError:
    return False

# eof