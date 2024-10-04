#!/usr/bin/env python
# encoding: UTF-8

 

from src.utils import settings

"""
About: Uses backticks instead of "$()" for commands substitution on the generated payloads.
Notes: This tamper script works against Unix-like target(s).
"""

__tamper__ = "backticks"

if not settings.TAMPER_SCRIPTS[__tamper__]:
  settings.TAMPER_SCRIPTS[__tamper__] = True

def tamper(payload):
  settings.TAMPER_SCRIPTS[__tamper__] = True
  settings.USE_BACKTICKS = True
  payload = payload.replace("$((", "`expr ").replace("))", "`")
  return payload

# eof