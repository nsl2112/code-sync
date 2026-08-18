class Solution {
public:
    vector<bool> kidsWithCandies(vector<int>& candies, int extraCandies) {
        int max = candies[0];
        int size = candies.size();
        for (int i = 1; i < size; i++)
        {
            if (max < candies[i]) max = candies[i];
        }

        vector<bool> result;

        for (int i = 0; i < size; i++)
        {
            if (max - candies[i] <= extraCandies)
            {
                result.push_back(true);
            }
            else
            {
                result.push_back(false);
            }
        }

        return result;
    }
};