class Solution {
    public int maxArea(int[] heights) {
        int res = 0;
        // Testing brute force solution (n^2)
        int l = 0, r = heights.length-1;
        while (l < r){
            int water = Math.min(heights[l], heights[r]) * (r-l);
            res = Math.max(water, res);
            if(heights[l]<=heights[r]){
                l++;
            }
            else{
                r--;
            }
        }
        return res;
    }
}
