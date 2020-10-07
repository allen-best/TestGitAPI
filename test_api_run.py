# -*- coding: utf-8 -*-
"""
Updated Jan 21, 2018
The primary goal of this file is to demonstrate a simple unittest implementation

@author: jrr
@author: rk
"""

import unittest
from unittest.mock import patch, Mock

from api_run import printRepos

# This code implements the unit test functionality
# https://docs.python.org/3/library/unittest.html has a nice description of the framework

class TestApiRun(unittest.TestCase):
    # define multiple sets of tests as functions with names that begin
    successful_response = {
        "id": "allen-best",
        "statusCodeUser": 200,
        "repoCount": 2,
        "stats": [
            {
                "Repo":"allen-best", 
                "Commits": 2
            },
            {
                "Repo":"allen-best", 
                "Commits": 20
            }
        ]
    }

    def testStatusCodeUser(self): 
        with patch('api_run.printRepos') as mock_get:
            mock_get.return_value = Mock()
            mock_get.return_value.json.return_value = self.successful_response
        self.assertEqual(printRepos("allen-best")["statusCodeUser"],200)

    def testRepoCountLength(self): 
        with patch('api_run.printRepos') as mock_get:
            mock_get.return_value = Mock()
            mock_get.return_value.json.return_value = self.successful_response
        self.assertEqual(printRepos("allen-best")["repoCount"],2)

    def testCheckFirstRepo(self): 
        with patch('api_run.printRepos') as mock_get:
            mock_get.return_value = Mock()
            mock_get.return_value.json.return_value = self.successful_response
        self.assertEqual(printRepos("allen-best")["stats"][1],{"Repo":"allen-best.github.io", "Commits": 20})
    

if __name__ == '__main__':
    print('Running unit tests')
    unittest.main()