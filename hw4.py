##
# @file hw4.py
# @brief homework 4
# @author Nicholas Siviglia (31360256)
# @version 1
# @date 2018-03-05

import sys
from cll import CLL

#Check input
if len(sys.argv) != 5:
    print("Invalid Parameters: hw4.py N M x D")
    sys.exit()

#Set input
N = int(sys.argv[1])
M = int(sys.argv[2])
x = int(sys.argv[3])
D = str(sys.argv[4])
print("N: %d, M: %d, x: %d, D: %s" % (N, M, x, D))

#Create object and load data into object
cll = CLL()

for i in range(1, N+1, 1):
    cll.push(i)

#Get to the starting point
for i in range(x-1):
    cll.shift(D)

#loop until one player
while cll.len() > 1:
    for i in range(M):
        cll.shift(D)
    print(cll.pop(D))

#Print the winner
print(str(cll.pop(D)) + " Won")
