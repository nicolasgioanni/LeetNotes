// C++
class Solution {
public:
    int maxArea(vector<int>& heights) {
        int result = 0;
        int l = 0;
        int r = static_cast<int>(heights.size()) - 1;

        while (l < r) {
            int area = min(heights[l], heights[r]) * (r - l);
            result = max(result, area);

            if (heights[l] > heights[r]) {
                r--;
            } else {
                l++;
            }
        }
        return result;
    }
};
