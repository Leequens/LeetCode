# 问题分析：

给定一个排序链表，删除所有重复的元素，使得每个元素只出现一次。

# 编程实现：
```c++
class Solution {
public:
    ListNode* deleteDuplicates(ListNode* head) 
    {
        if(head==NULL||head->next==NULL) 
            return head;
        ListNode *newhead=head;
        while (head->next)
        {
            if(head->val==head->next->val)
                head->next=head->next->next;
            else
                head=head->next;
        }
        return newhead;
    }
};
```
# 总结体会：
首先应该先判断是否为空，然后在用循环语句判断当前的节点的值与下一个节点的值是否相等，如果相等，则将下下一个节点赋值给下一个节点。因为head已经移动到了最后一个节点，所以应该在循环之前设置新的head作为记录，最后返回它。
