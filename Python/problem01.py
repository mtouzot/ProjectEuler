# -*- coding:utf-8 -*-

def sumMultiples(a, b, minVal, maxVal):
	"""
	Find the sum of all the multiples of a or b between [minVal, maxValue[.
	"""
	try:
		result = 0
		for i in range(minVal, maxVal):
			if(i%a == 0 or i%b == 0):
				result += i
	except ZeroDivisionError:
			result = 0
			print("a ou b ne peuvent pas être égaux à zéro.")
	return result

def main():
	"""
	If we list all the natural numbers below 10 that are multiples of 3 or 5, we get 3, 5, 6 and 9. The sum of these multiples is 23.

	Find the sum of all the multiples of 3 or 5 below 1000.
	"""
	minVal = 0
	maxVal = 1000
	a = 3
	b = 5
	print(sumMultiples(a,b,minVal,maxVal))

if __name__ == '__main__':
	main()
