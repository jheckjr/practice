'''
Problem:
Hacker Rank - Two Strings
'''

import sys

def is_funny(curr_str):
    reverse_idx = len(curr_str)
    for i in range(1,len(curr_str)):
        c_val = abs(ord(curr_str[i]) - ord(curr_str[i-1]))
        r_val = abs(ord(curr_str[reverse_idx-i]) - ord(curr_str[reverse_idx-i-1]))
        
        if c_val != r_val:
            return False
            
    return True
    
def process(f):
    output = []
    n = int(f.readline().strip())
    
    for i in range(n):
        curr_str = f.readline().strip()
        
        if is_funny(curr_str):
            output.append("Funny")
        else:
            output.append("Not Funny")
        
    return output
        
def test():
    with open('funnystring.txt', 'r') as f:
        result = process(f)
        assert result == ["Funny", "Not Funny"]
        
    print("Test passed")

test()
