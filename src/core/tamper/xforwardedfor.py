#!/usr/bin/env python
# encoding: UTF-8

 

import random
from random import sample
from src.utils import settings
from src.core.compat import xrange

"""
About: Append a fake HTTP header 'X-Forwarded-For' (and alike).
"""

__tamper__ = "xforwardedfor"

if not settings.TAMPER_SCRIPTS[__tamper__]:
  settings.TAMPER_SCRIPTS[__tamper__] = True

def tamper(request):
  def randomIP():
    numbers = []
    while not numbers or numbers[0] in (10, 172, 192):
      numbers = sample(xrange(1, 255), 4)
    return '.'.join(str(_) for _ in numbers)
  request.add_header('X-Forwarded-For', randomIP())
  request.add_header('X-Client-Ip', randomIP())
  request.add_header('X-Real-Ip', randomIP())
  request.add_header('CF-Connecting-IP', randomIP())
  request.add_header('True-Client-IP', randomIP())
  # Reference: https://developer.chrome.com/multidevice/data-compression-for-isps#proxy-connection
  request.add_header('Via', '1.1 Chrome-Compression-Proxy')
  # Reference: https://wordpress.org/support/topic/blocked-country-gaining-access-via-cloudflare/#post-9812007
  request.add_header('CF-IPCountry', random.sample(('GB', 'US', 'FR', 'AU', 'CA', 'NZ', 'BE', 'DK', 'FI', 'IE', 'AT', 'IT', 'LU', 'NL', 'NO', 'PT', 'SE', 'ES', 'CH'), 1)[0])


# eof