// Naay LC Problem: 1043. Partition Array for Maximum Sum
// LINK: https://leetcode.com/problems/partition-array-for-maximum-sum/
// I skipped this, idk know how to answer.

#include <bits/stdc++.h>
using namespace std;

int main(){
    cout << "Enter size of array: ";
    int N;
    cin >> N;
    cout << "Enter array:\n";
    vector<int> A(N);
    for(int i = 0; i < N; i++){
        cin >> A[i];
    }
    cout << "Enter k: ";
    int K;
    cin >> K;

    // dp[i][j] = minimum cost to partition the first i elements into j subarrays
    // Use long long because the sum can exceed 32-bit int (e.g., 500 * 1,000,000,000)
    vector<vector<long long>> dp(N + 1, vector<long long>(K + 1, LLONG_MAX));
    
    // Base case: cost to partition 0 elements into 0 subarrays is 0
    dp[0][0] = 0;

    // Fill the DP table
    for (int j = 1; j <= K; j++) { // j = number of subarrays
        for (int i = j; i <= N; i++) { // i = number of elements considered
            long long current_max = 0;
            for (int p = i; p >= j; p--) {
                current_max = max(current_max, (long long) A[p - 1]);
                if (dp[p - 1][j - 1] != LLONG_MAX) {
                    dp[i][j] = min(dp[i][j], dp[p - 1][j - 1] + current_max);
                }
            }
        }
    }

    // The answer is the minimum cost to partition all N elements into K subarrays
    cout << dp[N][K] << endl;

    return 0;
}

// My answer to LC:
class Solution {
public:
    int maxSumAfterPartitioning(vector<int>& arr, int k) {
        int n = arr.size();
        vector<int> dp(n + 1, 0);
        for (int i = 1; i <= n; i++) {
            int curMax = 0;
            for (int len = 1; len <= k && i - len >= 0; len++) {
                curMax = max(curMax, arr[i - len]);
                dp[i] = max(dp[i], dp[i - len] + len * curMax);
            }
        }
        return dp[n];
    }
};