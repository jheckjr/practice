'''
Problem:
Hacker Rank - Snakes and Ladders
'''

### TODO ###
using System;
using System.Collections.Generic;
using System.IO;
class Solution {
    static Dictionary<int, List<int>> MakeBoard() {
        Dictionary<int, List<int>> board = new Dictionary<int, List<int>>();
        for (int i = 1; i < 100; i++) {
            board.Add(i, new List<int>());
            
            for (int j = i + 6; j > i; j--) {
                board[i].Add(j);
            }
        }
        
        return board;
    }
    
    static Dictionary<int, List<int>> AddLadder(Dictionary<int, List<int>> board, int start, int end) {
        for (int i = start - 1; i >= start - 6; i--) {
            if (0 < i) {
                board[i][6 - (start - i)] = end;
            }
        }
        
        return board;
    }
    
    static Dictionary<int, List<int>> AddSnake(Dictionary<int, List<int>> board, int start, int end) {
        for (int i = start - 1; i >= start - 6; i--) {
            board[i][6 - (start - i)] = end;
        }
        
        return board;
    }
    
    static void BFS(Dictionary<int, List<int>> board) {
        Queue<int> queue = new Queue<int>();
        queue.Enqueue(1);
        Queue<int> distances = new Queue<int>();
        distances.Enqueue(0);
        HashSet<int> explored = new HashSet<int>();
        
        while (0 < queue.Count) {
            int vertex = queue.Dequeue();
            int dist = distances.Dequeue();
            
            if (vertex == 100) {
                Console.WriteLine(dist);
                return;
            } else if (100 < vertex)
                continue;
            
            if (!explored.Contains(vertex)) {
                foreach(int newV in board[vertex]) {
                    if (!explored.Contains(newV) && !queue.Contains(newV)) {
                        queue.Enqueue(newV);
                        distances.Enqueue(dist + 1);
                    }
                }
                explored.Add(vertex);
            }
        }
        
        Console.WriteLine(-1);
    }
    
    static void Main(String[] args) {
        /* Enter your code here. Read input from STDIN. Print output to STDOUT. Your class should be named Solution */
        int T = Int32.Parse(Console.ReadLine());
        for (int t = 0; t < T; t++) {
            Dictionary<int, List<int>> board = MakeBoard();
            
            int N = Int32.Parse(Console.ReadLine());
            for (int n = 0; n < N; n++) {
                String[] ladder = Console.ReadLine().Split(' ');
                board = AddLadder(board, Int32.Parse(ladder[0]), Int32.Parse(ladder[1]));
            }
            
            int M = Int32.Parse(Console.ReadLine());
            for (int m = 0; m < M; m++) {
                String[] snake = Console.ReadLine().Split(' ');
                board = AddSnake(board, Int32.Parse(snake[0]), Int32.Parse(snake[1]));
            }
            
            BFS(board);
        }
    }
}  
'''
3
5
'''