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
    int goodNodes(TreeNode* root) {
        if(!root){
            return 0;
        }
        
        dfs(root, root->val);
        return res;
        
    }
    void dfs(TreeNode* node, int curr){
        if(!node){
            return;
        }
        curr = max(curr, node->val);
        if (node->val >= curr){
            res++;
        }

        if (node->left)dfs(node->left, curr);
        if (node->right) dfs(node->right, curr);
    }
};
