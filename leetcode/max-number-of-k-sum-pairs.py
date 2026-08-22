class Solution {
public:
    int maxOperations(vector<int>& nums, int k) {
        sort(nums.begin(), nums.end());
        int left = 0;
        int right = nums.size() - 1;
        int result = 0;
        int sum = 0;
        
        while (left < right)
        {
            sum = nums[left] + nums[right];
            if (sum == k)
            {
                result++;
                left++;
                right--;
            } 
            else if (sum < k ) left++;
            else right--;
        }

        return result;
    }
};