# Binary-Sum

Binary Sum Problem

You are given two integers N and K. Your task is to determine whether there exists a binary string S of length N such that:

1. The sum of all the digits of S equals K, i.e., 
   S_1 + S_2 + S_3 + ... + S_N = K
2. No two adjacent digits in S are equal, i.e., 
   S_i ≠ S_(i+1) for every 1 ≤ i < N

If such a binary string exists, output "YES". Otherwise, output "NO".

Input Format

- The first line of input contains a single integer T — the number of test cases.
- The next T lines each contain two space-separated integers N and K.

Output Format

For each test case, output a single line containing either "YES" or "NO" (case-insensitive).

Constraints

- 1 ≤ T ≤ 100
- 1 ≤ N ≤ 100
- 0 ≤ K ≤ 100

Example Input

5
5 2
7 5
9 5
12 7
82 41

Example Output

YES
NO
YES
NO
YES

Explanation

1. Test Case 1:  
   S = 01010 is valid. The sum of digits is 0 + 1 + 0 + 1 + 0 = 2, and no two adjacent digits are equal.

2. Test Case 2:  
   It is impossible to construct a valid binary string with N = 7 and K = 5.

3. Test Case 3:  
   S = 101010101 is valid. The sum of digits is 1 + 0 + 1 + 0 + 1 + 0 + 1 + 0 + 1 = 5.

4. Test Case 4:  
   It is impossible to construct a valid binary string with N = 12 and K = 7.

5. Test Case 5:  
   S = 101010... (alternating 1s and 0s for 82 digits) is valid. The sum of digits equals 41.

