PackageProblem
==============

Code for trying to solve PackageProblem from CodeEval

Description (from CodeEval)

Challenge Description:

You want to send your friend a package with different things. 
Each thing you put inside of a package has such parameters as index number, weight and cost. 
The package has a weight limitation. 
Your goal is to determine which things to put into the package so that the total weight is less than or equal to the package limit and the total cost is as large as possible. 
This is a variation of Knapsack problem

Input sample:

Your program should accept as its first argument a path to a filename. The input file contains several lines. Each line is one test case. 

Each line contains the weight that a package can take (before the colon) and the list of things you need to pick from. Each thing is enclosed in parentheses where 1st number is a thing's index number, the 2nd is it's weight and the 3rd is it's cost. E.g.

81 : (1,53.38,$45) (2,88.62,$98) (3,78.48,$3) (4,72.30,$76) (5,30.18,$9) (6,46.34,$48)

8 : (1,15.3,$34)

75 : (1,85.31,$29) (2,14.55,$74) (3,3.98,$16) (4,26.24,$55) (5,63.69,$52) (6,76.25,$75) (7,60.02,$74) (8,93.18,$35) (9,89.95,$78)

56 : (1,90.72,$13) (2,33.80,$40) (3,43.15,$10) (4,37.97,$16) (5,46.81,$36) (6,48.77,$79) (7,81.80,$45) (8,19.36,$79) (9,6.76,$64)
Output sample:

For each set of things produce a list of things (their index numbers separated by comma) that you put into the package. E.g.

4
-
2,7
8,9
Constraints: 
Max weight any package can take is <= 100. 
There might be up to 15 things you need to choose from. 
Max weight and max cost of any thing is <= 100.
