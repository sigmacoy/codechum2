# K-Palindrome Check
"""
Given a string S and an integer K, determine if the string can be
transformed into a palindrome by changing at most K
characters. A palindrome is a word, phrase, or sequence that
reads the same backward as forward (e.g., madam, radar).

Consider the string "apple" and K= 2.

To check whether it can become a palindrome:
• Compare characters from the ends moving inward:
'a' vs 'e' → mismatch (1)
'p' vs 'l' → mismatch (2)
• The middle character 'p' has no pair → no issue
So, we have 2 mismatches. This means we need to change at
least 2 characters to make the string a palindrome.
• If K >= 2 → YES
•IfK < 2 → NO

Input:
The first line of input is a single stringS, consisting of
lowercase English letters (a-z). The length of S will be between
1 and 1000, inclusive.
The second line of input is a single integer (0 ≤ K ≤ 1000).

Output:
Output YES if the string S can be made a palindrome by
changing at most K characters. Otherwise, output NO.
"""
def can_make_palindrome(s, k):
    left = 0
    right = len(s) - 1
    mismatches = 0
    
    # Move pointers towards the center
    while left < right:
        # If the characters don't match, we must change one of them
        if s[left] != s[right]:
            mismatches += 1
            
            # Optimization: If we already exceeded K, we can stop early
            if mismatches > k:
                return "NO"
                
        left += 1
        right -= 1
        
    # If we finish the loop and mismatches <= k, it's possible
    return "YES"

s = input("Enter string: ")
k = int(input("Enter K: "))

result = can_make_palindrome(s, k)
print("Result:", result)