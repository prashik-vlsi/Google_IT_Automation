#!/usr/bin/env python3

import re

with open("../logs/simulation.log","r") as file:
	count =0
	for line in file:
		if re.search(r"Pass", line, re.IGNORECASE):
			count +=1 
print(f"there are {count} pass present in log file")
