# Task

#Ahmed is a shoe shop owner. His shop has X number of shoes.
# He has a list containing the size of each shoe he has in his shop.
# There are N number of customers who are willing to pay Xi amount of money only if they get the shoe of their desired size.

# Your task is to compute how much money Ahmed earned.

# Input Format

# The first line contains X, the number of shoes.
# The second line contains the space separated list of all the shoe sizes in the shop.
# The third line contains N, the number of customers.
# The next N lines contain the space separated values of the shoe size  desired by the customer and Xi, the price of the shoe.


# 10
# 2 3 4 5 6 8 7 6 5 18
# 6
# 6 55
# 6 45
# 6 55
# 4 40
# 18 60
# 10 50

import sys
input = sys.stdin.readline
from collections import Counter

n = int(input())
arr = Counter(map(int, input().split()))
        
q = int(input())
ans = 0

for _ in range(q):
    a, b = map(int, input().split())
    if arr[a] > 0:
        ans += b
        arr[a] -= 1

print(ans)                                   
