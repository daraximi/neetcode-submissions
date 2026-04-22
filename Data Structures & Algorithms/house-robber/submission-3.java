class Solution {
    private int[] memo;
    private int[] nums;
    
    public int rob(int[] nums) {
        this.nums = nums;
        this.memo = new int[nums.length];

        for(int i = 0; i< memo.length; i++){
            memo[i] = -1;
        }

        return dfs(0);
    }
    private int dfs(int i){
        if(i >= nums.length){
            return 0;
        }
        if (memo[i] != -1){
            return memo[i];
        }
        memo[i] = Math.max(dfs(i+1), nums[i]+ dfs(i+2));
        return memo[i];
    }
}
