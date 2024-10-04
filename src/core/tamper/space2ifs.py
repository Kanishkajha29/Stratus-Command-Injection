#!/usr/bin/env python
# encoding: UTF-8

 

from src.utils import settings

"""
About: Replaces space character ('%20') with the internal field separator ('$IFS').
The internal field separator refers to a variable which defines the character
or characters used to separate a pattern into tokens for some operations.
Notes: This tamper script works against Unix-like target(s).
"""

__tamper__ = "space2ifs"
space2ifs = "${IFS}"

if not settings.TAMPER_SCRIPTS[__tamper__]:
  settings.TAMPER_SCRIPTS[__tamper__] = True

def tamper(payload):
  if space2ifs in settings.WHITESPACES[0] and \
  settings.EVAL_BASED_STATE != False:
    settings.WHITESPACES[0] = space2ifs
  if settings.TARGET_OS != settings.OS.WINDOWS:
    settings.TAMPER_SCRIPTS[__tamper__] = True
    if settings.WHITESPACES[0] == "%20":
      settings.WHITESPACES[0] = space2ifs
    elif space2ifs not in settings.WHITESPACES:
      settings.WHITESPACES.append(space2ifs)
  else:
    if space2ifs in settings.WHITESPACES:
      settings.WHITESPACES.remove(space2ifs)
  return payload

# eof
