class Solution {
    public int maxArea(int[] heights) {
        int res = 0;
        // Testing brute force solution (n^2)
        for (int i = 0; i< heights.length; i++){
            for (int j= heights.length-1; j>0; j--){
                int water = Math.min(heights[i],heights[j]) * Math.abs(i-j);
                res = Math.max(res, water);
            }
        }
        return res;
    }
}
