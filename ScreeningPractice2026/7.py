# Subarray Bitwise Evolution
"""
You are a researcher observing the evolution of a sequence of numbers. You have an array A of N integers. This array undergoes a series of M transformations. Each transformation is applied to a specific contiguous subsegment of the array, defined by a start index L and an end index R.
The transformations are of three types, denoted by a character: 'A' (Augment), 'S' (Shift), and 'X' (XOR-Neighbor). These operations are applied sequentially in the given order. The array is modified by each operation, and subsequent operations work on the modified array.
The transformation rules are as follows:

Type 'A' (Augment): For each element x in the subarray from index L to R (inclusive):

If x is positive (x > 0), it is replaced by x * popcount(|x|).

If x is negative (x < 0), it is replaced by x + popcount(|x|).

If x is zero (x = 0), it is replaced by 1.

The function popcount(n) returns the number of set bits (1s) in the 64-bit binary representation of a non-negative number n. For example, popcount(13) is 3 because 13 in binary is ...001101.

Type 'S' (Shift): For each element x at index i in the subarray from L to R (inclusive):

Let k = (i % 5) + 1.

The element x is replaced by the result of a 64-bit circular left shift by k positions. A circular left shift operation moves the most significant k bits to the least significant bit positions.

Type 'X' (XOR-Neighbor): This transformation updates elements based on the values of their neighbors at the start of this operation. To do this, imagine a temporary copy B of the array A is made before any changes for this 'X' operation occur.

For each index i from L to R (inclusive):

If L < i < R, the new value is A[i] = B[i] XOR (B[i-1] + B[i+1]).

If i == L and L < R (a multi-element range), the new value is A[L] = B[L] XOR B[R].

If i == R and L < R (a multi-element range), the new value is A[R] = B[R] XOR B[L].

If L == R (a single-element range), the value of A[L] does not change.

Your task is to determine the final state of the array after all M operations have been performed.
Note: The values in the array can become very large. Use a 64-bit integer type (like long long in C) to store them and perform calculations to avoid overflow.

Input:
The first line of input contains an integer N (1 ≤ N ≤ 100), representing the size of the array.
The second line contains N space-separated integers, which are the initial elements of the array A (-1,000,000,000 ≤ A[i] ≤ 1,000,000,000).
The third line contains an integer M (1 ≤ M ≤ 100), which is the number of operations to follow.
Each of the next M lines describes an operation. An operation is given by a character op and two integers L and R (op ∈ {'A', 'S', 'X'}, 0 ≤ L ≤ R < N), separated by spaces.

Output:
Print a single line containing N space-separated integers, representing the final state of the array. Each number should be followed by a space.
"""


def popcount(n):
    return bin(n).count('1')

def circular_shift_left(val, k):
    # Ensure val is treated as a 64-bit unsigned integer
    val = val & 0xFFFFFFFFFFFFFFFF
    k = k % 64
    
    if k == 0:
        shifted = val
    else:
        # Perform circular left shift
        shifted = ((val << k) | (val >> (64 - k))) & 0xFFFFFFFFFFFFFFFF
    
    # Convert back to signed 64-bit integer
    if shifted >= (1 << 63):
        shifted -= (1 << 64)
    return shifted

# --- Input Handling ---
N = int(input("Enter array size: "))
A = list(map(int, input("Enter array elements: ").split()))
M = int(input("Enter number of operations: "))

# --- Process Operations ---
for _ in range(M):
    # Read the operation as a single string, then split it into parts
    op_line = input("Enter operation: ").split()
    op = op_line[0]
    L = int(op_line[1])
    R = int(op_line[2])
    
    if op == 'A':
        for i in range(L, R + 1):
            x = A[i]
            if x > 0:
                A[i] = x * popcount(x)
            elif x < 0:
                A[i] = x + popcount(abs(x))
            else:
                A[i] = 1
                
    elif op == 'S':
        for i in range(L, R + 1):
            k = (i % 5) + 1
            A[i] = circular_shift_left(A[i], k)
            
    elif op == 'X':
        # Temporary copy for simultaneous evaluation
        B = A.copy()
        for i in range(L, R + 1):
            if L == R:
                continue # Single element, no change
            elif i == L:
                A[L] = B[L] ^ B[R]
            elif i == R:
                A[R] = B[R] ^ B[L]
            else:
                A[i] = B[i] ^ (B[i-1] + B[i+1])

print("Final array:", " ".join(map(str, A)))