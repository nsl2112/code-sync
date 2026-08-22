class Solution {
public:
    bool isSubsequence(string s, string t) {
        int sP = 0;
        int tSize = t.length();
        for (int i = 0; i < tSize; i++)
        {
            if (t[i] == s[sP])
            {
                sP++;
            }
        }

        return sP == s.length();
    }
};