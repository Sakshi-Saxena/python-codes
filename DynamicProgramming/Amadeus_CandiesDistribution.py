# Candies Distribution

# Chef has N boxes arranged in a line. Each box has some candles in it say C[I]. 
# Chef wants to distribute all the candies between of his friends: A and B, 
# in the following way A starts eating candies kept in the leftmost box(box at 1st place) and B 
# starts eating candies kept in the rightmost box(box at Nth place). A eats candies X times faster than B 
# le. A eats X candles when B eats only 1. Candies in each box can be eaten by only the person who reaches
# that box first. If both reach a box at the same time, then the one who has eaten from more number of BOXES
# till now will eat the candies in that box. If both have eaten from the same number of boxes till now then
# A will eat the candies in that box. Find the number of boxes finished by both A and B.NOTE- We assume 
# that it does not take any time to switch from one box to another

# Input: First line will contain Ti number of testcases. Then the testcases follow Each testcase 
# contains three lines of input The first line of each test case contains N the number of boxes. 
# second line of each test case contains a sequence C1 C2 CB The CN where Cl denotes the number of candles 
# in the ith box The third line of each test case contains an integer X

# Output For each testcase, print two space separated integers in a new line - 
# the number of boxes eaten by A and B respectively.

# Constraints 1ST 100. 1N 200000. 1C 1000000 1

# SX 10. Sum of N over all test cases does not exceed 300000

n = int(input())
arr = list(map(int, input().split()))
x = int(input())
s, e, a, b = 0, n-1, 0, 0
while(s<e):
    if(s+x > e and a > b):
        a+=x
    elif(s+x > e and b > a):
        b+=1
    else:
        a+=x
        b+=1
    s+=x
    e-=1 

if(s == e):
    if(a>b):
        a+=x
    else:
        b+=1
    
print(a , b)
