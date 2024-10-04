#!/usr/bin/env python
# encoding: UTF-8

 

import sys
from src.utils import settings

"""
Show version number and exit.
"""
def show_version():
  settings.print_data_to_stdout(settings.VERSION)
  raise SystemExit()

"""
Check python version number.
"""
def python_version():
  PYTHON_VERSION = sys.version.split()[0]
  if PYTHON_VERSION.split(".")[0] != "3":
    warn_msg = "Deprecated Python version detected: "
    warn_msg += PYTHON_VERSION + ". "
    warn_msg += "You are advised to re-run with Python 3."
    settings.print_data_to_stdout(settings.print_bold_warning_msg(warn_msg))

# eof