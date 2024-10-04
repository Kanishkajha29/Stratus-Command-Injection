#!/usr/bin/env python
# encoding: UTF-8

 

import sys
from src.utils import menu
from src.utils import settings

"""
About: Replaces slashes (/) with environment variable value "${PATH%%u*}".
Notes: This tamper script works against Unix-like target(s).
Reference: https://www.secjuice.com/bypass-strict-input-validation-with-remove-suffix-and-prefix-pattern/
"""

__tamper__ = "slash2env"

if not settings.TAMPER_SCRIPTS[__tamper__]:
  settings.TAMPER_SCRIPTS[__tamper__] = True

def tamper(payload):
  def add_slash2env(payload):
    settings.TAMPER_SCRIPTS[__tamper__] = True
    payload = payload.replace("/", "${PATH%%u*}")
    return payload

  if settings.TARGET_OS != settings.OS.WINDOWS:
    if settings.EVAL_BASED_STATE != False:
      return payload
    else:
      return add_slash2env(payload)
  else:
    return payload

# eof