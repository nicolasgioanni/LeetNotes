// C++
class Solution {
public:
    vector<vector<int>> threeSum(vector<int>& nums) {
        sort(nums.begin(), nums.end());
        vector<vector<int>> result;
        int target = 0;

        for (int i = 0; i < nums.size(); i++) {
            if (i > 0 && nums[i] == nums[i - 1]) continue;

            if (nums[i] > target) break;

            int l = i + 1;
            int r = nums.size() - 1;

            while (l < r) {
                int threeSum = nums[i] + nums[l] + nums[r];

                if (threeSum > target) {
                    r--;
                } else if (threeSum < target) {
                    l++;
                } else {
                    result.push_back({nums[i], nums[l], nums[r]});
                    
                    l++;
                    r--;
                    while (l < r && nums[l] == nums[l - 1]) l++;
                    while (l < r && nums[r] == nums[r + 1]) r--;
                }
            }
        }
        return result;
    }
};
