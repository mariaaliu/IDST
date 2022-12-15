#!/usr/bin/python3

import sys

def main():
	d = {'A': 'A', 'B': 'D', 'C': 'C', 'D': 'X', 'E': 'V', 'F': 'F', 'G': 'B', 'H': 'H', 'I': 'I', 'J': 'J', 'K': 'K', 'L': 'O', 'M': 'M', 'N': 'N', 'O': 'O', 'P': 'O', 'Q': 'Q', 'R': 'R', 'S': 'N', 'T': 'R', 'U': 'E', 'V': 'V', 'W': 'W', 'X': 'X', 'Y': 'Y', 'Z': 'M'}
        with open('readme.txt') as f:
		text = f.readline()
	for i in text:
		if i in d.keys:
			# "\033[1;34m I'm blue \033[0m"
			print("%s", d[j])
		else
			print("%s", i)

if __name__ == '__main__':
        main()

