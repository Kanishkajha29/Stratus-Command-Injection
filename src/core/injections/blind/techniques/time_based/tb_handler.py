#!/usr/bin/env python
# encoding: UTF-8

 

from src.utils import common
from src.utils import settings
from src.core.injections.controller import checks
from src.core.injections.controller import handler

"""
The "time-based" injection technique on Blind OS Command Injection.
"""

"""
The "time-based" injection technique handler.
"""
def tb_injection_handler(url, timesec, filename, http_request_method, url_time_response, injection_type, technique, tmp_path):
  return handler.do_time_relative_proccess(url, timesec, filename, http_request_method, url_time_response, injection_type, technique, tmp_path)

"""
The exploitation function.
(call the injection handler)
"""
def exploitation(url, timesec, filename, http_request_method, url_time_response, injection_type, technique):
  # Check if attack is based on time delays.
  if not settings.TIME_RELATIVE_ATTACK :
    checks.time_relative_attaks_msg()
    settings.TIME_RELATIVE_ATTACK = True

  if url_time_response >= settings.SLOW_TARGET_RESPONSE:
    warn_msg = "It is highly recommended, due to serious response delays, "
    warn_msg += "to skip the time-based (blind) technique and to continue "
    warn_msg += "with the file-based (semiblind) technique."
    settings.print_data_to_stdout(settings.print_warning_msg(warn_msg))
    go_back = False
    while True:
      if go_back == True:
        return False
      message = "How do you want to proceed? [(C)ontinue/(s)kip] > "
      proceed_option = common.read_input(message, default="C", check_batch=True)
      if proceed_option.lower() in settings.CHOICE_PROCEED :
        if proceed_option.lower() == "c":
          if tb_injection_handler(url, timesec, filename, http_request_method, url_time_response, injection_type, technique) == False:
            return False
        elif proceed_option.lower() == "s":
          from src.core.injections.semiblind.techniques.file_based import fb_handler
          fb_handler.exploitation(url, timesec, filename, http_request_method, url_time_response, injection_type, technique)
        elif proceed_option.lower() == "q":
          raise SystemExit()
      else:
        common.invalid_option(proceed_option)
        pass
  else:
    tmp_path = ""
    if tb_injection_handler(url, timesec, filename, http_request_method, url_time_response, injection_type, technique, tmp_path) == False:
      settings.TIME_RELATIVE_ATTACK = False
      return False
# eof
