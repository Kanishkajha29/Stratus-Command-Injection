#!/usr/bin/env python
# encoding: UTF-8

 

from src.utils import settings

"""
About: Replaces space character ('%20') with vertical tab ('%0b').
Notes: This tamper script works against Windows targets.
"""

__tamper__ = "space2vtab"
space2vtab = "%0b"

if not settings.TAMPER_SCRIPTS[__tamper__]:
  settings.TAMPER_SCRIPTS[__tamper__] = True

def tamper(payload):
  if settings.TARGET_OS == settings.OS.WINDOWS:
    settings.TAMPER_SCRIPTS[__tamper__] = True
    if settings.WHITESPACES[0] == "%20":
      settings.WHITESPACES[0] = space2vtab
    elif space2vtab not in settings.WHITESPACES:
      settings.WHITESPACES.append(space2vtab)
  else:
    if space2vtab in settings.WHITESPACES:
      settings.WHITESPACES.remove(space2vtab)
  return payload

# eof