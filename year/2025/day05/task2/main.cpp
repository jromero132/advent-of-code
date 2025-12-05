/*
Author: Jose A. Romero
Puzzle: Advent of Code (year=2025 ; day=5 ; task=2)
*/

#include <bits/stdc++.h>

#define ll long long
#define endl '\n'

using namespace std;

int main() {
    ios_base::sync_with_stdio(0), cin.tie(0), cout.tie(0);

    vector<pair<ll, ll>> inp_ranges;
    vector<ll> ids;

    bool read_ranges = true;
    for (string line ; getline(cin, line) ; ) {
        if (line.empty()) {
            read_ranges = false;
            continue;
        }
        if (read_ranges) {
            ll l, r;
            sscanf(line.c_str(), "%lld-%lld", &l, &r);
            inp_ranges.push_back({l, r});
        }
        else {
            ids.push_back(stoll(line));
        }
    }

    sort(inp_ranges.begin(), inp_ranges.end());
    vector<pair<ll, ll>> ranges = {inp_ranges[0]};
    for (int i = 1 ; i < inp_ranges.size() ; ++i) {
        if (inp_ranges[i].first <= ranges.back().second) {
            ranges.back().second = max(ranges.back().second, inp_ranges[i].second);
        }
        else {
            ranges.push_back(inp_ranges[i]);
        }
    }

    sort(ids.begin(), ids.end());

    ll ans = 0;
    for (auto range : ranges) {
        ans += range.second - range.first + 1;
    }
    cout << ans << endl;
    return 0;
}
