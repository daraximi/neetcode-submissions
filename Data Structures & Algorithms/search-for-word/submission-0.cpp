class Solution {
public:
    bool exist(vector<vector<char>>& board, string word) {
        int ROWS = board.size();
        int COLS = board[0].size();
        unordered_set<int> visited;
        
        function<bool(int, int, int)> dfs = [&](int r, int c, int idx) -> bool {
            if (idx == word.size())
                return true;
            if (r < 0 || c < 0 || r >= ROWS || c >= COLS)
                return false;
            if (visited.count(r * COLS + c))
                return false;
            if (board[r][c] != word[idx])
                return false;

            visited.insert(r * COLS + c);

            bool found = dfs(r + 1, c, idx + 1) ||
                         dfs(r - 1, c, idx + 1) ||
                         dfs(r, c + 1, idx + 1) ||
                         dfs(r, c - 1, idx + 1);

            visited.erase(r * COLS + c);  // backtrack
            return found;
        };
        for (int r = 0; r < ROWS; r++)
            for (int c = 0; c < COLS; c++)
                if (dfs(r, c, 0))
                    return true;
        return false;
    }
};
