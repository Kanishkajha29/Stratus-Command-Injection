#!/usr/bin/env python
# encoding: UTF-8

 

from src.core.injections.controller import injector

"""
The "file-based" technique on semiblind OS command injection.
"""

"""
The main command injection exploitation.
"""
def injection(separator, TAG, cmd, prefix, suffix, whitespace, http_request_method, url, vuln_parameter, OUTPUT_TEXTFILE, alter_shell, filename, technique):
  return injector.results_based_injection(separator, TAG, cmd, prefix, suffix, whitespace, http_request_method, url, vuln_parameter, OUTPUT_TEXTFILE, alter_shell, filename, technique)

"""
Find the URL directory.
"""
def injection_output(url, OUTPUT_TEXTFILE, timesec, technique):
  return injector.injection_output(url, OUTPUT_TEXTFILE, timesec, technique)

"""
Command execution results.
"""
def injection_results(response, TAG, cmd, technique, url, OUTPUT_TEXTFILE, timesec):
  return injector.injection_results(response, TAG, cmd, technique, url, OUTPUT_TEXTFILE, timesec)

# eof