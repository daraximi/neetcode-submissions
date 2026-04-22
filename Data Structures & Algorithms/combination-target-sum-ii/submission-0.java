class Solution {
    List<Integer> subset;
    List<List<Integer>> res;
    public List<List<Integer>> combinationSum2(int[] candidates, int target) {
        res = new ArrayList<>();
        subset = new ArrayList<>();
        // Sort array now to avoid duplicates easily. (O log n)
        Arrays.sort(candidates);
        backtrack(0, subset, candidates, target);
        return res;
    }
    private void backtrack(int start, List<Integer> subset, int[] candidates, int target ){
        //base case
        if (target == 0){
            res.add(new ArrayList<>(subset));
            return;
        }
        for (int i = start; i < candidates.length; i++){
            // Skip duplicates
            if(i > start && candidates[i] == candidates[i-1])continue;

            // If numer is too large, no point continuing as array is sorted
            if (candidates[i] > target) break;

            // Select candidate AKA decision 1
            subset.add(candidates[i]);
            // recursively explore more options. but reduce the target by candidate[i]
            backtrack(i+1, subset, candidates, target - candidates[i]);

            //Undo the choice (backtrack) AKA Decision 2
            subset.remove(subset.size() - 1);
        }
    }
}
