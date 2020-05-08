# -*- coding:utf-8 -*-
from math import sqrt

def maxPrimeFactor(N):
	maxPrime = -1

	while N%2 == 0:
		maxPrime = 2
		N = N / 2

	for i in range(3, int(sqrt(N))+1, 2):
		while N % i == 0:
			maxPrime = i;
			N = N / i 

	if N > 2:
		maxPrime = n
	return int(maxPrime)

def main():
	"""
	The prime factors of 13195 are 5, 7, 13 and 29.

	What is the largest prime factor of the number 600851475143 ?
	"""
	primes = maxPrimeFactor(600851475143)
	print(primes)

if __name__ == '__main__':
	main()