/*
Author: Jose A. Romero
Puzzle: Advent of Code (year=2025 ; day=3 ; task=1)
*/

#include <bits/stdc++.h>

#define endl '\n'

using namespace std;

int main() {
    ios_base::sync_with_stdio(0), cin.tie(0), cout.tie(0);

    int ans = 0;
    string line;
    while (getline(cin, line)) {
        auto digit1 = max_element(line.begin(), line.end() - 1);
        auto digit2 = max_element(digit1 + 1, line.end());
        ans += 10 * (*digit1 - '0') + (*digit2 - '0');
    }
    cout << ans << endl;
    return 0;
}
