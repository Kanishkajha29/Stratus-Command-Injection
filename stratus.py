#!/usr/bin/env python
# encoding: UTF-8
import sys
try:
  __import__("src.utils.version")
  from src.utils import version
  version.python_version()

except ImportError as err:
  print(f"ImportError: {err}")
  sys.exit(1)

# Main
def main():
  import src.core.main
  # Ensure core logic from src.core.main is executed here if needed
  src.core.main.execute_main_logic()

# Main
if __name__ == '__main__':
  try:
    main()
  except SystemExit:
    raise SystemExit()
  except KeyboardInterrupt:
    raise SystemExit()
  except IndentationError as err_msg:
    from src.utils import settings
    settings.print_data_to_stdout(settings.print_critical_msg(err_msg))
    raise SystemExit()
  except Exception as e:
    from src.utils import common
    common.unhandled_exception(e)
