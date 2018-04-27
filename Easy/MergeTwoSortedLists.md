# 问题分析：

将两个有序链表合并为一个新的有序链表并返回。新链表是通过拼接给定的两个链表的所有节点组成的。 
示例：
输入：1->2->4, 1->3->4
输出：1->1->2->3->4->4

# 编程实现：
```C++
class Solution {
public:
    ListNode* mergeTwoLists(ListNode* l1, ListNode* l2) 
    {
        if(l1==NULL) return l2;
        if(l2==NULL) return l1;
        ListNode* new_list=NULL;  
         if(l1->val<l2->val)       
         {  
             new_list=l1;   
             l1=l1->next;   

         }  
         else                         
         {   
             new_list=l2;   
             l2=l2->next;  
        } 
        ListNode * pre=new_list;
        while(l1!=NULL&&l2!=NULL )
        {
            if(l1->val<l2->val)
            {
                pre->next=l1;
                l1=l1->next;
            }
            else
            {
                pre->next=l2;
                l2=l2->next;
            }
            pre=pre->next;
        }
        if(l1)
            pre->next=l1;
        else 
            pre->next=l2;
        return new_list;

    }
};
```
# 总结体会：
首先判断空链表的情况，如果两个都是空链表，那么返回也是空，有一方是空链表，则返回另一方即可；
如果都不是空链表，比较值的大小，小的存入新链表中，然后指向下一个值，当有一个链表比较完毕后，把剩下的另外一个链表直接存入心里暗标即可。