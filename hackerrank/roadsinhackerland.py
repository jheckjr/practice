'''
Problem:
Hacker Rank - Roads in Hackerland
'''

### TODO ###
using System;
using System.Collections.Generic;
using System.IO;
using System.Numerics;
using System.Text;

class Edge : IComparable {
    public int weight;
    public int start;
    public int end;
    
    public Edge(int start, int end, int weight) {
        this.weight = weight;
        this.start = start;
        this.end = end;
    }
    
    public int CompareTo(object obj) {
        if (obj == null) return 1;
        
        Edge otherEdge = obj as Edge;
        return this.weight - otherEdge.weight;
    }
}

class Subset {
    public int parent;
    public int rank;
    
    public Subset(int parent, int rank) {
        this.parent = parent;
        this.rank = rank;
    }
}

class Solution {
    static int V, E;
    static SortedDictionary<int, Edge> edges;
    
    static int Find(Subset[] subsets, int i) {
        if (subsets[i].parent != i)
            subsets[i].parent = Find(subsets, subsets[i].parent);
        
        return subsets[i].parent;
    }
    
    static void Union(Subset[] subsets, int x, int y) {
        if (subsets[x].rank < subsets[y].rank) 
            subsets[x].parent = y;
        else if (subsets[x].rank > subsets[y].rank)
            subsets[y].parent = x;
        else {
            subsets[y].parent = x;
            subsets[x].rank += 1;
        }
    }
    
    static Dictionary<int, List<Edge>> MST() {
        Dictionary<int, List<Edge>> tree = new Dictionary<int, List<Edge>>();
        
        Subset[] subsets = new Subset[V];
        for (int i = 0; i < V; i++) {
            subsets[i] = new Subset(i, 0);
        }
        
        int e = 0;
        foreach (Edge next_edge in edges.Values) {
            int x = Find(subsets, next_edge.start - 1);
            int y = Find(subsets, next_edge.end - 1);
            
            if (x != y) {
                if (tree.ContainsKey(next_edge.start))
                    tree[next_edge.start].Add(next_edge);
                else
                    tree.Add(next_edge.start, new List<Edge> {next_edge});
                if (tree.ContainsKey(next_edge.end))
                    tree[next_edge.end].Add(new Edge(next_edge.end, next_edge.start, next_edge.weight));
                else
                    tree.Add(next_edge.end, new List<Edge> {new Edge(next_edge.end, next_edge.start, next_edge.weight)});
                
                Union(subsets, x, y);
                e++;
            }
            
            if (e == V-1)
                break;
        }
        
        return tree;
    }
    
    static int[] DFS(Dictionary<int, List<Edge>> tree) {
        int[] edgeUse = new int[E]; // num of children using edge
        Stack<int> stack = new Stack<int>();
        stack.Push(1);
        Stack<int> weights = new Stack<int>();
        weights.Push(-1);
        HashSet<int> explored = new HashSet<int>();
        
        while (0 < stack.Count) {
            int vertex = stack.Peek();
            
            if (!explored.Contains(vertex)) {
                int count = 0;
                foreach (Edge e in tree[vertex]) {
                    if (!explored.Contains(e.end) && !stack.Contains(e.end)) {
                        stack.Push(e.end);
                        weights.Push(e.weight);
                        count++;
                    }
                }
                
                if (count == 0) {
                    int last = stack.Pop();
                    explored.Add(last);
                    // find number of children below vertex
                    int children = 1;
                    foreach (Edge e in tree[last]) {
                        if (0 < edgeUse[e.weight])
                            children += edgeUse[e.weight];
                    }
                    // add number of children to edge
                    int w = weights.Pop();
                    if (-1 < w)
                        edgeUse[w] = children;
                }
            }
        }
        
        return edgeUse;
    }
    
    static void Binary(int[] arr) {
        ulong[] binary = new ulong[2*E];
        int index = 0;
        ulong a = 0;
        for (int i = 0; i < 2*E; i++) {
            a = binary[i];
            if (i < arr.Length)
                a += ((ulong)V - (ulong)arr[i]) * (ulong)arr[i];
            else if (a == 0) {
                index = i - 1;
                break;
            }
            
            binary[i+1] = a / 2;
            binary[i] = a % 2;
        }
        
        bool one = false;
        for (int i = index; i > -1; i--) {
            if (!one && binary[i] == 1) 
                one = true;
            if (one)
                Console.Write(binary[i]);
        }
    }
    
    static void Main(String[] args) {
        string[] input = Console.ReadLine().Split(' ');
        V = Int32.Parse(input[0]);
        E = Int32.Parse(input[1]);
        edges = new SortedDictionary<int, Edge>();
        
        for (int i = 0; i < E; i++) {
            input = Console.ReadLine().Split(' ');
            int start = Int32.Parse(input[0]);
            int end = Int32.Parse(input[1]);
            int weight = Int32.Parse(input[2]);
            
            edges.Add(weight, new Edge(start, end, weight));
        }
        
        int[] edgeUse = DFS(MST());

        Binary(edgeUse);
    }
}
'''
1000100
'''