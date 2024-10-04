#!/usr/bin/env python
# encoding: UTF-8

 

from src.core.injections.controller import handler

"""
The "file-based" technique on semiblind OS command injection.
"""

"""
The "file-based" injection technique handler
"""
def fb_injection_handler(url, timesec, filename, http_request_method, url_time_response, injection_type, technique):
  return handler.do_results_based_proccess(url, timesec, filename, http_request_method, injection_type, technique)

"""
The exploitation function.
(call the injection handler)
"""
def exploitation(url, timesec, filename, http_request_method, url_time_response, injection_type, technique):
  return fb_injection_handler(url, timesec, filename, http_request_method, url_time_response, injection_type, technique)

# eof
