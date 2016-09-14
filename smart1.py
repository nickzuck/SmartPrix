#!/usr/bin/python
import re

replacement = raw_input().split()

format_string = raw_input().split()

answer = ""
count = 0

for i in format_string:
	
	if re.match("%s\[(\d)\]:(\d)",i) is not None:
		
		match = re.match("%s\[(\d)\]:(\d)",i)

		answer += i.replace(match.group(0),replacement[int(match.group(1))][:int(match.group(2))]) + " "


	elif re.match("%s\[(\d)\]",i) is not None:

		match = re.match("%s\[(\d)\]",i)

		answer += i.replace(match.group(0),replacement[int(match.group(1))]) + " "

	elif re.match("%s:(\d)",i) is not None:

		match = re.match("%s:(\d)",i)

		answer += i.replace(match.group(0),replacement[count][:int(match.group(1))]) + " "

		count += 1

	elif re.match("%s",i) is not None:

		answer += i.replace("%s",replacement[count]) + " "

		count += 1

	else:
		answer += i + " "

print answer










