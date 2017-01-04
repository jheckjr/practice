'''
Problem:
Hacker Rank - Counter Game
'''

### TODO ###
#include <cmath>
#include <cstdio>
#include <vector>
#include <iostream>
#include <algorithm>
using namespace std;
// subtract one and count ones

int main() {
    /* Enter your code here. Read input from STDIN. Print output to STDOUT */ 
    int cases = 0;
    cin >> cases;
    unsigned long long num = 0;

    for (int i = 0; i < cases; i++) {
        cin >> num;
        int count = 0;
        num--;
        
        while (num) {
            num &= (num-1);
            count++;
        }
        
        if (count & 1)
            cout << "Louise\n";
        else
            cout << "Richard\n";
    }
    
    
    return 0;
}


'''
Louise
'''