class Solution {
public:
    void moveZeroes(vector<int>& nums) 
    {
        int left = 0;
        int right = 1;
        int numSize = nums.size();
        int temp;
        while (right < numSize)
        {
            if (nums[left] == 0)
            {
                if (nums[right] == 0)
                {
                    right++;
                    continue;
                }
                else
                {
                    temp = nums[left];
                    nums[left] = nums[right];
                    nums[right] = temp;
                }
            }
            else
            {
                left++;
                right++;
            }
        }
    }
};