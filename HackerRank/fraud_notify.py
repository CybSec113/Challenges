#!/bin/python3

import math
import os
import random
import re
import sys
import statistics

#
# Complete the 'activityNotifications' function below.
#
# The function is expected to return an INTEGER.
# The function accepts following parameters:
#  1. INTEGER_ARRAY expenditure
#  2. INTEGER d
#

#HackerLand National Bank has a simple policy for warning clients about possible fraudulent account activity. 
# If the amount spent by a client on a particular day is greater than or equal to 2x the client's median spending 
# for a trailing number of days, they send the client a notification about potential fraud. 
# The bank doesn't send the client any notifications until they have at least that trailing number of prior days' transaction data.
# 
# Given the number of trailing days, d, and a client's total daily expenditures for a period of n days, 
# determine the number of times the client will receive a notification over all n days.
#
# Constraints:
# 1 <= n <= 2E10**5
# 1 <= d <= n
# 0 <= expenditure[i] <= 200

def printmedian(median):
    for i in range(201):
        if median[i] > 0:
            print(i, median[i], end=',')
    print("")

def activityNotifications(expenditure, d):
    # Write your code here
    result=0

    # initialize a dictionary with count of each value from 0 to 200 to be used for running median
    median_dict = dict()
    for i in range(201):
        median_dict[i] = 0
    for i in range(d):
        median_dict[expenditure[i]] = median_dict[expenditure[i]] + 1

    # update the dictionary by removing first value and adding next value from expenditures
    def update_median_dict(a,b):
        median_dict[expenditure[a]] = median_dict[expenditure[a]] - 1
        median_dict[expenditure[b]] = median_dict[expenditure[b]] + 1

    # median is where the count > mid, with special condition if count == mid
    # dictionary always reflects current lookback period
    def median():
        count=0
        mid = (d//2)
        for i in range(201):
            count += median_dict[i]
            if count > mid:
                return i
            if count == mid:
                if d%2:
                    return i+1
                else:
                    return (2*i+1)/2

    # iterate through expenditures and count the days where expenditure[i] >= 2* median of current dictionary
    for x in range(d,len(expenditure)-1):
        if expenditure[x] >= 2*median():
            result+=1
        update_median_dict(x-d, x)

    return result

# test cases
if __name__ == '__main__':

    # test 0
    exp=[2,3,4,2,3,6,8,4,5]
    d=5
    print("Test 0:", activityNotifications(exp,d))

    # test 1
    exp=[2,3,4,2,3,6,8,4,5]
    d=5
    print("Test 1 (2):", activityNotifications(exp,d))

    # test 2
    exp=[1,2,3,4,4]
    d=4
    print("Test 2 (0):", activityNotifications(exp,d))

    # test 3
    exp=[10, 20, 30, 40, 50]
    d=3
    print("Test 3 (1):", activityNotifications(exp,d))

    # test 4 (large), input.txt
    #first_multiple_input = input().rstrip().split()
    #n = int(first_multiple_input[0])
    #d = int(first_multiple_input[1])
    #expenditure = list(map(int, input().rstrip().split()))
    #result = activityNotifications(expenditure, d)
    #print("Test 4 (633): ", result)

    # test 5 (large), input2.txt
    #first_multiple_input = input().rstrip().split()
    #n = int(first_multiple_input[0])
    #d = int(first_multiple_input[1])
    #expenditure = list(map(int, input().rstrip().split()))
    #result = activityNotifications(expenditure, d)
    #print("Test 5 (770): ", result)
