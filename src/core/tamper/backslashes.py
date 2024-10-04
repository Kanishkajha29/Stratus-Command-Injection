#!/usr/bin/env python
# encoding: UTF-8

 

import re
import sys
from src.utils import menu
from src.utils import settings

"""
About: Adds back slashes ("\") between the characters of the generated payloads.
Notes: This tamper script works against Unix-like target(s).
"""

__tamper__ = "backslashes"

if not settings.TAMPER_SCRIPTS[__tamper__]:
  settings.TAMPER_SCRIPTS[__tamper__] = True

def tamper(payload):
  def add_back_slashes(payload):
    settings.TAMPER_SCRIPTS[__tamper__] = True
    obf_char = "\\"
    payload = re.sub(r'([b-zD-Z])', lambda x: obf_char + x[0], payload)
    for word in settings.IGNORE_TAMPER_TRANSFORMATION:
      _ = obf_char.join(word[i:i+1] for i in range(-1, len(word), 1))
      if _ in payload:
        payload = payload.replace(_,_.replace(obf_char, ""))
    return payload

  if settings.TARGET_OS != settings.OS.WINDOWS:
    if settings.EVAL_BASED_STATE != False:
      return payload
    else:
      return add_back_slashes(payload)
  else:
    return payload

# eof