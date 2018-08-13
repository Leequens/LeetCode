# 问题分析：
翻转一棵二叉树。
# 编程实现：
```C++
class Solution {
public:
    TreeNode* invertTree(TreeNode* root) {
        if (!root) return NULL;
        queue<TreeNode*> q;
        q.push(root);
        while (!q.empty()) 
        {
            TreeNode *node = q.front(); 
            q.pop();
            TreeNode *tmp = node->left;
            node->left = node->right;
            node->right = tmp;
            if (node->left) q.push(node->left);
            if (node->right) q.push(node->right);
        }
        return root;
    }
};
```
# 总结体会：
用queue来辅助，先把根节点排入队列中，然后从队中取出来，交换其左右节点，如果存在则分别将左右节点在排入队列中，以此类推直到队列中木有节点了停止循环，返回root即可。