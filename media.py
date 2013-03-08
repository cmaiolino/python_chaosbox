#!/bin/python3

count = 0
total = 0

print("Write one integer per line and press enter. When finished, just press enter\n")

while True:
	try:
		line = input("Integer: ")
		if line:
			number = int(line)
			total += number
			count += 1
		else:
			break
	except ValueError as err:
		print(err)
		continue
	except EOFError:
		break	

if count:
	print("\n\n")
	print("Count:", count, "Total:", total, "Mean:", total / count)
