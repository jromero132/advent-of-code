/*
Author: Jose A. Romero
Puzzle: Advent of Code (year=2025 ; day=2 ; task=1)
*/

#include <bits/stdc++.h>

#define ll long long
#define endl '\n'

using namespace std;

int main() {
    ios_base::sync_with_stdio(0), cin.tie(0), cout.tie(0);

    vector<ll> invalid_ids;
    for (int i = 0 ; i < 1e6 ; ++i) {
        invalid_ids.push_back(stoll(to_string(i) + to_string(i)));
    }
    vector<ll> pref_sum = {0};
    for (auto x : invalid_ids) {
        pref_sum.push_back(pref_sum.back() + x);
    }

    string line;
    getline(cin, line);
    stringstream ss(line);

    ll l, r;
    char dash;
    ll ans = 0;
    while (ss >> l >> dash >> r) {
        int pos_l = lower_bound(invalid_ids.begin(), invalid_ids.end(), l) - invalid_ids.begin();
        int pos_r = lower_bound(invalid_ids.begin(), invalid_ids.end(), r + 1) - invalid_ids.begin();
        ans += pref_sum[pos_r] - pref_sum[pos_l];
        ss.ignore();  // Skip comma (or EOF)
    }
    cout << ans << endl;
    return 0;
}
