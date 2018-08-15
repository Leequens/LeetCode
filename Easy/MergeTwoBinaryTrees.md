# 问题分析：
给定两个二叉树，想象当你将它们中的一个覆盖到另一个上时，两个二叉树的一些节点便会重叠。

你需要将他们合并为一个新的二叉树。合并的规则是如果两个节点重叠，那么将他们的值相加作为节点合并后的新值，否则不为 NULL 的节点将直接作为新二叉树的节点。
# 编程实现：
```C++
class Solution {
public:
    TreeNode* mergeTrees(TreeNode* t1, TreeNode* t2) {
        if (!t1) return t2;
        if (!t2) return t1;
        TreeNode *t = new TreeNode(t1->val + t2->val);
        t->left = mergeTrees(t1->left, t2->left);
        t->right = mergeTrees(t1->right, t2->right);
        return t;
    }
};
```
# 总结体会：
使用递归解决，首先判断，如果t1不存在，则直接返回t2，反之，如果t2不存在，则直接返回t1。如果上面两种情况都不满足，那么以t1和t2的结点值之和建立新结点t，然后对t1和t2的左子结点调用递归并赋给t的左子结点，再对t1和t2的右子结点调用递归并赋给t的右子结点，返回t结点即可。