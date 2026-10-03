#!/usr/bin/env python3

import re

with open("../logs/simulation.log", "r") as file:

    pass_count = 0
    fail_count = 0
    warning_count = 0
    error_count = 0
    info_count = 0

    for line in file:

        if re.search(r"pass:", line, re.IGNORECASE):
            pass_count += 1

        elif re.search(r"fail:", line, re.IGNORECASE):
            fail_count += 1

            match = re.search(
               	r"\[(\d+:\d+:\d+)\]\s+FAIL:\s+(TEST_\d+)\s+-\s+(.*)",
                line,
                re.IGNORECASE
            )

            if match:
                test_name = match.group(1)
                reason = match.group(2)

                print(f"{test_name} -> {reason}")

        elif re.search(r"warning:", line, re.IGNORECASE):
            warning_count += 1

        elif re.search(r"error:", line, re.IGNORECASE):
            error_count += 1

        elif re.search(r"info:", line, re.IGNORECASE):
            info_count += 1


print(f"there are total {pass_count} test passed")
print(f"there are total {fail_count} test failed")
print(f"there are total {warning_count} Warnings")
print(f"there are total {error_count} Error in the file.")
print(f"there are total {info_count} info Message in file.")
