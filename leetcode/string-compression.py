class Solution {
public:
    int compress(vector<char>& chars) {
        char current = chars[0];
        int count = 1;
        vector<char> result;

        int charSize = chars.size();
        for (int i = 1; i < charSize; i++)
        {
            if (chars[i] == current)
            {
                count++;
            }
            else
            {
                result.push_back(current);              
                if (count > 1)
                {
                    string countStr = std::to_string(count);
                    int countStrLength = countStr.length();
                    for (int j = 0; j < countStrLength; j++)
                    {
                        result.push_back(countStr[j]);
                    }
                }
                current = chars[i];
                count = 1;
            }
        }

        result.push_back(current);              
        if (count > 1)
        {
            string countStr = std::to_string(count);
            int countStrLength = countStr.length();
            for (int j = 0; j < countStrLength; j++)
            {
                result.push_back(countStr[j]);
            }
        }

        chars = result;
        return result.size();
    }
};