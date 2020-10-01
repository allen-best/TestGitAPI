# -*- coding: utf-8 -*-
"""
Updated Jan 21, 2018
The primary goal of this file is to demonstrate a simple unittest implementation

@author: jrr
@author: rk
"""

import unittest

from api_run import printRepos

# This code implements the unit test functionality
# https://docs.python.org/3/library/unittest.html has a nice description of the framework

class TestApiRun(unittest.TestCase):
    # define multiple sets of tests as functions with names that begin

    def testStatusCodeUser(self): 
        self.assertEqual(printRepos("allen-best")["statusCodeUser"],200)
    
    def testStatusCodeRepo(self): 
        self.assertEqual(printRepos("allen-best")["statusCodeRepo"],200)

    def testRepoCountLength(self): 
        self.assertEqual(printRepos("allen-best")["repoCount"],2)

    def testCheckFirstRepo(self): 
        self.assertEqual(printRepos("allen-best")["stats"][0],{"Repo":"allen-best.github.io", "Commits": 20})
    

if __name__ == '__main__':
    print('Running unit tests')
    unittest.main()