#!/usr/bin/python
'''
Problem:
Hacker Rank - Almost sorted
'''

### TODO ###
# helper functions
# dec means out of order item found so check for reverse
def inOrder(arr, index):
    if index == 0:
        if 1 < len(arr):
            return arr[index] < arr[index + 1]
        else:
            return true
    elif index == len(arr) - 1:
        return arr[index - 1] < arr[index]
    else:
        return (arr[index - 1] < arr[index] and arr[index] < arr[index + 1])
    
# arr is the array, first and second are indexes
def swap(arr, first, second):
    temp = arr[first]
    arr[first] = arr[second]
    arr[second] = temp
    return arr

def reverse(arr, first, second):
    reversedArr = arr[first:second + 1]
    reversedArr.reverse()
    arr[first:second+1] = reversedArr
    return arr

def isSorted(arr):
    return all(arr[x] < arr[x+1] for x in range(0,len(arr)-1))

def checkSwap(arr, first, second):
    swapArr = list(arr)
    
    if isSorted(swap(swapArr, first, second)):
        print('yes')
        print('swap ' + str(first + 1) + ' ' + str(second + 1))
        return True
    
    return False

def checkRev(arr, first, second):
    revArr = list(arr)
    
    if isSorted(reverse(revArr, first, second)):
        print('yes')
        print('reverse ' + str(first + 1) + ' ' + str(second + 1))
        return True
        
    return False
            
# main execution
n = int(input())

array = [int(x) for x in input().split(' ')];
# start from start and end and look for out of place elements
# when pair found, try swap, then try reverse
# check for sorted
if isSorted(array):
    print('yes')
else:
    first = -1
    second = -1
    
    for x in range(0,n):
        if -1 == first and not inOrder(array, x):
            first = x
        
        if -1 == second and not inOrder(array, n - 1 - x):
            second = n - 1 - x
    
    sorted = False
    
    if -1 < first and -1 < second:
        if not checkSwap(array, first, second):
            if not checkRev(array, first, second):
                print('no')
    else:
        print('no')
    
'''
yes  
swap 1 2

no

yes
reverse 2 5

'''