class Solution {
public:
    string reverseWords(string s) {
        
        string result;
        
        int start, end;
        start = s.length() - 1;
        end = start;

        while (start >= 0)
        {
            while (s[start] != ' ')
            {
                start--;
                if (start == -1) break;
            }
            
            if (start != end)
            {
                result += s.substr(start + 1, end - start) + ' ';
            }

            start--;
            end = start;
        }

        return result.substr(0, result.length() - 1);
    }
};