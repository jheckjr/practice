#!/usr/bin/python
'''
Problem:
Hacker Rank - Almost sorted
'''

# helper functions
# dec means out of order item found so check for reverse
def inOrder(arr, index):
    if index == 0:
        if 1 < len(arr):
            return arr[index] < arr[index + 1]
        else:
            return True
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
    return all(arr[x] < arr[x+1] for x in range(len(arr)-1))

def checkSwap(arr, first, second):
    swapArr = list(arr)
    
    if isSorted(swap(swapArr, first, second)):
        result = ['yes']
        result.append('swap ' + str(first + 1) + ' ' + str(second + 1))
        return result
    
    return None

def checkRev(arr, first, second):
    revArr = list(arr)
    
    if isSorted(reverse(revArr, first, second)):
        result = ['yes']
        result.append('reverse ' + str(first + 1) + ' ' + str(second + 1))
        return result
        
    return None
            
def solve(f):
    result = []
    n = int(f.readline().strip())
    
    array = [int(x) for x in f.readline().strip().split(' ')];
    # start from start and end and look for out of place elements
    # when pair found, try swap, then try reverse
    # check for sorted
    if isSorted(array):
        result = ['yes']
    else:
        first = -1
        second = -1
        
        for x in range(n):
            if -1 == first and not inOrder(array, x):
                first = x
            
            if -1 == second and not inOrder(array, n - 1 - x):
                second = n - 1 - x
        
        if -1 < first and -1 < second:
            result = checkSwap(array, first, second)
            if not result:
                result = checkRev(array, first, second)
                if not result:
                    result = ['no']
        else:
            result = ['no']
            
    return result
    
def test():
    with open('almostsorted.txt', 'r') as f:
        result = solve(f)
        assert result[0] == 'yes'
        assert result[1] == 'swap 1 2'
        
        f.readline()
        result = solve(f)
        assert result[0] == 'no'
        
        f.readline()
        result = solve(f)
        assert result[0] == 'yes'
        assert result[1] == 'reverse 2 5'
        
    print("Test passed")
    
test()
