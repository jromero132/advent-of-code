/*
Author: Jose A. Romero
Puzzle: Advent of Code (year=2025 ; day=2 ; task=2)
*/

#include <bits/stdc++.h>

#define ll long long
#define endl '\n'

using namespace std;

int main() {
    ios_base::sync_with_stdio(0), cin.tie(0), cout.tie(0);

    set<ll> invalid_ids_set;
    for (int i = 0 ; i < 1e6 ; ++i) {
        string s = to_string(i), ss = s;

        for (int r = 10 / s.length() ; r >= 2 ; --r) {  // Number of repetitions, from 2 to 10 / s.length()
            ss += s;
            invalid_ids_set.insert(stoll(ss));
        }
    }
    vector<ll> invalid_ids(invalid_ids_set.begin(), invalid_ids_set.end());
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
