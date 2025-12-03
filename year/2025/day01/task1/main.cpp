/*
Author: Jose A. Romero
Puzzle: Advent of Code (year=2025 ; day=1 ; task=1)
*/

#include <bits/stdc++.h>

#define endl '\n'

using namespace std;

int main() {
    ios_base::sync_with_stdio(0), cin.tie(0), cout.tie(0);

    int ans = 0, dial = 50;
    string line;
    while (getline(cin, line)) {
        dial += (line[0] == 'L' ? -1 : 1) * stoi(line.substr(1));
        dial %= 100;
        ans += dial == 0;
    }
    cout << ans << endl;
    return 0;
}
