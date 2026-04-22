class Solution {
public:
    bool canJump(vector<int>& nums) {
        int greedy = nums.size() - 1;
        for (int i = nums.size() -2; i >= 0; i--){
            if(nums[i] + i >= greedy){
                greedy = i;
            }
        }
        return greedy == 0;
    }
};
