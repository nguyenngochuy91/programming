# -*- coding: utf-8 -*-
"""
Created on Wed Oct  2 15:52:52 2019

@author: huyn
"""

#866. Prime Palindrome
#Find the smallest prime palindrome greater than or equal to N.
#
#Recall that a number is prime if it's only divisors are 1 and itself, and it is greater than 1. 
#
#For example, 2,3,5,7,11 and 13 are primes.
#
#Recall that a number is a palindrome if it reads the same from left to right as it does from right to left. 
#
#For example, 12321 is a palindrome.
def primePalindrome(self, N):
    def is_prime(n):
        return n > 1 and all(n%d for d in range(2, int(n**.5) + 1))

    for length in range(1, 6):
        #Check for odd-length palindromes
        for root in range(10**(length - 1), 10**length):
            s = str(root)
            x = int(s + s[-2::-1]) #eg. s = '123' to x = int('12321')
            if x >= N and is_prime(x):
                return x
                #If we didn't check for even-length palindromes:
                #return min(x, 11) if N <= 11 else x

        #Check for even-length palindromes
        for root in range(10**(length - 1), 10**length):
            s = str(root)
            x = int(s + s[-1::-1]) #eg. s = '123' to x = int('123321')
            if x >= N and is_prime(x):
                return x