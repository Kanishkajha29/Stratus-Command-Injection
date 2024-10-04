#!/usr/bin/env python
# encoding: UTF-8

 

import re
import os
import sys
from src.utils import settings

"""
Runs the basic smoke testing
"""
def smoke_test():
    info_msg = "Executing smoke test."
    settings.print_data_to_stdout(settings.print_info_msg(info_msg))

    _ = True
    file_paths = []
    for root, directories, filenames in os.walk(settings.stratus_ROOT_PATH):
        file_paths.extend([os.path.abspath(os.path.join(root, i)) for i in filenames])

    for filename in file_paths:
      if os.path.splitext(filename)[1].lower() == ".py" and not "__init__.py" in filename:
        path = os.path.join(settings.stratus_ROOT_PATH, os.path.splitext(filename)[0])
        path = path.replace(settings.stratus_ROOT_PATH, '.')
        path = path.replace(os.sep, '.').lstrip('.')
        if "." in path:
          try:
            __import__(path)
            if settings.VERBOSITY_LEVEL != 0:
              debug_msg = "Succeeded importing '" + str(path) + "' module."
              settings.print_data_to_stdout(settings.print_debug_msg(debug_msg))
          except Exception as e:
            error_msg = "Failed importing '" + path + "' module due to '" + str(e) + "'."
            settings.print_data_to_stdout(settings.print_error_msg(error_msg))
            _ = False

    result = "Smoke test "
    if _:
      result = result + "passed."
      settings.print_data_to_stdout(settings.print_bold_info_msg(result))
    else:
      result = result + "failed."
      settings.print_data_to_stdout(settings.print_bold_error_msg(result))
    raise SystemExit()


