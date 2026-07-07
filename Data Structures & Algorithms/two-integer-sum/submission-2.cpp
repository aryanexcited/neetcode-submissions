class Solution {
public:
    vector<int> twoSum(vector<int>& nums, int target) {
        unordered_map<int, int> hash_s;

        for (int i = 0; i < nums.size(); i++) {
            int complement = target - nums[i];

            if (hash_s.find(complement) != hash_s.end()) {
                return {hash_s[complement], i};
            }

            hash_s[nums[i]] = i;
        }

        return {};
    }
};