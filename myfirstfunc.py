#!/bin/python3

def shownumber(msg, number):
	print("Entering shownumber() function\n")
	print(msg, number)

print("This is my first python program using functions\n")
print("Just enter numbers or press Enter to exit\n")

while True:
	try:
		line = input("enter the number: ")
		line2 = str(input("Add msg: "))
		if line and line2:
			number = int(line)
			string = str(line2)
			shownumber(number, string)
		else:
			break
	except ValueError as err:
		print(err)
