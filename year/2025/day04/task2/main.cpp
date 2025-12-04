/*
Author: Jose A. Romero
Puzzle: Advent of Code (year=2025 ; day=4 ; task=2)
*/

#include <bits/stdc++.h>

#define endl '\n'

using namespace std;

int main() {
    ios_base::sync_with_stdio(0), cin.tie(0), cout.tie(0);

    vector<vector<char>> grid;
    string line;
    while (getline(cin, line)) {
        grid.push_back({});
        for (auto c : line) {
            grid.back().push_back(c);
        }
    }

    int n = grid.size(), m = grid[0].size();
    int ans = 0, cur = -1;

    // Performance does not matter for this one since the grid is 136 x 136 :)
    while (cur != 0) {
        cur = 0;
        for (int i = 0 ; i < n ; ++i) {
            for (int j = 0 ; j < m ; ++j) {
                if (grid[i][j] == '@') {
                    int cnt = 0;
                    for (int di = -1 ; di <= 1 ; ++di) {
                        for (int dj = -1 ; dj <= 1 ; ++dj) {
                            cnt += 0 <= i + di && i + di < n && 0 <= j + dj && j + dj < m && grid[i + di][j + dj] == '@';
                        }
                    }
                    if (cnt < 5) {  // It should be less than 5 because when di = dj = 0 then it counts itself :)
                        ++cur;
                        // We can remove it here already, since at the end of this step, it will be removed anyways
                        // and it won't be counted in next step, for the next rolls.
                        // So it really does not matter if we remove it here or in another run after the for loops :)
                        grid[i][j] = '.';
                    }
                }
            }
        }
        ans += cur;
    }
    cout << ans << endl;
    return 0;
}
