class Solution {
public:
    vector<int> productExceptSelf(vector<int>& nums)
     {
        int numSize = nums.size();
        vector<int> prefixPro = vector<int>(numSize, 1);
        vector<int> sufixPro = vector<int>(numSize, 1);
        vector<int> result;

        prefixPro[0] = nums[0]; 
        sufixPro[numSize - 1] = nums[numSize -1];

        for (int i = 1; i < numSize; i++)
        {
            prefixPro[i] = prefixPro[i - 1] * nums[i];
            sufixPro[numSize - 1 - i] = sufixPro[numSize - i] * nums[numSize - 1 - i];
        }

        for (int i = 0; i < numSize; i++)
        {
            if (i == 0) result.push_back(sufixPro[i + 1]);
            else if (i == numSize - 1) result.push_back(prefixPro[i - 1]);
            else result.push_back(prefixPro[i - 1] * sufixPro[i + 1]);      
        }
        return result;
    }
};