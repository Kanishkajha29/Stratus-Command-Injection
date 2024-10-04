#!/usr/bin/env python
# encoding: UTF-8

 

import random
from src.utils import settings

"""
About: Adds multiple spaces around OS commands
Notes: Useful to bypass very weak and bespoke web application firewalls that has poorly written permissive regular expressions.
"""

__tamper__ = "multiplespaces"

def tamper(payload):
  if not (settings.TAMPER_SCRIPTS[__tamper__]):
    settings.TAMPER_SCRIPTS[__tamper__] = True
    for i in range(0, len(settings.WHITESPACES)):
      settings.WHITESPACES[i] = settings.WHITESPACES[i] * random.randrange(3, 8)
  return payload
# eof