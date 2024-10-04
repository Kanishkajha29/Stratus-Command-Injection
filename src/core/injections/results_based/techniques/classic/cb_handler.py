#!/usr/bin/env python
# encoding: UTF-8

 

from src.core.injections.controller import handler

"""
The "classic" technique on result-based OS command injection.
"""

"""
The "classic" injection technique handler.
"""
def cb_injection_handler(url, timesec, filename, http_request_method, injection_type, technique):
  return handler.do_results_based_proccess(url, timesec, filename, http_request_method, injection_type, technique)

"""
The exploitation function.
(call the injection handler)
"""
def exploitation(url, timesec, filename, http_request_method, injection_type, technique):
  return cb_injection_handler(url, timesec, filename, http_request_method, injection_type, technique)

# eof
