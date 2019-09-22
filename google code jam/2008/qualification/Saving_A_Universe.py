# -*- coding: utf-8 -*-
"""
Problem

The urban legend goes that if you go to the Google homepage and search for "Google", 
the universe will implode. We have a secret to share... It is true! Please don't try it, 
or tell anyone. All right, maybe not. We are just kidding.

The same is not true for a universe far far away. In that universe, if you search on 
any search engine for that search engine's name, the universe does implode!

To combat this, people came up with an interesting solution. All queries are pooled 
together. They are passed to a central system that decides which query goes to which search engine.
 The central system sends a series of queries to one search engine, and can switch to another at any time. 
 Queries must be processed in the order they're received. The central system must never 
 send a query to a search engine whose name matches the query. 
 In order to reduce costs, the number of switches should be minimized.

Your task is to tell us how many times the central system will have to switch 
between search engines, assuming that we program it optimally.

Input

The first line of the input file contains the number of cases, N. N test cases follow.

Each case starts with the number S -- the number of search engines. 
The next S lines each contain the name of a search engine. Each search engine 
name is no more than one hundred characters long and contains only uppercase 
letters, lowercase letters, spaces, and numbers. There will not be two search engines with the same name.

The following line contains a number Q -- the number of incoming queries. 
The next Q lines will each contain a query. Each query will be the name of a search engine in the case.

Output

For each input case, you should output:
Case #X: Y
where X is the number of the test case and Y is the number of search engine switches. 
Do not count the initial choice of a search engine as a switch.
"""
# function that given list of company, and list of queries, output the least number of switch
def findLeastSwitch(queries,companies):
    numSwitch =0
    numCompanyZero = len(companies)
    dictionary = {company:0 for company in companies}
    for query in queries:
        if dictionary[query] ==0:
            if numCompanyZero==1: # have to use this company:
            # increase numSwitch
                numSwitch+=1
                numCompanyZero =len(companies)-1
                dictionary = {company:0 for company in companies}
            else: # we are still ok 
                numCompanyZero-=1
            dictionary[query]=1
        else:
             # we repeat something, go right ahead lol
             continue
    return numSwitch
def solve(infile,outfile):
    handle     = open(infile,"r")
    N          = int(handle.readline().strip())
    outfile    = open(outfile,"w")
    for testCase in range(1,N+1):
        numCompany = int(handle.readline().strip())
        companyNames = []
        for i in range(numCompany):
            name = handle.readline().strip()
            companyNames.append(name)
        numQuery = int(handle.readline().strip())
        queries = []
        for i in range(numQuery):
            query = handle.readline().strip()
            queries.append(query)
        result = findLeastSwitch(queries,companyNames)
        outfile.write("Case #{}: {}\n".format(testCase,result))
    outfile.close()
    

        