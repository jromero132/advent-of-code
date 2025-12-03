/*
Author: Jose A. Romero
Puzzle: Advent of Code (year=2025 ; day=1 ; task=2)
*/

#include <bits/stdc++.h>

#define endl '\n'

using namespace std;

int main() {
    ios_base::sync_with_stdio(0), cin.tie(0), cout.tie(0);

    int ans = 0, dial = 50;
    string line;
    while (getline(cin, line)) {
        int num = stoi(line.substr(1));

        if (line[0] == 'L') {
            ans += abs(dial - num) / 100 + (dial != 0 && dial <= num);
            dial = ((dial - num) % 100 + 100) % 100;  // Ensure the final number is positive
        }
        else {
            ans += (dial + num) / 100;
            dial = (dial + num + 100) % 100;
        }
    }
    cout << ans << endl;
    return 0;
}
