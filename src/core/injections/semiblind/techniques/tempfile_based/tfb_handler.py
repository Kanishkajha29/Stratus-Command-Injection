#!/usr/bin/env python
# encoding: UTF-8

 

from src.utils import settings
from src.core.injections.controller import checks
from src.core.injections.controller import handler

"""
The "tempfile-based" injection technique on semiblind OS command injection.
__Warning:__ This technique is still experimental, is not yet fully functional and may leads to false-positive results.
"""

"""
The "tempfile-based" injection technique handler
"""
def tfb_injection_handler(url, timesec, filename, http_request_method, url_time_response, injection_type, technique, tmp_path):
  return handler.do_time_relative_proccess(url, timesec, filename, http_request_method, url_time_response, injection_type, technique, tmp_path)

"""
The exploitation function.
(call the injection handler)
"""
def exploitation(url, timesec, filename, tmp_path, http_request_method, url_time_response):
  # Check if attack is based on time delays.
  if not settings.TIME_RELATIVE_ATTACK :
    checks.time_relative_attaks_msg()
    settings.TIME_RELATIVE_ATTACK = True

  injection_type = settings.INJECTION_TYPE.SEMI_BLIND
  technique = settings.INJECTION_TECHNIQUE.TEMP_FILE_BASED

  if tfb_injection_handler(url, timesec, filename, http_request_method, url_time_response, injection_type, technique, tmp_path) == False:
    settings.TIME_RELATIVE_ATTACK = settings.TEMPFILE_BASED_STATE = False
    return False

# eof