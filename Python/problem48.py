# -*- coding:utf-8 -*-

def sumSquare(first, last):
	"""
	Compute the series first^first + ... + last^last
	"""
	result = sum(integer**integer for integer in range(first, last+1))

	return result

def main():
	"""
	The series, 1^1 + 2^2 + 3^3 + ... + 10^10 = 10405071317.

	Find the last ten digits of the series, 1^1 + 2^2 + 3^3 + ... + 1000^1000.
	"""
	result = sumSquare(1,1000)
	print(str(result)[-10:])

if __name__ == '__main__':
	main()