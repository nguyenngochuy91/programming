# -*- coding: utf-8 -*-
"""
Created on Sat Oct  5 23:03:33 2019

@author: huyn
"""
#5216. Count Vowels Permutation
def countVowelPermutation(n: int) -> int:
    d= {"a":"e","e":"ai","i":"aeou","o":"iu","u":"a"}
    if n==1:
        return 5
    count = {"a":1,"e":1,"i":1,"o":1,"u":1}
    for i in range(n-1):
        newcount = {"a":0,"e":0,"i":0,"o":0,"u":0}
        for letter in "aeiou":
            for possible in d[letter]:
                newcount[possible]+=count[letter]
        count = {key:newcount[key]%(10**9+7) for key in newcount}

    res = 0
    for key in count:
        res= (res+count[key])%(10**9+7)
    return res