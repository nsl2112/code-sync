class Solution {
public:
    string gcdOfStrings(string str1, string str2) 
    {
        int length1 = str1.length();
        int length2 = str2.length();
        int shorter = length1 >= length2 ? length2 : length1;
        for (int i = shorter; i >= 1; i--)
        {
            if (length1 % i == 0 && length2 % i == 0)
            {
                string prefix1 = str1.substr(0, i);
                string subfix1 = str1.substr(length1 - i);
                string prefix2 = str2.substr(0, i);
                string subfix2 = str2.substr(length2 - i);

                if (prefix1 == subfix1 && subfix1 == prefix2 && prefix2 == subfix2)
                {
                    if (checkConcate(str1, prefix1) && checkConcate(str2, prefix1))
                    {
                        return prefix1;
                    }
                }
            }
        }

        return "";  
    }

    bool checkConcate(string str1, string sub)
    {
        int subLength = sub.length();
        for (int i = 0;  i < str1.length(); i+=subLength)
        {
            if (str1.substr(i, subLength) != sub)
            {
                return false;
            }
        }
        return true;
    }
};