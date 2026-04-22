class Solution {
    public int[] dailyTemperatures(int[] temperatures) {
        int n = temperatures.length;
        int[] res = new int[n];
        Stack<Integer> stack = new Stack<>();

        for (int i = 0;i< n;i++){
            int t = temperatures[i];
            while(!stack.isEmpty() && t>temperatures[stack.peek()]){
                int prev_i = stack.pop();
                res[prev_i] = i-prev_i;
            }
            stack.push(i);
        }
        return res;
    }
}
