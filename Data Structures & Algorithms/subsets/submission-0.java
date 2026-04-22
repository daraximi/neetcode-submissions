class Solution {
    List<List<Integer>> res;
    List<Integer> subset;
    int limit;
    public List<List<Integer>> subsets(int[] nums) {
        res = new ArrayList<>();
        subset = new ArrayList();
        limit = nums.length;
        backtrack(0,nums);
        return res;
    }
    private void backtrack(int i, int[] nums){
        if(i >= limit){
            res.add(new ArrayList<>(subset));
            return;
        }
        // Decision 1
        subset.add(nums[i]);
        backtrack(i+1, nums);
        // Decision 2
        subset.remove(subset.size() -1);
        backtrack(i+1, nums);
    }

}
