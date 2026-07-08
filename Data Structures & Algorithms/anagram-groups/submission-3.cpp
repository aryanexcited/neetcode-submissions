class Solution {
public:
    vector<vector<string>> groupAnagrams(vector<string>& strs) {
        unordered_map<string,vector<string>> hash_s;
        for(string str: strs){
            string sorted = str;
            sort(sorted.begin(), sorted.end());
            hash_s[sorted].push_back(str);
        }
        vector<vector<string>> ans;
        for (auto &it : hash_s) {
            ans.push_back(it.second);
        }

        return ans;
    }
};
