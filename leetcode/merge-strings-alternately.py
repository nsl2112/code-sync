class Solution {
public:
    string mergeAlternately(string word1, string word2) 
    {
        int i = 0;
        int word1Length = word1.length();
        int word2Length = word2.length();
        int maxBound = max(word1Length, word2Length);
        string result = "";
        
        while (i < maxBound)
        {
            if (i < word1Length) result += word1[i];
            if (i < word2Length) result += word2[i];
            i++;  
            
        }  

        return result;  
    }
};