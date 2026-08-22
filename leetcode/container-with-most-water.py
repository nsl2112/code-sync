class Solution {
public:
    int maxArea(vector<int>& height) {
        int left = 0;
        int right = height.size() - 1;
        int result = 0;
        int current = 0;
        while (left < right)
        {
            current = (right - left) * min(height[left], height[right]);
            result = max(result, current);
            if (height[left] > height[right]) right--;
            else left++;
        }

        return result;
    }
};