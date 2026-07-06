class Solution {
public:
    bool isAnagram(string s, string t) {
        unordered_map<char, int> hash_s;
        if(s.size()!=t.size()){return false;}
        for(char str: s){
            hash_s[str]++;
        }
        for(char str: t){
            hash_s[str]--;
        }
        for(const auto&[key,item]: hash_s){
            if(item >= 1){
                return false;
            }
        }
        return true;
    }
};
