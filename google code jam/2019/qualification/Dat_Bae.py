# -*- coding: utf-8 -*-
"""
Problem

A research consortium has built a new database system for their new data center. 
The database is made up of one master computer and N worker computers, which are given IDs 
from 0 to N-1. Each worker stores exactly one bit of information... which seems rather wasteful, but this is very important data!

You have been hired to evaluate the following instruction for the database:

TEST_STORE <bits>: The master reads in <bits>, which is a string of N bits, and sends the 
i-th bit to the i-th worker for storage. The master will then read the bits back from the workers and return 
them to the user, in the same order in which they were read in.
During normal operation, TEST_STORE should return the same string of bits that it read in, but unfortunately, 
B of the workers are broken!

The broken workers are correctly able to store the bits given to them, but whenever the master tries to read 
from a broken worker, no bit is returned. This causes the TEST_STORE operation to return only N-B bits, 
which are the bits stored on the non-broken workers (in ascending order of their IDs). For example, 
suppose N = 5 and the 0th and 3rd workers are broken (so B = 2). Then:

TEST_STORE 01101 returns 111.
TEST_STORE 00110 returns 010.
TEST_STORE 01010 returns 100.
TEST_STORE 11010 also returns 100.
For security reasons, the database is hidden in an underground mountain vault, so calls to
 TEST_STORE take a very long time. You have been tasked with working out which workers are broken using at most F calls to TEST_STORE.
 
Input

Initially, your program should read a single line containing a single integer T indicating the number of test cases. 
Then, you need to process T test cases.

For each test case, your program will first read a single line containing three integers N, B, and F, indicating the 
number of workers, the number of broken workers, and the number of lines you may send (as described below).

Then you may send the judge up to F lines, each containing a string of exactly N characters, each either 0 or 1.
 Each time you send a line, the judge will check that you have not made more than F calls. If you have, the judge will 
 send you a single line containing a single -1, and then finish all communication and wait for your program to finish. 
 Otherwise, the judge will send a string of length N-B: the string returned by TEST_STORE, as described above.

Once your program knows the index of the B broken workers, it can finish the test case by sending B space-separated integers: 
    the IDs of the broken workers, in sorted order. This does not count as one of your F calls.

If the B integers are not exactly the IDs of the B broken workers, you will receive a Wrong Answer verdict, and the 
judge will send a single line containing -1, and then no additional communication. If your answer was correct,
 the judge will send a single line with 1, followed by the line that begins the next test case (or exit, if that was the last test case).
"""
import sys

T = int(input().strip())
def solve(array):
    result = ""
    
    return result
            
        
                
for i in range(T):
    sys.stdout.flush()
    N,B,F = [int(i) for i in input().strip().split()]
    for i in range(F):
        print (i)
        sys.stdout.flush()
        string = input()
    print ("Case #{}: {}".format(i+1,result))
    sys.stdout.flush()