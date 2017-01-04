'''
Problem:
Hacker Rank - Journey to the Moon
'''

### TODO ###
using System;
using System.Collections.Generic;
using System.IO;
class Solution {
    static List<long> DFS(Dictionary<int, HashSet<int>> graph) {
        HashSet<int> allExplored = new HashSet<int>();
        List<long> groups = new List<long>();
        
        foreach (int key in graph.Keys) {
            if (!allExplored.Contains(key)) {
                Stack<int> stack = new Stack<int>();
                stack.Push(key);
                HashSet<int> explored = new HashSet<int>();

                while (0 < stack.Count) {
                    int vertex = stack.Peek();
                    
                    if (!explored.Contains(vertex)) {
                        int count = 0;
                        foreach (int newV in graph[vertex]) {
                            if (!explored.Contains(newV) && !stack.Contains(newV)) {
                                stack.Push(newV);
                                count++;
                            }
                        }

                        if (count == 0) {
                            explored.Add(stack.Pop());
                            allExplored.Add(vertex);
                        }
                    }
                }
                
                groups.Add(explored.Count); 
            }
        }
        
        return groups;
    }

    static long Factorial(long i) {
        if (i <= 1)
            return 1;
        return i * Factorial(i - 1);
    }
    
    static Dictionary<int, HashSet<int>> MakeGraph(long n) {
        Dictionary<int, HashSet<int>> graph = new Dictionary<int, HashSet<int>>();
        for (int i = 0; i < n; i++) {
            graph.Add(i, new HashSet<int>());
        }
        
        return graph;
    }
    
    static void Main(String[] args) {
        // create graph, find number of vertices in each tree, do some factorial math
        string[] input = Console.ReadLine().Split(' ');
        long totalAstros = Int64.Parse(input[0]);
        Dictionary<int, HashSet<int>> astros = MakeGraph(totalAstros);
        long numI = Int32.Parse(input[1]);
        
        for (int i = 0; i < numI; i++) {
            input = Console.ReadLine().Split(' ');
            int first = Int32.Parse(input[0]);
            int second = Int32.Parse(input[1]);
            astros[first].Add(second);
            astros[second].Add(first);
        }
        
        List<long> astroGroups = DFS(astros);
        long totalPairs = totalAstros * (totalAstros - 1) / 2;
        long groupPairs = 0;
        foreach (long astroGroup in astroGroups) {
            groupPairs += astroGroup * (astroGroup - 1) / 2;
        }
        Console.WriteLine(totalPairs - groupPairs);
    }
} 
'''
4
'''