#!/usr/bin/env python
# encoding: UTF-8

 

from src.core.injections.controller import injector

"""
The "tempfile-based" injection technique on semiblind OS command injection.
__Warning:__ This technique is still experimental, is not yet fully functional and may leads to false-positive resutls.
"""

"""
The main command injection exploitation.
"""
def injection(separator, maxlen, TAG, cmd, prefix, suffix, whitespace, timesec, http_request_method, url, vuln_parameter, OUTPUT_TEXTFILE, alter_shell, filename, url_time_response, technique):
  return injector.time_relative_injection(separator, maxlen, TAG, cmd, prefix, suffix, whitespace, timesec, http_request_method, url, vuln_parameter, OUTPUT_TEXTFILE, alter_shell, filename, url_time_response, technique)

"""
False Positive check and evaluation.
"""
def false_positive_check(separator, TAG, cmd, prefix, suffix, whitespace, timesec, http_request_method, url, vuln_parameter, OUTPUT_TEXTFILE, randvcalc, alter_shell, exec_time, url_time_response, false_positive_warning, technique):
  return injector.false_positive_check(separator, TAG, cmd, prefix, suffix, whitespace, timesec, http_request_method, url, vuln_parameter, OUTPUT_TEXTFILE, randvcalc, alter_shell, exec_time, url_time_response, false_positive_warning, technique)
  
# eof