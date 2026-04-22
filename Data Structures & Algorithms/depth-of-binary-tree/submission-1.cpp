/**
 * Definition for a binary tree node.
 * struct TreeNode {
 *     int val;
 *     TreeNode *left;
 *     TreeNode *right;
 *     TreeNode() : val(0), left(nullptr), right(nullptr) {}
 *     TreeNode(int x) : val(x), left(nullptr), right(nullptr) {}
 *     TreeNode(int x, TreeNode *left, TreeNode *right) : val(x), left(left), right(right) {}
 * };
 */

class Solution {
    int res = 0;
public:
    int maxDepth(TreeNode* root) {
        int res = 0;
        res = dfs(root);
        return res;
    }
private:
    int dfs(TreeNode* node){
        if (!node){
            return 0;
        }
        return 1 + max(dfs(node->left), dfs(node->right));
    }
};
