#!/usr/bin/env python
# encoding: UTF-8

 

from src.core.injections.controller import handler

"""
The dynamic code evaluation (aka eval-based) technique.
"""

"""
The "eval-based" injection technique handler.
"""
def eb_injection_handler(url, timesec, filename, http_request_method, injection_type, technique):
  return handler.do_results_based_proccess(url, timesec, filename, http_request_method, injection_type, technique)

"""
The exploitation function.
(call the injection handler)
"""
def exploitation(url, timesec, filename, http_request_method, injection_type, technique):
  return eb_injection_handler(url, timesec, filename, http_request_method, injection_type, technique)

# eof