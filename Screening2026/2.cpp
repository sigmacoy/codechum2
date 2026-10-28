// left right middle avg

#include <bits/stdc++.h>
using namespace std;

bool isPrime(int n) {
    if (n <= 1) return false;
    for (int i = 2; i < n; i++) {
        if (n % i == 0) return false;
    }
    return true;
}

int main() {
    int N, K;
    cout << "Enter size of the array:";
    cin >> N;
    cout << "Enter cycle pass something:";
    cin >> K;
    vector<int> A(N);
    for (int i = 0; i < N; i++) {
        cin >> A[i];
    }
    for (int pass = 0; pass < K; pass++) {
        vector<int> temp = A; 
        for (int i = 0; i < N; i++) {
            int left = A[(i - 1 + N) % N];
            int right = A[(i + 1) % N];
            int current = A[i];
            int avg = (left + current + right) / 3;
            if (!isPrime(avg)) {
                temp[i] = avg;
            }
        }
        A = temp;
    }
    for (int i = 0; i < N; i++) {
        cout << A[i] << " ";
    }
    return 0;
}