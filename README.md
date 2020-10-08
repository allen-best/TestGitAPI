[![build status of HW05a_Mocking](https://travis-ci.org/allen-best/TestGitAPI.svg?branch=HW05a_Mocking)](https://travis-ci.org/allen-best/TestGitAPI)

# TestGitAPI Mock Version
Testing on git api calls. If the testing is failing then we have reached the max api limit for now.

Summary:
I struggled at first using mock as it was my first time using it but I found the provided links helpful as well as outside research regarding this functionality. I find the purpose of this assignment to be very informative and gave me pretty great experience/exposure to mocking when doing unnittest.

Assignment:

In last week's assignment HW 04a you may have encountered problems when testing your code in Travis-CI given that your tests were highly dependent on the GitHub APIs. Those APIs would start to return errors if you exceeded a threshold on use, or those APIs would return different results if you make a change to your repos.    Remember that one of the key concepts behind unit-tests was that if you don't change your program then the unit-tests should behave consistently.  Unfortunately that is not the case so far. 

In this assignment you will use a mocking package to "mock" your program's external dependence on GitHub, so that you can guarantee that your unit tests will run consistently ever time you run them, no matter how many times you run them, and no matter what changes you make to your repos.
