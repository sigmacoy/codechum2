# Array Equilibrium
"""
Given a 1D array of integers, your task is to find an equilibrium index. An equilibrium index is a position in the array such that the sum of all elements before it is equal to the sum of all elements after it. The element at the equilibrium index itself is not included in either sum.
For an array arr of size n, an index i is an equilibrium point if:
sum(arr[0]...arr[i-1]) == sum(arr[i+1]...arr[n-1])
Special Cases:

For the first element (index 0), the sum of elements before it is considered 0.

For the last element (index n-1), the sum of elements after it is considered 0.

If there are multiple equilibrium indices, you should return the first one (the one with the smallest index). If no such index exists, you must return -1.
Input:
The first line of input contains a single integer N (1 ≤ N ≤ 100), representing the number of elements in the array.
The second line contains N space-separated integers, representing the elements of the array arr (-1000 ≤ arr[i] ≤ 1000).
Output:
A single integer representing the lowest equilibrium index. If no equilibrium index is found, output -1.


"""

def find_equilibrium_index(arr):
    total_sum = sum(arr)
    left_sum = 0
    
    for i in range(len(arr)):
        # right_sum is total_sum minus the left_sum and the current element
        right_sum = total_sum - left_sum - arr[i]
        
        # Check if left sum equals right sum
        if left_sum == right_sum:
            return i
            
        # If not, add the current element to the left_sum before moving to the next index
        left_sum += arr[i]
        
    return -1

n = int(input("Enter array size: "))
arr = list(map(int, input("Enter the elements: ").split()))

result = find_equilibrium_index(arr)
print("Equilibrium index:", result)