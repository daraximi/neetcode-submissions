class Solution {
    public int[] twoSum(int[] numbers, int target) {
        int l = 0, r = numbers.length - 1; // ✅ use '-' not '()'

        while (l < r) {
            int sum = numbers[l] + numbers[r];

            if (sum > target) {
                r--; // ✅ close the if properly
            } else if (sum < target) {
                l++;
            } else {
                // ✅ correct array creation syntax
                return new int[] {l + 1, r + 1}; // problem usually expects 1-based indices
            }
        }
        return new int[0];
    }
}
