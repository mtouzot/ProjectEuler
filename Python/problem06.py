# -*- coding:utf-8 -*-

def squareDiff(minVal, maxVal):
	sumSquare = sum([val * val for val in range(minVal, maxVal+1)])
	squareSum = sum(range(minVal, maxVal+1)) * sum(range(minVal, maxVal+1))

	return squareSum - sumSquare

def main():
	"""
	The sum of the squares of the first ten natural numbers is,

	1²+2²+...+10² = 385
	The square of the sum of the first ten natural numbers is,

	(1+2+...+10)² = 55² = 3025
	Hence the difference between the sum of the squares of the first ten natural numbers and the square of the sum is 3025−385=2640.

	Find the difference between the sum of the squares of the first one hundred natural numbers and the square of the sum.
	"""
	minVal = 1
	maxVal = 100
	print("Problem 6 solution : ", squareDiff(minVal, maxVal))
	
if __name__ == '__main__':
	main()