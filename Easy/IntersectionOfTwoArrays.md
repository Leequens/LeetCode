# 问题分析：
给定两个数组，写一个函数来计算它们的交集。
# 编程实现：
```C++
class Solution {
public:
    vector<int> intersection(vector<int>& nums1, vector<int>& nums2) 
    {
        vector<int>res;
        int i=0,j=0;
        sort(nums1.begin(),nums1.end());
        sort(nums2.begin(),nums2.end());
        while (i<nums1.size()&&j<nums2.size())
        {
            if(nums1[i]<nums2[j])
                i++;
            else if(nums1[i]>nums2[j]) 
                j++;
            else
            {
                if(res.empty()||res.back()!=nums1[i]) 
                {
                    res.push_back(nums1[i]);
                }
                i++;
                j++;
            }
        }
        return res;
    }
};
```
# 总结体会：
先给两个数组排序，然后用两个指针分别指向两个数组的开头，然后比较两个数组的大小，把小的数字的指针向后移，如果两个指针指的数字相等，那么看结果res是否为空，如果为空或者是最后一个数字和当前数字不等的话，将该数字加入结果res中，这是因为题目要求返回的res中元素不能重复。