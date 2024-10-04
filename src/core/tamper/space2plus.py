#!/usr/bin/env python
# encoding: UTF-8

 

from src.utils import settings

"""
About: Replaces space character ('%20') with plus ('+').
Notes: This tamper script works against all targets.
"""

__tamper__ = "space2plus"
space2plus = "+"

if not settings.TAMPER_SCRIPTS[__tamper__]:
  settings.TAMPER_SCRIPTS[__tamper__] = True

def tamper(payload):
  settings.TAMPER_SCRIPTS[__tamper__] = True
  if settings.WHITESPACES[0] == "%20":
    settings.WHITESPACES[0] = space2plus
  elif space2plus not in settings.WHITESPACES:
    settings.WHITESPACES.append(space2plus)
  return payload

# eof