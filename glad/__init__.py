import os
import sys

__version__ = '2.0.8'

RED = "\033[0;31m"
CRESET = "\033[0m"

partial_substring = "/glad"
wanted_substring = f"{partial_substring}/glad"

execution_path = os.path.dirname(os.path.realpath(__file__))
current_dir = os.getcwd()

path_matches = execution_path.endswith(wanted_substring)
dir_matches = current_dir.endswith(partial_substring)

if (not path_matches) and (not dir_matches):
 raise Exception(f"{RED}Failed to match path for build. Package: Glad. File: /glad/__init__.py{CRESET}")

jinja_src = "vendor/jinja/src"
junji_ito = ""

if dir_matches:
  junji_ito = os.path.join(current_dir, jinja_src)

if path_matches:
  junji_ito = os.path.join(execution_path, "../", jinja_src)

sys.path.append(junji_ito)
