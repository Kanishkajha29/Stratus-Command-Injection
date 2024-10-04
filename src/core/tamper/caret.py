#!/usr/bin/env python
# encoding: UTF-8

 

import re
import sys
from src.utils import menu
from src.utils import settings

"""
About: Adds caret symbol (^) between the characters of the generated payloads.
Notes: This tamper script works against windows targets.
"""

__tamper__ = "caret"

if not settings.TAMPER_SCRIPTS[__tamper__]:
  settings.TAMPER_SCRIPTS[__tamper__] = True

def tamper(payload):
  def add_caret_symbol(payload):
    settings.TAMPER_SCRIPTS[__tamper__] = True
    if re.compile(r"\w+").findall(payload):
      long_string = ""
      if len(max(re.compile(r"\w+").findall(payload), key=lambda word: len(word))) >= 5000:
        long_string = max(re.compile(r"\w+").findall(payload), key=lambda word: len(word))
    rep = {
            "^^": "^",
            '"^t""^o""^k""^e""^n""^s"': '"t"^"o"^"k"^"e"^"n"^"s"',
            '^t^o^k^e^n^s': '"t"^"o"^"k"^"e"^"n"^"s"',
            re.sub(r'([b-zD-Z])', r'^\1', long_string) : long_string.replace("^", "")
          }
    payload = re.sub(r'([b-zD-Z])', r'^\1', payload)
    rep = dict((re.escape(k), v) for k, v in rep.items())
    pattern = re.compile("|".join(rep.keys()))
    payload = pattern.sub(lambda m: rep[re.escape(m.group(0))], payload)
    return payload

  if settings.TARGET_OS == settings.OS.WINDOWS:
    if settings.EVAL_BASED_STATE != False:
      return payload
    else:
      return add_caret_symbol(payload)
  else:
    return payload

# eof