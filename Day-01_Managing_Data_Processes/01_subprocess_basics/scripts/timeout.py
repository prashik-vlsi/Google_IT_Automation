#!/usr/bin/env python3

import subprocess
try:
	subprocess.run(
	["sleep", "5"],
	timeout=2
	)
except subprocess.TimeoutExpired:
	print("Process timed out")
