class Solution {
    List<List<Integer>> res;
    public List<List<Integer>> permute(int[] nums) {
        res = new ArrayList<>();
        backtrack(new ArrayList<>(), nums, new boolean[nums.length]);
        return res;
    }
    private void backtrack(List<Integer> perm, int[] nums, boolean[]picked){
        if(perm.size() == nums.length){
            res.add(new ArrayList<>(perm));
            return;
        }
        for(int i = 0; i < nums.length; i++){
            if(!picked[i]){
                perm.add(nums[i]);
                picked[i] = true;
                backtrack(perm, nums, picked);
                perm.remove(perm.size() - 1);
                picked[i] = false;
            }
        }

    }
}
