/*
Author: Jose A. Romero
Puzzle: Advent of Code (year=2025 ; day=3 ; task=2)
*/

#include <bits/stdc++.h>

#define ll long long
#define endl '\n'

using namespace std;

int main() {
    ios_base::sync_with_stdio(0), cin.tie(0), cout.tie(0);

    const int N_TURNS = 12;
    ll ans = 0;
    string line;
    while (getline(cin, line)) {
        vector<string::iterator> digits;
        auto it = line.begin();
        for (int i = N_TURNS - 1 ; i >= 0 ; --i) {
            digits.push_back(max_element(it, line.end() - i));
            it = digits.back() + 1;
        }
        string num;
        for (auto iter : digits) {
            num += *iter;
        }
        ans += stoll(num);
    }
    cout << ans << endl;
    return 0;
}
