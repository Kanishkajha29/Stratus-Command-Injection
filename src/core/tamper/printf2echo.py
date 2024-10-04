#!/usr/bin/env python
# encoding: UTF-8

 

from src.utils import settings

"""
About: Replaces the printf-based ASCII to Decimal `printf "%d" "'$char'"` with `echo -n $char | od -An -tuC | xargs`.
Notes: This tamper script works against Unix-like target(s)
"""

__tamper__ = "printf2echo"

settings.TAMPER_SCRIPTS[__tamper__] = True

def tamper(payload):
  def printf_to_echo(payload):
    if "printf" in payload:
      payload = payload.replace("str=$(printf" + settings.WHITESPACES[0] + "'%d'" + settings.WHITESPACES[0] + "\"'$char'\")", "str=$(echo" + settings.WHITESPACES[0] + "-n" + settings.WHITESPACES[0] + "$char" + settings.WHITESPACES[0] + "|" + settings.WHITESPACES[0] + "od" + settings.WHITESPACES[0] + "-An" + settings.WHITESPACES[0] + "-tuC" + settings.WHITESPACES[0] + "|" + settings.WHITESPACES[0] + "xargs)")
    return payload

  return printf_to_echo(payload)

# eof