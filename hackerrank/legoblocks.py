'''
Problem:
Hacker Rank - Lego Blocks
'''

### TODO ###

#include <cmath>
#include <cstdio>
#include <vector>
#include <iostream>
#include <algorithm>
#include <string>
using namespace std;


int main() {
    /* Enter your code here. Read input from STDIN. Print output to STDOUT */   
    int t;
    cin >> t;
    
    int heights [t];
    int widths [t];
    int maxH = 0;
    int maxW = 0;
    
    for (int i = 0; i < t; i++) {
        cin >> heights[i];
        cin >> widths[i];
        
        if (maxH < heights[i]) {
            maxH = heights[i];
        }
        
        if (maxW < widths[i]) {
            maxW = widths[i];
        }
    }
    
    unsigned long A[1000][1000];
    A[0][0] = 1;
    A[0][1] = 2;
    A[0][2] = 4;
    A[0][3] = 8;
    A[0][4] = 15;
    
    for (int i = 5; i < maxW; i++) {
        A[0][i] = ((2*A[0][i-1] - A[0][i-5] + 1000000007) % 1000000007); 
    }
    
    unsigned long S[1000][1000];
    // i is height
    for (int i = 0; i < t; i++) {
        int height = heights[i] - 1;
        
        // j is width-1
        for (int j = 0; j < maxW; j++) {
            A[height][j] = A[0][j];
            
            for (int h = 1; h <= height; h++) {
                A[height][j] = (unsigned long)(A[height][j]*A[0][j]) % 1000000007;
            }
            
            unsigned long sum = 0;
            
            for (int k = 0; k < j; k++) {
                sum += (unsigned long)(S[height][k] * A[height][j-k-1]) % 1000000007;
                sum = sum % 1000000007;
            }
            
            S[height][j] = (unsigned long)(A[height][j] - sum + 1000000007) % 1000000007;
            //cout << sum << ' ' << A[height][j] << ' ' << S[height][j] << '\n';
        }
        
        cout << S[height][widths[i]-1] << '\n';
    }
    
    return 0;
}

    
'''
3  
7  
9  
3375
'''