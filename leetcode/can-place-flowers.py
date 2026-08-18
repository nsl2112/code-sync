class Solution {
public:
    int adject[2] = {-1, 1};
    bool canPlaceFlowers(vector<int>& flowerbed, int n) {
        for (int i = 0; i < flowerbed.size() ; i++)
        {
            if (checkAdject(flowerbed, i))
            {
                flowerbed[i] = 1;
                n--;
            }
        }

        return n <= 0;
    }

    bool checkAdject(vector<int>& flowerbed, int index)
    {
        int bedSize = flowerbed.size();
        if (flowerbed[index] == 1) return false;
        
        for (int i = 0; i < 2; i++)
        {
            int adjectIndex = index + adject[i];
            if ( adjectIndex < 0 || adjectIndex == bedSize)
            {
                continue;
            }

            if (flowerbed[adjectIndex] == 1)
            {
                return false;
            }
        }

        return true;
    }
};