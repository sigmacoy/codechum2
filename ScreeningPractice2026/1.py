# Smallest Cyclic Shift ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
# All 1-8 is Strictly Python. But on Screening Not Practice. C, C++, C#, Java, Python allowed.
"""
Given a string S, you need to find its lexicographically smallest cyclic shift. A cyclic shift (or rotation) is formed by moving a number of characters from the beginning of the string to the end. For example, if the string is example, its cyclic shifts are example, xamplee, ampleex, mpleexa, and so on.
Lexicographical order is the alphabetical order used in dictionaries. For instance, apple comes before apply.
Input:
A single line containing a string S (1 ≤ length of S ≤ 1000) consisting of lowercase English letters.
Output:
A single line containing the lexicographically smallest cyclic shift of the input string.
"""

str1 = input("Enter string: ")
smallest_shift = min( str1[i:] + str1[:i] for i in range(len(str1)) )
print("Smallest Cyclic Shift:", smallest_shift)