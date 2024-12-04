#https://www.codechef.com/START163D/problems/BINARYSUM
t = int(input())
for _ in range(t):
    N, K = map(int, input().split())
    
    max_possible_ones = (N + 1) // 2
    if K > max_possible_ones:
        print("NO")
    else:
        print("YES")
