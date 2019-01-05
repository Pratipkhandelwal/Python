#!/bin/python3

import math
import os
import random
import re
import sys

for t in range(int(input())):
    n = int(input())
    a = list(map(int,input().split()))
    a.sort()
    count = [0,1,1,2,2]
    for i in range(1,n):
        for j in range(5):
            d = a[i] - a[0] + j
            count[j] += d // 5
            d %= 5
            count[j] += d // 2
            d %= 2
            count[j] += d
            print(a[i],count)
    print(min(count))
