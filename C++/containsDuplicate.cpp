class Solution {
public:
    bool containsDuplicate(vector<int>& nums) {

        
        // Iterate through the array nums and add to hashmap
        // If count at hashmap is already 1, return false
        // Keep repeating this process

        unordered_set<int> hashmap;

        for (int i: nums){
            if (hashmap.count(i) > 0){
                return true;
            }

            hashmap.insert(i);
        }

        return false;

        
    }
};
