class Solution {
public:
    string reverseVowels(string s) {
        int low = 0;
        int high = s.length() - 1;
        while (low < high)
        {
            if (isVowel(s[low]) && isVowel(s[high]))
            {
                char temp = s[low];
                s[low] = s[high];
                s[high] = temp;
                low++;
                high--;
            }
            
            if (isVowel(s[low]) == false)
            {
                low++;
            }
            
            if (isVowel(s[high]) == false)
            {
                high--;
            }
        }
       
        return s;
    }

    bool isVowel(char c)
    {
        if (c == 'a' || c == 'e' || c == 'i' || c == 'o' || c == 'u'||
            c == 'A' || c == 'E' || c == 'I' || c == 'O' || c == 'U')
        {
            return true;
        }

        return false;
    }
};