#!/usr/bin/env python
# encoding: UTF-8

 

import os
import sys

from src.utils import menu
from src.utils import settings
from src.thirdparty.colorama import Fore, Back, Style, init

"""
Load modules
"""
def load_modules(url, http_request_method, filename):

  # Check if defined the shellshock module
  if menu.options.shellshock :
    try:
      # The shellshock module
      from src.core.modules.shellshock import shellshock
      # The shellshock handler
      shellshock.shellshock_handler(url, http_request_method, filename)
    except ImportError as err_msg:
      settings.print_data_to_stdout("\n" + settings.print_critical_msg(err_msg))
      raise SystemExit()
    raise SystemExit()