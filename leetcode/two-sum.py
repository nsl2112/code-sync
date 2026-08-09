class Solution {
public:
    vector<int> twoSum(vector<int>& nums, int target) {
        unordered_map<int, vector<int>> map;
        int numSize = nums.size();
        vector<int> result;
        for  (int i = 0; i < numSize; i++)
        {
            map[nums[i]].push_back(i);
        }

        for (int i = 0; i < numSize - 1; i++)
        {
            int left = target - nums[i];
            if (map.find(left) == map.end()) continue;
            if (left != nums[i])
            {
                result = {i, map[left][0]};
                return result;
            }
            else
            {
                for (int j = 0; j < map[left].size(); j++)
                {
                    if (map[left][j] != i)
                    {
                        result = {i, map[left][j]};
                        return result;               
                    }
                }
            }

        }

        return result;
    }
};