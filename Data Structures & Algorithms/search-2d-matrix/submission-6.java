class Solution {
    public boolean searchMatrix(int[][] matrix, int target) {
        int ROWS = matrix.length;
        int COLS = matrix[0].length;

        // System.out.println(ROWS);
        // System.out.println(COLS);
        for (int i = 0; i<ROWS; i++){
            // CHECk the start and end of each row
            int start = i;
            int end = COLS - 1;
            // System.out.println(start);
            // System.out.println(end);

            if ((matrix[i][0]<= target) && (target <= matrix[i][end])){

                System.out.println(matrix[i][0]);
                System.out.println(matrix[i][end]);

                //Perform binary search here until true
                int l = 0;
                int r = end;
                while (l<=r){
                    int mid = (l + r)/2;
                    if(matrix[i][mid] == target){
                        return true;
                    }
                    else if(matrix[i][mid] > target){
                        r = mid - 1;
                    }
                    else{
                        l = mid + 1;
                    }
                }
            } 
        }
        return false;
    }
}
