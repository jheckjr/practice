'''
Problem:
Hacker Rank - Even Tree
'''

### TODO ###
using System;
using System.Collections.Generic;
using System.IO;
class Solution {
    static void DFS(Dictionary<string, HashSet<string>> tree) {
        Stack<string> stack = new Stack<string>();
        stack.Push("1");
        HashSet<string> explored = new HashSet<string>();
        Dictionary<string, int> heights = new Dictionary<string, int>();
        int cuts = -1;
        
        while (0 < stack.Count) {
            string vertex = stack.Peek();
            
            if (!explored.Contains(vertex)) {
                int count = 0;
                foreach (string newV in tree[vertex]) {
                    if (!explored.Contains(newV) && !stack.Contains(newV)) {
                        stack.Push(newV);
                        count++;
                    }
                }
                
                if (count == 0) {
                    string last = stack.Pop();
                    explored.Add(last);
                    
                    int height = 1;
                    foreach (string v in tree[last]) {
                        if (heights.ContainsKey(v)) {
                            height += heights[v];
                        }
                    }
                    heights.Add(last, height);
                }
            }
        }
        
        foreach (string h in heights.Keys) {
            cuts = (heights[h] % 2 == 0) ? ++cuts : cuts;
        }
        Console.Write("{0} ", cuts);
    }
    
    static void Main(String[] args) {
        String[] input = Console.ReadLine().Split(' ');
        //int N = Int32.Parse(input[0]);
        int M = Int32.Parse(input[1]);
        
        Dictionary<string, HashSet<string>> tree = new Dictionary<string, HashSet<string>>();
        
        for (int i = 0; i < M; i++) {
            input = Console.ReadLine().Split(' ');
            
            if (tree.ContainsKey(input[0])) 
                tree[input[0]].Add(input[1]);
            else
                tree.Add(input[0], new HashSet<string> {input[1]});
            if (tree.ContainsKey(input[1]))
                tree[input[1]].Add(input[0]);
            else
                tree.Add(input[1], new HashSet<string> {input[0]});
        }
        
        DFS(tree);
    }
}
    
    
'''
2
'''