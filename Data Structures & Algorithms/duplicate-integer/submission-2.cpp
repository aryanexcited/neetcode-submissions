class Solution {
public:
    bool hasDuplicate(vector<int>& nums) {
        unordered_map<int, int> hash_n;
        int n = nums.size();
        for(int i = 0; i < n; i++){
            hash_n[nums[i]]++;
        }
        for(const auto&[key, item]: hash_n){
            if(item>1){
                return true;
            }
        }
        return false;
    }
};