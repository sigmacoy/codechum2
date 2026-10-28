# Segmented Pattern Compressor ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
"""
Write a program that compresses a sequence of numbers by identifying and summarizing contiguous segments that follow a consistent arithmetic trend.
A segment is defined as a sequence of at least two numbers where all adjacent pairs exhibit the same trend: either strictly increasing, strictly decreasing, or constant.
The program should iterate through the array and identify the longest possible segment starting from the current position. Once a segment is identified, it is compressed into a special string format. Any number that does not belong to a segment of length 2 or more is considered 'noise' and is output as-is. The process repeats starting from the element immediately following the identified segment.

Compression Rules:

An increasing segment (e.g., 1 4 9) is compressed to (start_value,end_value). Example: (1,9).

A decreasing segment (e.g., 8 5 2) is compressed to (start_value,end_value). Example: (8,2).

A constant segment (e.g., 7 7 7 7) is compressed to (valuexcount). Example: (7x4).

Individual numbers not part of any segment are printed as they are.

Example:
For an input sequence 1 2 4 4 4 2 1 9, the output should be (1,2) (4x3) (2,1) 9.
Explanation:

1 2 is an increasing segment of length 2. The next number, 4, breaks the trend. This segment is compressed to (1,2).

The next search begins at 4. The sequence 4 4 4 is a constant segment. This is compressed to (4x3).

The next search begins at 2. The sequence 2 1 is a decreasing segment. This is compressed to (2,1).

The next search begins at 9. It is the last number and cannot form a segment of length 2, so it is treated as noise and printed as 9.

Input:
The first line contains an integer N (1 ≤ N ≤ 100), the number
of elements in the sequence.
The second line contains N space-separated integers, where
each integer is between -1,000,000,000 and 1,000,000,000.
Output:
A single line containing the space-separated compressed
representation of the sequence.
"""

def compress_sequence(arr):
    result = []
    n = len(arr)
    i = 0
    
    while i < n:
        # If we are at the last element, it can't form a segment of length 2
        if i == n - 1:
            result.append(str(arr[i]))
            break
            
        # Determine the direction/trend of the first two elements
        # 1 for increasing, -1 for decreasing, 0 for constant
        if arr[i+1] > arr[i]:
            trend = 1
        elif arr[i+1] < arr[i]:
            trend = -1
        else:
            trend = 0
            
        # Find the longest contiguous segment that follows this trend
        j = i + 1
        while j < n - 1:
            next_diff = arr[j+1] - arr[j]
            
            # Check if the next pair matches the current trend
            if (trend == 1 and next_diff > 0) or \
               (trend == -1 and next_diff < 0) or \
               (trend == 0 and next_diff == 0):
                j += 1
            else:
                break
                
        segment_length = j - i + 1
        
        # If the segment is at least 2 elements long, compress it
        if segment_length >= 2:
            start_val = arr[i]
            end_val = arr[j]
            
            if trend == 0:
                # Constant segment: (value x count)
                result.append(f"({start_val}x{segment_length})")
            else:
                # Increasing or Decreasing segment: (start, end)
                result.append(f"({start_val},{end_val})")
                
            # Move the index past the processed segment
            i = j + 1
        else:
            # No valid segment, treat as noise and print as-is
            result.append(str(arr[i]))
            i += 1
            
    return " ".join(result)

n = int(input("Enter array size: "))
numbers = list(map(int, input("Enter the numbers: ").split()))

compressed = compress_sequence(numbers)
print("Compressed Result:", compressed)
