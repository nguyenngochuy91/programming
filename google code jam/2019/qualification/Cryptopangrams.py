# -*- coding: utf-8 -*-
"""
Problem

On the Code Jam team, we enjoy sending each other pangrams, which are phrases 
that use each letter of the English alphabet at least once. One common example of a pangram 
is "the quick brown fox jumps over the lazy dog". Sometimes our pangrams contain confidential information — 
for example, CJ QUIZ: KNOW BEVY OF DP FLUX ALGORITHMS — so we need to keep them secure.

We looked through a cryptography textbook for a few minutes, and we learned that 
it is very hard to factor products of two large prime numbers, so we devised an encryption scheme 
based on that fact. First, we made some preparations:

We chose 26 different prime numbers, none of which is larger than some integer N.
We sorted those primes in increasing order. Then, we assigned the smallest prime to the letter A, 
the second smallest prime to the letter B, and so on.
Everyone on the team memorized this list.
Now, whenever we want to send a pangram as a message, we first remove all spacing to form a plaintext message. 
Then we write down the product of the prime for the first letter of the plaintext and the prime for the second 
letter of the plaintext. Then we write down the product of the primes for the second and third plaintext letters, 
and so on, ending with the product of the primes for the next-to-last and last plaintext letters. 
This new list of values is our ciphertext. The number of values is one smaller than the number of 
characters in the plaintext message.

For example, suppose that N = 103 and we chose to use the first 26 odd prime numbers, 
because we worry that it is too easy to factor even numbers. 
Then A = 3, B = 5, C = 7, D = 11, and so on, up to Z = 103. Also suppose that we want to encrypt the CJ QUIZ... 
pangram above, so our plaintext is CJQUIZKNOWBEVYOFDPFLUXALGORITHMS. 
Then the first value in our ciphertext is 7 (the prime for C) times 31 (the prime for J) = 217;
 the next value is 1891, and so on, ending with 3053.

We will give you a ciphertext message and the value of N that we used. 

We will not tell you which primes we used, or how to decrypt the ciphertext. Do you think you can recover the plaintext anyway?
Input

The first line of the input gives the number of test cases, T. T test cases follow; 
each test case consists of two lines. The first line contains two integers: N, as described above, and L, the length of the list of values in the ciphertext.
 The second line contains L integers: the list of values in the ciphertext.
Output

For each test case, output one line containing Case #x: y, where x is the test case 
number (starting from 1) and y is a string of L + 1 uppercase English alphabet letters: the plaintext.
"""
import sys
from math import gcd
T = int(input().strip())
def solve(array):
    result = ""
    unrepeated = [array[0]]
    for item in array:
        if item != unrepeated[-1]:
            unrepeated.append(item)
    alphabet = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
    primes = set()
    # array store need resolve number, for example, AB, BA gives gcd AB
    for i in range(len(unrepeated)-1):
        num1,num2 = unrepeated[i],unrepeated[i+1]
        largestGCD = gcd(num1,num2)
        primes.add(largestGCD)
        # we can find the previous prime
        previousPrime = num1/largestGCD
        afterPrime    = num2/largestGCD
        primes.add(previousPrime)
        primes.add(afterPrime)     
        if len(primes)==26:
            break
    primes = sorted(list(primes))

    unresolved = []
    d = {primes[i]:alphabet[i] for i in range(26)}
#    print (d)
    currentPrime = None
    for i in range(len(array)-1):
        num1,num2 = array[i],array[i+1]
        if num1 == num2:
            if currentPrime: # our currentPrime basically would be the connection
                result+= d[currentPrime]
                nextPrime    = num2/currentPrime
                currentPrime  = nextPrime
            else:
                unresolved.append(num1)
        else: # CASE AB,BC
            # find the set
            if not currentPrime:
                for item in primes:
                    if num1%item ==0:
                        firstSet = [num1/item,item]
                    if num2% item ==0:
                        secondSet = [num2/item,item]
                for item in firstSet:
                    if item in secondSet:
                        currentPrime = item
                        break
                firstSet.remove(item)
                previousPrime = firstSet[0]
                secondSet.remove(item)
                nextPrime     = secondSet[0]
                result+=d[previousPrime]+d[currentPrime]
#                print (unresolved)
                for item in unresolved[::-1]:
                    prime = item/previousPrime
#                    print (d[prime])
                    result=d[prime]+result
                    previousPrime = prime
                currentPrime = nextPrime
            else:
                result+=d[currentPrime]
                currentPrime = num2/currentPrime
    result+=d[currentPrime]       
    return result
            
def generateTest():
    d  = {2.0: 'A',
 89.0: 'B',
 109.0: 'C',
 211.0: 'D',
 239.0: 'E',
 353.0: 'F',
 479.0: 'G',
 601.0: 'H',
 701.0: 'I',
 827.0: 'J',
 883.0: 'K',
 1021.0: 'L',
 1051.0: 'M',
 1087.0: 'N',
 1277.0: 'O',
 1381.0: 'P',
 1531.0: 'Q',
 1571.0: 'R',
 1669.0: 'S',
 1861.0: 'T',
 1973: 'U',
 1997.0: 'V',
 2137.0: 'W',
 2213.0: 'X',
 2281.0: 'Y',
 2411.0: 'Z'}
    x=  {'A': 2.0,
 'B': 89.0,
 'C': 109.0,
 'D': 211.0,
 'E': 239.0,
 'F': 353.0,
 'G': 479.0,
 'H': 601.0,
 'I': 701.0,
 'J': 827.0,
 'K': 883.0,
 'L': 1021.0,
 'M': 1051.0,
 'N': 1087.0,
 'O': 1277.0,
 'P': 1381.0,
 'Q': 1531.0,
 'R': 1571.0,
 'S': 1669.0,
 'T': 1861.0,
 'U': 1973,
 'V': 1997.0,
 'W': 2137.0,
 'X': 2213.0,
 'Y': 2281.0,
 'Z': 2411.0}   

for i in range(T):
    sys.stdout.flush()
    N,L = [int(i) for i in input().strip().split()]
    array = [int(i) for i in input().strip().split()]
    result = solve(array)
    print ("Case #{}: {}".format(i+1,result))