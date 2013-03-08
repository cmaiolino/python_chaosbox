#!/bin/python3

#This is my first (almost) robust python program

import sys

Zero =	["   ***   ", "  *   *  ", " *     * ", " *     * ", " *     * ",
	 "  *   *  ", "   ***   "]
One =	["    *    ", "   **    ", "  * *    ", "    *    ", "    *    ",
	 "    *    ", "  *****  "]
Two =	["   ***   ", "  *   *  ", "  *   *  ", "     *   ", "    *    ",
	 "   *     ", "  *****  "]
Three =	["  ****   ", "      *  ", "      *  ", "  ****   ", "      *  ",
	 "      *  ", "  ****   "]
Four =	["     *   ", "    **   ", "   * *   ", "  *  *   ", " ******  ",
	 "     *   ", "     *   "]
Five =	[" *****   ", " *       ", " *       ", " *****   ", "      *  ",
	 "      *  ", " *****   "]
Six =	["     *   ", "    *    ", "   *     ", "  *****  ", " *     * ",
	 " *     * ", "  *****  "]
Seven =	[" ******* ", "      *  ", "     *   ", "    *    ", "   *     ",
	 "  *      ", " *       "]
Eigth =	["   ***   ", "  *   *  ", " *     * ", "  *****  ", " *     * ",
	 "  *   *  ", "   ***   "]
Nine = 	["  *****  ", " *     * ", " *     * ", "  *****  ", "     *   ",
	 "    *    ", "   *     "]

Digits = [Zero, One, Two, Three, Four, Five, Six, Seven, Eigth, Nine]

try:
	digits = sys.argv[1]
	row = 0
	while row < 7:
		line = ""
		column = 0
		while column < len(digits):
			number = int(digits[column])
			digit = Digits[number]
			line += digit[row] + " "
			column += 1
		print(line)
		row += 1
except IndexError:
		print("Usage: bigdigits.py <number>\n")
except ValueError as err:
		print(err, "in", digits)
