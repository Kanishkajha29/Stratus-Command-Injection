#!/usr/bin/env python
# encoding: UTF-8

 

import sys
import base64
from src.thirdparty.six.moves import urllib as _urllib
from src.utils import settings

"""
About: Base64 all characters in a given payload.
Notes: This tamper script works against all targets.
"""

__tamper__ = "base64encode"

if not settings.TAMPER_SCRIPTS[__tamper__]:
  settings.TAMPER_SCRIPTS[__tamper__] = True

def tamper(payload):
  if settings.WHITESPACES[0] == "+":
    err_msg = "Tamper script '" +  __tamper__  + "' is unlikely to work combined with the tamper script 'space2plus'."
    if settings.VERBOSITY_LEVEL == 0:
      settings.print_data_to_stdout(settings.SINGLE_WHITESPACE)
    settings.print_data_to_stdout(settings.print_critical_msg(err_msg))
    raise SystemExit()

  else:
    payload = _urllib.parse.unquote(payload)
    payload = base64.b64encode(payload.encode())
    payload = payload.decode(settings.DEFAULT_CODEC)
    return payload

# eof