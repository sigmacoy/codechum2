// Martian Date? MORE LIKE MARTIAN CALENDAR.
#include <iostream>
using namespace std;

int main() {
    long long s;
    cout << "Enter seconds: " << s;
    long long sec = s % 50; s /= 50;
    long long min = s % 70; s /= 70;
    long long hr  = s % 25; s /= 25;
    long long daysInYear = (6 * 35) + (6 * 28);
    long long year = 1 + (s / daysInYear);
    long long remDays = s % daysInYear;
    int month = 1, day = 1;
    for (int m = 1; m <= 12; m++) {
        long long daysInMonth = (m % 2 != 0) ? 35 : 28;
        if (remDays < daysInMonth) {
            month = m;
            day = remDays + 1;
            break;
        }
        remDays -= daysInMonth;
    }
    cout << "Martian Date: " 
    << to_string(year) << "-" 
    << month << "-" 
    << day << " " 
    << hr << ":" 
    << min << ":" 
    << sec;

    return 0;
}