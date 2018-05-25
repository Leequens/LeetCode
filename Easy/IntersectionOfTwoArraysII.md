# 问题分析：
给定两个数组，写一个方法来计算它们的交集。
注意：
   输出结果中每个元素出现的次数，应与元素在两个数组中出现的次数一致。
   我们可以不考虑输出结果的顺序。
# 编程实现：
```C++
class Solution {
public:
    vector<int> intersect(vector<int>& nums1, vector<int>& nums2) 
    {
        vector<int> res;
        int i=0,j=0;
        sort(nums1.begin(),nums1.end());
        sort(nums2.begin(),nums2.end());
        while (i<nums1.size()&&j< nums2.size()) 
        {
            if(nums1[i]==nums2[j])
            {
                res.push_back(nums1[i]);
                i++; 
                j++;
            } 
            else if(nums1[i]>nums2[j])
            {
                j++;
            }
            else
                i++;
        }
        return res;
    }
};
```
# 总结体会：
这个题与上个题要求不同，这道题要求尽可能多的输出相同元素，先给两个数组排序，然后用两个指针分别指向两个数组的起始位置，如果两个指针指的数字相等，则存入结果中，两个指针均自增1，如果第一个指针指的数字大，则第二个指针自增1，反之亦然。