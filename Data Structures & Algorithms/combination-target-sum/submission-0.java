class Solution {
    List<List<Integer>> res;
    List<Integer> current;
    public List<List<Integer>> combinationSum(int[] nums, int target) {
        res = new ArrayList<>();
        current = new ArrayList<>();

        backtrack(0,current, nums, target);

        return (res);
    }
    private void backtrack(int i,List<Integer> current ,int[] nums, int target){
        if (i >= nums.length) {
            return;
        }
        int curr = 0;
        for (int num:current){
            curr += num;
        }
        if (curr > target){
            return;
        }
        if (curr == target){
            res.add(new ArrayList<>(current));
            return;
        }
        //Decision 1 - add itself
        current.add(nums[i]);
        backtrack(i, current, nums, target);
        // Decision 2 - add next number
        current.remove(current.size() -1);
        backtrack(i+1, current, nums, target);
    }
}
