// operator, isalpha, isdigit
#include <bits/stdc++.h>
using namespace std;

int main() {
    string inputLine;
    getline(cin, inputLine);
    int pos = inputLine.find(": ");
    if (pos != string::npos) {
        inputLine = inputLine.substr(pos + 2);
    }
    vector<int> numbers;
    stringstream ss(inputLine);
    string token;
    while (getline(ss, token, ',')) {
        if (!token.empty()) {
            numbers.push_back(stoi(token));
        }
    }
    string finalOutput = "";
    for (int i = 0; i < numbers.size(); i++) {
        int num = numbers[i];
        char c = static_cast<char>(num);
        string formattedValue = "";
        if (c == '+' || c == '-' || c == '*' || c == '/') {
            formattedValue = string(1, c);
        } 
        else if (isdigit(c)) {
            formattedValue = to_string(num) + ".000";
        }
        else if (isalpha(c)) {
            string hexStr = "";
            int tempNum = num;
            if (tempNum == 0) hexStr = "0";
            
            while (tempNum > 0) {
                int rem = tempNum % 16;
                if (rem < 10) {
                    hexStr = char('0' + rem) + hexStr;
                } else {
                    hexStr = char('A' + (rem - 10)) + hexStr;
                }
                tempNum /= 16;
            }
            formattedValue = hexStr;
        }
        if (!formattedValue.empty()) {
            if (!finalOutput.empty()) {
                finalOutput += " ";
            }
            finalOutput += formattedValue;
        }
    }
    cout << finalOutput << endl;
    return 0;
}