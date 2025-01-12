/*
Author: Jose A. Romero
Puzzle: Advent of Code (year=2024 ; day=2 ; task=2)
*/

#include <bits/stdc++.h>

#define endl '\n'

using namespace std;

bool is_safe_report(vector<int> &nums, int pos)
{
    int last = pos == 0;
    bool cond1 = true, cond2 = true;
    for (int i = last + 1; i < nums.size(); ++i) {
        if (pos == i)
            continue;

        cond1 &= 1 <= nums[i] - nums[last] && nums[i] - nums[last] <= 3;
        cond2 &= -3 <= nums[i] - nums[last] && nums[i] - nums[last] <= -1;
        last = i;
    }
    return cond1 || cond2;
}

int main()
{
    ios_base::sync_with_stdio(0), cin.tie(0), cout.tie(0);
    string line;
    int ans = 0;
    while (getline(cin, line)) {
        istringstream s(line);
        vector<int> nums;
        int num;
        while (s >> num) {
            nums.push_back(num);
        }
        for (int i = 0; i < nums.size(); ++i) {
            if (is_safe_report(nums, i)) {
                ++ans;
                break;
            }
        }
    }
    cout << ans << endl;
    return 0;
}
